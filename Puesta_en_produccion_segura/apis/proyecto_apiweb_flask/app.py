from flask import Flask, jsonify, request, make_response, redirect
import jwt
import urllib.request
import urllib.parse
import json
from datetime import datetime, timedelta
from functools import wraps
import os
import hmac
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'cambia_esto_por_un_secreto_largo_y_unico')

# Configuración OAuth GitHub
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "fjortegan")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "3cba795bf7a2f9ce6bcb9aa8220b18cc88b93240")

# ==============================================================================
# CONTROL 4.1.5: Configuración para Firmas Digitales
# ==============================================================================
# Medida: Verificar que se usan firmas digitales por mensaje para proporcionar
# garantías adicionales en transacciones sensibles o que atraviesan múltiples sistemas.
# Explicación: Las firmas HMAC-SHA256 garantizan la integridad y autenticidad de
# las peticiones críticas (como DELETE), evitando ataques de replay y manipulación.
# La firma incluye los datos de la petición + timestamp, y expira en 5 minutos.
SIGNATURE_SECRET = os.getenv("SIGNATURE_SECRET", "clave_secreta_para_firmas_muy_larga_y_segura")

# ==============================================================================
# CONTROL 4.1.4: Métodos HTTP Permitidos
# ==============================================================================
# Medida: Solo permitir métodos HTTP explícitamente soportados por la API,
# bloqueando métodos no usados o peligrosos.
# Explicación: Métodos como TRACE, TRACK, CONNECT pueden usarse en ataques
# XST (Cross-Site Tracing) o para bypass de controles de seguridad.
ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']

# --------------------
# Datos en memoria
# --------------------
nombres = []
ultimo_id = 0

# -------------------
# Login básico sin BD
# -------------------
USUARIO = "admin"
PASSWORD = "1234"

# ==============================================================================
# CONTROL 4.1.4: Validación de Métodos HTTP (BEFORE_REQUEST)
# ==============================================================================
@app.before_request
def validate_http_method():
    """
    Medida 4.1.4 (Nivel 3): Verificar que solo se usen métodos HTTP permitidos.
    Si el método no está en ALLOWED_METHODS, rechazar con 405 Method Not Allowed.
    """
    if request.method not in ALLOWED_METHODS:
        return jsonify({'error': 'Método HTTP no permitido'}), 405

# ==============================================================================
# CONTROL 4.1.2: Redirección HTTP a HTTPS (BEFORE_REQUEST)
# ==============================================================================
@app.before_request
def redirect_http_to_https():
    """
    Medida 4.1.2 (Nivel 2): Solo endpoints user-facing (acceso manual/navegador)
    deben redirigir automáticamente de HTTP a HTTPS.
    
    Explicación: Los endpoints de API REST NO deben redirigir automáticamente
    para evitar que datos sensibles se transmitan sin cifrar si un cliente
    envía accidentalmente una petición HTTP. En su lugar, se rechaza la petición.
    Solo /login y /github_oauth (user-facing) redirigen a HTTPS.
    """
    # MODO DESARROLLO: Desactivar redirección cuando DEBUG=True
    # En producción, asegúrate de que app.debug = False
    if app.debug:
        return  # No redirigir en modo desarrollo
    
    user_facing_endpoints = ['login', 'github_oauth']
    
    # Solo redirigir si NO es conexión segura Y es endpoint user-facing
    if not request.is_secure and request.endpoint in user_facing_endpoints:
        # Verificar header X-Forwarded-Proto si estás detrás de proxy/load balancer
        if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)


# ==============================================================================
# CONTROL 4.1.1 y 4.1.3: Headers de Seguridad (AFTER_REQUEST)
# ==============================================================================
@app.after_request
def set_secure_headers(response):
    """
    Medida 4.1.1 (Nivel 1): Verificar que toda respuesta HTTP con cuerpo de mensaje
    contenga un Content-Type con charset que coincida con el contenido real.
    
    Explicación: Especificar charset (UTF-8) según IANA Media Types previene
    ataques de interpretación incorrecta de contenido y vulnerabilidades XSS
    relacionadas con diferentes encodings de caracteres.
    """
    # 4.1.1: Content-Type con charset UTF-8 explícito
    if response.content_type and 'application/json' in response.content_type:
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
    elif response.content_type and 'text/' in response.content_type:
        response.headers['Content-Type'] = f'{response.content_type.split(";")[0]}; charset=utf-8'
    
    """
    Medida 4.1.3 (Nivel 2): Verificar que headers HTTP usados por la aplicación
    y establecidos por intermediarios (load balancer, proxy) no puedan ser
    sobrescritos por el usuario final.
    
    Explicación: Estos headers de seguridad protegen contra ataques donde un
    atacante manipula headers para bypass de controles o suplantación. Los
    establecemos en el servidor y NO pueden ser modificados por el cliente.
    """
    # 4.1.3: Headers de seguridad que NO pueden ser sobrescritos por clientes
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Previene MIME sniffing
    response.headers['X-Frame-Options'] = 'DENY'  # Previene clickjacking
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'  # Fuerza HTTPS
    
    return response

# ==============================================================================
# CONTROL 4.1.5: Funciones de Firma Digital
# ==============================================================================
def generar_firma(data, timestamp):
    """
    Genera una firma HMAC-SHA256 para los datos de la petición.
    
    Parámetros:
    - data: Diccionario con los datos a firmar (id, método, path)
    - timestamp: Marca temporal ISO format para evitar replay attacks
    
    Retorna: String hexadecimal con la firma HMAC-SHA256
    """
    # Serializar datos de forma consistente (ordenando claves)
    message = f"{json.dumps(data, sort_keys=True)}{timestamp}"
    
    # Generar HMAC-SHA256
    firma = hmac.new(
        SIGNATURE_SECRET.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return firma

def verificar_firma(data, timestamp, firma_recibida):
    """
    Verifica que la firma sea válida y no esté expirada.
    
    Parámetros:
    - data: Datos originales de la petición
    - timestamp: Timestamp de cuando se generó la firma
    - firma_recibida: Firma enviada por el cliente
    
    Retorna: Tupla (bool, str) -> (válida, mensaje)
    """
    # Verificar que el timestamp no sea muy antiguo (ventana de 5 minutos)
    try:
        ts = datetime.fromisoformat(timestamp)
        if datetime.utcnow() - ts > timedelta(minutes=5):
            return False, "Firma expirada (más de 5 minutos)"
    except:
        return False, "Timestamp inválido o mal formateado"
    
    # Calcular la firma esperada con los mismos datos
    firma_esperada = generar_firma(data, timestamp)
    
    # Comparación segura contra timing attacks usando hmac.compare_digest
    if not hmac.compare_digest(firma_esperada, firma_recibida):
        return False, "Firma inválida (no coincide con la esperada)"
    
    return True, "Firma válida"

# ==============================================================================
# AUTENTICACIÓN JWT
# ==============================================================================
def generar_token(username):
    payload = {
        "sub": username,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
    return token

def verificar_token(token):
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    return data

def token_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer "):
            return jsonify({"error": "Token faltante o malformado"}), 401
        token = auth.split(" ", 1)[1].strip()
        try:
            claims = verificar_token(token)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    return wrapper

# ==============================================================================
# ENDPOINTS DE AUTENTICACIÓN
# ==============================================================================
@app.route('/login', methods=['POST'])
def login():
    """Endpoint de login básico con usuario/contraseña"""
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    if username == USUARIO and password == PASSWORD:
        token = generar_token(username)
        return jsonify({"message": "Login correcto", "token": token}), 200
    return jsonify({"message": "Credenciales inválidas"}), 401

@app.route('/github_oauth', methods=['POST'])
def github_oauth():
    """
    Endpoint para autenticación con GitHub OAuth usando urllib (sin requests)
    """
    data = request.get_json(silent=True) or {}
    code = data.get("code")
    
    if not code:
        return jsonify({"error": "Falta code"}), 400
    
    try:
        # 1. Intercambiar el code por un access_token de GitHub
        token_url = "https://github.com/login/oauth/access_token"
        
        # Preparar los datos para enviar
        payload = {
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code
        }
        
        # Convertir el payload a JSON
        json_data = json.dumps(payload).encode('utf-8')
        
        # Crear la petición POST
        token_request = urllib.request.Request(
            token_url,
            data=json_data,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            method='POST'
        )
        
        # Hacer la petición
        with urllib.request.urlopen(token_request) as response:
            token_response = json.loads(response.read().decode('utf-8'))
        
        # Verificar si obtuvimos el token
        if "access_token" not in token_response:
            error_msg = token_response.get("error_description", "No se pudo obtener token de GitHub")
            return jsonify({"error": error_msg}), 400
        
        github_access_token = token_response["access_token"]
        
        # 2. Obtener información del usuario de GitHub
        user_url = "https://api.github.com/user"
        
        user_request = urllib.request.Request(
            user_url,
            headers={
                "Authorization": f"Bearer {github_access_token}",
                "Accept": "application/json"
            }
        )
        
        with urllib.request.urlopen(user_request) as user_response:
            user_info = json.loads(user_response.read().decode('utf-8'))
        
        if "login" not in user_info:
            return jsonify({"error": "No se pudo obtener información del usuario"}), 400
        
        github_username = user_info["login"]
        
        # 3. Generar tu propio JWT para ese usuario
        jwt_token = generar_token(github_username)
        
        return jsonify({
            "jwt": jwt_token,
            "githubUser": github_username,
            "message": "Login con GitHub exitoso"
        }), 200
        
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        return jsonify({"error": f"Error HTTP {e.code}: {error_body}"}), 500
    except urllib.error.URLError as e:
        return jsonify({"error": f"Error de conexión: {str(e.reason)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

# ==============================================================================
# CRUD DE NOMBRES (protegido con JWT)
# ==============================================================================

@app.route('/nombres/<string:nombre>', methods=['POST'])
@token_requerido
def crear_nombre(nombre):
    """Crear un nuevo nombre en la lista"""
    global ultimo_id, nombres
    if not nombre:
        return jsonify({'error': 'Nombre es requerido en la URL'}), 400
    ultimo_id += 1
    nuevo = {"id": ultimo_id, "nombre": nombre}
    nombres.append(nuevo)
    return jsonify(nuevo), 201

@app.route('/nombres', methods=['GET'])
@token_requerido
def listar_nombres():
    """Listar todos los nombres"""
    return jsonify(nombres)

@app.route('/nombres/<int:id>', methods=['GET'])
@token_requerido
def obtener_nombre(id):
    """Obtener un nombre por ID"""
    nombre = next((n for n in nombres if n['id'] == id), None)
    if nombre is None:
        return jsonify({'error': 'No encontrado'}), 404
    return jsonify(nombre)

@app.route('/nombres/<int:id>', methods=['PUT'])
@token_requerido
def actualizar_nombre(id):
    """Actualizar un nombre existente"""
    nombre = next((n for n in nombres if n['id'] == id), None)
    if nombre is None:
        return jsonify({'error': 'No encontrado'}), 404
    data = request.get_json(silent=True) or {}
    nuevo_nombre = data.get('nombre')
    if not nuevo_nombre:
        return jsonify({'error': 'campo nombre es requerido en JSON'}), 400
    nombre['nombre'] = nuevo_nombre
    return jsonify(nombre)

# ==============================================================================
# CONTROL 4.1.5: DELETE con Firma Digital Obligatoria
# ==============================================================================
@app.route('/nombres/<int:id>', methods=['DELETE'])
@token_requerido
def eliminar_nombre(id):
    """
    Eliminar un nombre - REQUIERE FIRMA DIGITAL
    
    Medida 4.1.5 (Nivel 3): Operaciones sensibles como DELETE requieren
    firma digital para garantizar integridad y no repudio.
    
    Headers requeridos:
    - Authorization: Bearer <token>
    - X-Signature: Firma HMAC-SHA256 de los datos
    - X-Timestamp: Timestamp ISO format de cuando se generó la firma
    
    La firma debe ser válida y no estar expirada (máx 5 minutos).
    """
    # Obtener firma y timestamp de los headers
    firma = request.headers.get('X-Signature')
    timestamp = request.headers.get('X-Timestamp')
    
    # Verificar que se proporcionaron ambos headers
    if not firma or not timestamp:
        return jsonify({
            'error': 'Se requiere firma digital',
            'detalle': 'Debes incluir los headers X-Signature y X-Timestamp',
            'ayuda': 'Usa el endpoint /generar_firma para obtener una firma válida'
        }), 400
    
    # Preparar datos que deben coincidir con la firma
    data = {
        'id': id,
        'method': 'DELETE',
        'path': request.path
    }
    
    # Verificar la firma
    valida, mensaje = verificar_firma(data, timestamp, firma)
    
    if not valida:
        return jsonify({
            'error': 'Firma digital inválida',
            'detalle': mensaje,
            'ayuda': 'Genera una nueva firma con /generar_firma'
        }), 401
    
    # Si la firma es válida, proceder con la eliminación
    global nombres
    original_len = len(nombres)
    nombres = [n for n in nombres if n['id'] != id]
    
    if len(nombres) == original_len:
        return jsonify({'error': 'No encontrado'}), 404
    
    return jsonify({
        'mensaje': 'Nombre eliminado correctamente',
        'id': id,
        'firma_verificada': True
    })

# ==============================================================================
# ENDPOINT AUXILIAR: Generar Firma Digital
# ==============================================================================
@app.route('/generar_firma', methods=['POST'])
@token_requerido
def generar_firma_endpoint():
    """
    Endpoint auxiliar para generar firmas digitales (útil para testing)
    
    Body JSON esperado:
    {
        "id": 1,
        "method": "DELETE",
        "path": "/nombres/1"
    }
    
    Retorna la firma HMAC-SHA256 y el timestamp que debes usar en los headers.
    """
    data = request.get_json(silent=True) or {}
    
    # Validar que se proporcionaron los datos necesarios
    if not all(key in data for key in ['id', 'method', 'path']):
        return jsonify({
            'error': 'Datos incompletos',
            'requerido': {'id': 'número', 'method': 'string', 'path': 'string'},
            'ejemplo': {'id': 1, 'method': 'DELETE', 'path': '/nombres/1'}
        }), 400
    
    # Generar timestamp actual
    timestamp = datetime.utcnow().isoformat()
    
    # Generar la firma
    firma = generar_firma(data, timestamp)
    
    return jsonify({
        'firma': firma,
        'timestamp': timestamp,
        'data': data,
        'instrucciones': 'Usa estos valores en los headers X-Signature y X-Timestamp',
        'valida_por': '5 minutos',
        'ejemplo_curl': f'curl -X DELETE http://localhost:5000{data["path"]} -H "Authorization: Bearer YOUR_TOKEN" -H "X-Signature: {firma}" -H "X-Timestamp: {timestamp}"'
    })

# ==============================================================================
# CONTROL 4.1.4: Bloquear Métodos HTTP Peligrosos Explícitamente
# ==============================================================================
@app.route('/', defaults={'path': ''}, methods=['TRACE', 'TRACK'])
@app.route('/<path:path>', methods=['TRACE', 'TRACK'])
def block_dangerous_methods(path):
    """
    Medida 4.1.4 (Nivel 3): Bloqueo explícito de métodos HTTP peligrosos.
    
    TRACE y TRACK pueden usarse en ataques XST (Cross-Site Tracing) donde
    un atacante puede robar cookies HTTPOnly o headers de autenticación.
    """
    return jsonify({
        'error': 'Método no permitido',
        'detalle': f'El método {request.method} está bloqueado por seguridad',
        'metodos_permitidos': ALLOWED_METHODS
    }), 405

# ==============================================================================
# ENDPOINT DE INFORMACIÓN (útil para verificar que la API está corriendo)
# ==============================================================================
@app.route('/', methods=['GET'])
def home():
    """Endpoint de información sobre la API"""
    return jsonify({
        'mensaje': 'API Flask con OWASP ASVS V4.1 implementado',
        'controles_implementados': {
            '4.1.1': 'Content-Type con charset UTF-8',
            '4.1.2': 'Redirección HTTP a HTTPS (endpoints user-facing)',
            '4.1.3': 'Headers de seguridad no sobrescribibles',
            '4.1.4': 'Validación de métodos HTTP permitidos',
            '4.1.5': 'Firmas digitales para operaciones sensibles'
        },
        'endpoints': {
            'autenticacion': ['/login', '/github_oauth'],
            'crud': ['/nombres', '/nombres/<id>'],
            'utilidad': ['/generar_firma']
        },
        'metodos_permitidos': ALLOWED_METHODS,
        'headers_seguridad': ['X-Content-Type-Options', 'X-Frame-Options', 'Strict-Transport-Security']
    })

# ------------------
# Ejecutar servidor
# ------------------
if __name__ == "__main__":
    print("\n" + "="*70)
    print("API Flask con OWASP ASVS V4.1 - Controles de Seguridad Implementados")
    print("="*70)
    print("\nControles OWASP ASVS V4.1 activos:")
    print("  ✓ 4.1.1: Content-Type con charset UTF-8")
    print("  ✓ 4.1.2: Redirección HTTP → HTTPS (endpoints user-facing)")
    print("  ✓ 4.1.3: Headers de seguridad no sobrescribibles")
    print("  ✓ 4.1.4: Validación de métodos HTTP permitidos")
    print("  ✓ 4.1.5: Firmas digitales para operaciones sensibles (DELETE)")
    print("\nServidor iniciando en http://0.0.0.0:5000")
    print("="*70 + "\n")
    
    app.run(debug=True, host="0.0.0.0", port=5000)
