require('dotenv').config();
const express = require('express');
const fs = require('fs');
const jwt = require('jsonwebtoken');
const OAuth2Server = require('@node-oauth/oauth2-server');
const { Request, Response } = OAuth2Server;
const crypto = require('crypto');


const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


const dataPath = './datos.json';
const oauthModel = require('./oauth-model');
const oauth = new OAuth2Server({
  model: oauthModel,
  accessTokenLifetime: 3600,
  allowBearerTokensInQueryString: true
});


const users = [
  { id: 1, username: 'user', password: 'password' },
  { id: 2, username: 'admin', password: 'admin123' }
];


// ========================================
// 🔥 OWASP ASVS V4.1 NIVEL 3
// ========================================


// V4.1.1 - Content-Type JSON UTF-8
app.use((req, res, next) => {
  if (req.method !== 'OPTIONS') {
    res.set('Content-Type', 'application/json; charset=utf-8');
  }
  next();
});


// V4.1.3 - Trust Proxy (ignora headers fake)
app.set('trust proxy', false);


// V4.1.4 - Solo métodos permitidos (NIVEL 3)
app.use((req, res, next) => {
  const allowed = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'];
  
  if (req.method === 'OPTIONS') {
    res.set({
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': allowed.join(', '),
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Message-Signature'
    });
    return res.status(204).end();
  }
  
  if (!allowed.includes(req.method)) {
    return res.status(405).json({ 
      error: 'V4.1.4 Method Not Allowed',
      allowed: allowed.join(', ')
    }).set('Allow', allowed.join(', '));
  }
  next();
});


// V4.1.5 - HMAC firmas per-message (NIVEL 3)
app.use('/nombres', (req, res, next) => {
  if (!['POST', 'PUT'].includes(req.method)) return next();
  
  const signature = req.get('X-Message-Signature');
  if (!signature) {
    return res.status(401).json({ error: 'V4.1.5 Missing X-Message-Signature' });
  }
  
  const hmacSecret = process.env.API_HMAC_SECRET || 'MiClaveSecretaNode12345678901234567890';
  const hmac = crypto.createHmac('sha256', hmacSecret);
  hmac.update(JSON.stringify(req.body));
  const expected = 'sha256=' + hmac.digest('hex');
  
  if (!crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected))) {
    return res.status(401).json({ error: 'V4.1.5 Invalid HMAC signature' });
  }
  
  console.log('✅ V4.1.5 HMAC válido');
  next();
});


// ========================================
// FUNCIONES
// ========================================
function readData() {
  const data = fs.readFileSync(dataPath, 'utf-8');
  return JSON.parse(data);
}


function writeData(data) {
  fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}


// JWT Auth
function authenticateJWT(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: 'No se proporcionó token' });
  const token = authHeader.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Token inválido' });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET);
    next();
  } catch (err) {
    res.status(403).json({ error: 'Token expirado o inválido' });
  }
}


// OAuth Auth
async function authenticateOAuth(req, res, next) {
  const request = new Request(req);
  const response = new Response(res);
  try {
    await oauth.authenticate(request, response);
    next();
  } catch (err) {
    res.status(err.code || 500).json({ error: 'OAuth failed', message: err.message });
  }
}


// ========================================
// RUTAS
// ========================================
app.get('/saludo', (req, res) => {
  res.json({ mensaje: 'Node.js OWASP ASVS V4.1 Nivel 3 ✅' });
});


// V4.1.3 TEST - Proxy headers
app.get('/ip', (req, res) => {
  res.json({
    realIP: req.ip,
    forwardedIP: req.get('X-Forwarded-For'),
    message: (req.ip === '127.0.0.1' || req.ip === '::1') ? 
      '✅ V4.1.3 PASS: Ignora fake proxy' : '❌ V4.1.3 FAIL'
  });
});


app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ error: 'Username y password requeridos' });
  }
  const user = users.find(u => u.username === username && u.password === password);
  if (!user) return res.status(401).json({ error: 'Credenciales inválidas' });
  
  const payload = { id: user.id, username: user.username };
  const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1h' });
  res.json({ 
    mensaje: 'Login JWT OK [V4.1]', 
    token, 
    usuario: user.username 
  });
});


// OAuth token endpoint - THIS IS YOUR CALLBACK
app.post('/oauth/token', async (req, res) => {
  const request = new Request(req);
  const response = new Response(res);
  try {
    const token = await oauth.token(request, response);
    res.json({
      access_token: token.accessToken,
      token_type: 'Bearer',
      expires_in: 3600,
      message: 'OAuth2 OK [V4.1]'
    });
  } catch (err) {
    res.status(err.code || 500).json({ error: err.message });
  }
});


app.get('/nombres', authenticateOAuth, (req, res) => {
  res.json(readData());
});


app.get('/nombres/:nombre', authenticateOAuth, (req, res) => {
  const nombre = req.params.nombre;
  if (!nombre) return res.status(400).json({ error: 'Nombre requerido' });
  const nombres = readData();
  const resultado = nombres.filter(p => 
    p.nombre.toLowerCase().includes(nombre.toLowerCase())
  );
  if (resultado.length === 0) {
    return res.status(404).json({ mensaje: 'No encontrado' });
  }
  res.json(resultado);
});


app.post('/nombres', authenticateOAuth, (req, res) => {
  const nombres = readData();
  const nuevo = { id: Date.now(), nombre: req.body.nombre || 'Sin nombre' };
  nombres.push(nuevo);
  writeData(nombres);
  res.status(201).json({ mensaje: 'Creado V4.1.5 HMAC OK', data: nuevo });
});


app.put('/nombres/:id', authenticateOAuth, (req, res) => {
  const nombres = readData();
  const id = parseInt(req.params.id);
  const index = nombres.findIndex(p => p.id === id);
  if (index === -1) return res.status(404).json({ error: 'No encontrado' });
  nombres[index].nombre = req.body.nombre;
  writeData(nombres);
  res.json({ mensaje: 'Actualizado V4.1.5 HMAC OK', data: nombres[index] });
});


app.delete('/nombres/:id', authenticateOAuth, (req, res) => {
  const nombres = readData();
  const id = parseInt(req.params.id);
  const nuevos = nombres.filter(p => p.id !== id);
  writeData(nuevos);
  res.status(204).send();
});


// 404
app.use((req, res) => {
  res.status(404).json({ error: 'No encontrado [V4.1 compliant]' });
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 Node.js API V4.1 Nivel 3: http://localhost:${PORT}`);
  console.log('\n🔐 OAuth2 Test:');
  console.log('  curl -X POST http://localhost:3000/oauth/token \\');
  console.log('    -H "Content-Type: application/x-www-form-urlencoded" \\');
  console.log('    -u "test-client:YOUR_OAUTH_SECRET" \\');
  console.log('    -d "grant_type=client_credentials"');
});
