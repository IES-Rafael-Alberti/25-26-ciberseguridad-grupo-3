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

## 3. Índice de Figuras
- Figura 1. Comprobación de integridad de hashes en PowerShell.
- Figura 2. Extracto del archivo access.registro con peticiones a ping.php.
- Figura 3. Localización de ping.php en FTK Imager.
- Figura 4. Contenido del archivo ping.php visualizado en Visual Studio Code.
- Figura 5. Localización de passwd.txt en FTK Imager.
- Figura 6. Contenido del archivo passwd.txt.
- Figura 7. Propiedades y fecha de modificación de passwd.txt.
- Figura 8. Análisis de cadenas en la captura de memoria RAM.
- Figura 9. registro de Samba con la IP del atacante en FTK Imager.
- Figura 10. Extracto del access.registro con información del cliente del atacante.

## 4. Resumen Ejecutivo
El presente informe documenta el análisis forense realizado sobre un servidor Linux comprometido mediante la explotación de una vulnerabilidad crítica de inyección de comandos del sistema operativo (CWE-78) presente en una aplicación web desarrollada en PHP. El atacante, cuya dirección IP es 192.168.1.6, utilizó esta vulnerabilidad para generar un volcado de credenciales del sistema y, presumiblemente, exfiltrarlo. El análisis de la imagen de disco y la captura de memoria RAM ha permitido reconstruir el vector de ataque, identificar los artefactos creados por el intruso y proponer medidas correctivas.

## 5. Introducción
### 5.1 Antecedentes
El técnico responsable del centro de datos de la empresa afectada, recibió una notificación de posible incidente de seguridad que alertaba sobre la exfiltración de datos sensibles desde un servidor interno. Ante la gravedad del incidente, la empresa contrató al equipo pericial para determinar el alcance del ataque, identificar al equipo responsable y proponer medidas de remediación.

### 5.2 Objetivos
El encargo pericial persigue los siguientes objetivos:

1. Identificar la vulnerabilidad de la aplicación web que fue explotada.

2. Determinar la dirección IP, el cliente de navegación y el sistema operativo del atacante.

3. Descubrir qué datos fueron exfiltrados del servidor comprometido.

4. Analizar por qué el archivo original de contraseñas no muestra actividad durante el incidente.

5. Proponer medidas de remediación para corregir la vulnerabilidad explotada.
