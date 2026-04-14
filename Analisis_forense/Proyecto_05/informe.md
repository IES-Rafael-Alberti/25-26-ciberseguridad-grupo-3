# Informe Pericial Forense: Proyecto 5: Incident on Linux Server I
### Grupo 3 — Análisis Forense Digital

## 1. Juramento y Declaración de Abstención y Tacha

Los peritos firmantes declaran bajo juramento que el presente informe ha sido elaborado con objetividad, imparcialidad y rigor técnico, sin que concurra ninguna causa de abstención o tacha que pudiera comprometer la independencia del análisis realizado. El equipo no mantiene ninguna relación personal ni profesional con las partes implicadas en el incidente que pudiera influir en las conclusiones aquí expuestas.

## 2. Palabras Clave

 - **Vulnerabilidad crítica**: Fallo grave en un sistema informático que permite a un atacante externo realizar acciones no autorizadas sobre él.

- **Inyección de comandos del sistema operativo (CWE-78)**: Tipo de ataque en el que un intruso introduce instrucciones maliciosas en un campo de texto de una aplicación web, engañando al servidor para que las ejecute como si fueran órdenes legítimas del sistema.

- **Aplicación web**: Programa informático accesible desde un navegador de internet, como un formulario o una tienda online.

- **PHP**: Lenguaje de programación ampliamente utilizado para construir aplicaciones web que se ejecutan en el servidor.

- **Exfiltración de datos**: Extracción no autorizada de información confidencial desde un sistema informático hacia el exterior.

- **Imagen de disco**: Copia exacta e íntegra del contenido de un disco duro, utilizada en análisis forense para estudiar el sistema sin alterar el original.

- **Volcado de memoria RAM**: Captura instantánea del contenido de la memoria activa de un ordenador en un momento concreto, que puede revelar programas en ejecución, contraseñas o actividad reciente.

- **Registro de acceso web (access.registro)**: Archivo que guarda automáticamente un historial de todas las peticiones recibidas por un servidor web, incluyendo la dirección IP del visitante, la fecha y hora, y el recurso solicitado.

- **Servidor Linux**: Ordenador que utiliza el sistema operativo Linux para ofrecer servicios en red, muy común en entornos empresariales y centros de datos.

- **Cadena de custodia**: Proceso de documentación que garantiza que las evidencias digitales no han sido manipuladas desde su recogida hasta su análisis.