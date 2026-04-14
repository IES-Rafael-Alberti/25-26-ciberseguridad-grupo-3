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

## 6. Fuentes de Información
Las evidencias digitales proporcionadas por el cliente para el análisis son las siguientes:

| Evidencia                        | Descripción                                                              |
| -------------------------------- | ------------------------------------------------------------------------ |
| Imagen de disco                  | Imagen forense del servidor Linux comprometido                           |
| Volcado de memoria RAM           | Captura de la memoria volátil del sistema en el momento del incidente    |
| Perfil de memoria                | Perfil necesario para el análisis del volcado con Volatility             |
| Archivo de sumas de verificación | Archivo hashes_sha256.txt con los valores hash SHA-256 de las evidencias |

### 6.1 Adquisición de Evidencias
Antes de iniciar cualquier análisis, se procedió a verificar la integridad de las evidencias comparando los valores hash SHA-256 proporcionados por el cliente con los calculados sobre los archivos recibidos. Esta verificación se realizó mediante PowerShell y los resultados confirmaron que las evidencias no habían sido alteradas desde su adquisición, garantizando así la cadena de custodia. 

![figura 1](<img/2026-04-13 19_48_18-Windows PowerShell.png>)
(Figura 1) Comprobación de sumas de integridad mediante herramienta Get-FileHash de windows Powershell

## 7. Análisis

### 7.1 Herramientas Utilizadas

| Herramienta             | Versión              | Uso                                          |
| ----------------------- | -------------------- | -------------------------------------------- |
| Exterro FTK Imager      | 8.2.0.26             | Análisis de la imagen de disco               |
| Volatility              | 2.x                  | Análisis del volcado de memoria RAM          |
| PowerShell              | Integrado en Windows | Verificación de hashes SHA-256               |
| Visual Studio Code      | Actual               | Revisión del contenido de archivos extraídos |
| Bloc de notas (Windows) | Integrado            | Revisión de registros de texto plano              |

### 7.2 Procesos
#### 7.2.1 Análisis de la vulnerabilidad web
La investigación comenzó con el análisis del archivo de registro de accesos de Apache, localizado en /var/registro/apache2/access.registro. En dicho archivo se observaron múltiples peticiones dirigidas al recurso ping.php, lo que motivó una inspección directa del archivo. 

![alt text](<img/2026-04-13 19_12_08-access.registro_ Bloc de notas.png>)
(Figura 2) Registro de peticiones a ese archivo

![alt text](<img/2026-04-13 19_13_44-Exterro FTK Imager 8.2.0.26.png>)
(Figura 3) Localización del archivo

El archivo ping.php, localizado en el directorio raíz del servidor web, con ruta /root/var/www/ping.php , contiene el siguiente fragmento de código en su línea 19:

```echo(system('ping -c 1 ' . $_POST['ping']));```

El valor recibido a través del parámetro ping del formulario se concatena directamente en una llamada a la función system() de PHP sin ningún tipo de validación ni saneamiento previo. Esto constituye una vulnerabilidad de inyección de comandos del sistema operativo, clasificada bajo el identificador CWE-78 (Improper Neutralization of Special Elements used in an OS Command). 

![alt text](<img/2026-04-13 19_15_01-ping.php - Proyecto 5 - Incident on Linux Server I - Visual Studio Code.png>)
(Figura 4) Código completo del archivo ping.php

En lugar de ejecutar únicamente el comando ping, el servidor ejecutaría cualquier instrucción adicional con los mismos privilegios que el proceso web, permitiendo desde la lectura de archivos sensibles hasta el establecimiento de un acceso remoto completo. La vulnerabilidad guarda similitud con CVE-2012-1823, que afecta a PHP en modo CGI, aunque su explotación en este caso no se basa necesariamente en dicho vector, sino en una mala práctica de programación del propio desarrollador de la aplicación.

#### 7.2.2 Análisis de la identidad del atacante
El análisis del archivo access.registro permitió identificar de forma inequívoca los datos del agente que interactuó con la vulnerabilidad. (Figura 10)

| Campo                     | Valor                                   |
| ------------------------- | --------------------------------------- |
| Dirección IP del atacante | 192.168.1.6                             |
| Navegador utilizado       | Firefox 78.0 ESR                        |
| Sistema operativo         | Linux x86_64 (probablemente Kali Linux) |

La dirección IP pertenece al rango de red local, lo que sugiere que el atacante operó desde dentro de la misma red o a través de un sistema comprometido en la misma subred.

#### 7.2.3 Análisis de los datos exfiltrados
En el mismo directorio que ping.php se localizó un archivo denominado passwd.txt cuya presencia no corresponde a ningún componente legítimo de la aplicación web. 

![alt text](<img/2026-04-13 19_16_21-Exterro FTK Imager 8.2.0.26.png>)
(Figura 5) Archivo passwd.txt en la carpeta junto a ping.php

El contenido del archivo corresponde a un volcado de credenciales del sistema, presumiblemente generado mediante un comando del tipo cat /etc/passwd o similar inyectado a través de la vulnerabilidad descrita.

![alt text](<img/2026-04-13 19_16_58-passwd.txt_ Bloc de notas.png>)
(Figura 6) Contenido del archivo passwd.txt

La fecha de modificación del archivo, visible en sus propiedades, coincide con la franja temporal de las peticiones maliciosas registradas en el access.registro, lo que refuerza la relación causal entre ambos artefactos. 

![alt text](<img/2026-04-13 19_38_25-Propiedades_ passwd.txt.png>)
(Figura 7) Se muestra le fecha de modificación como el día del ataque, con una hora muy cercana a los registros de seguridad.

El análisis de cadenas sobre el volcado de memoria RAM reveló lo que probablemente son los parámetros empleados por el atacante para generar el archivo y, con posterioridad, recuperarlo del servidor. 

![alt text](<img/2026-04-13 19_48_18-Windows PowerShell.png>)
(Figura 8)

Adicionalmente, se identificó la presencia de un registro de actividad del servicio Samba que contiene la dirección IP del atacante. Sin embargo, el registro se encontraba vacío, lo que parece indicar que la conexión al servicio fue intentada pero no consumada, o que no se registró actividad de transferencia efectiva a través de ese protocolo. 

![alt text](<img/2026-04-13 19_35_45-Exterro FTK Imager 8.2.0.26.png>)
(Figura 9) posición y nombre del registro de samba

## 8. Limitaciones
Durante el análisis se identificaron las siguientes limitaciones que podrían condicionar parcialmente las conclusiones:

1. La dirección IP del atacante (192.168.1.6) pertenece al espacio de red privado RFC 1918, lo que impide atribuir el ataque a una ubicación geográfica o entidad externa de forma directa. No es posible descartar que dicha IP corresponda a una máquina comprometida usada como punto de salto.

2. El registro de Samba estaba vacío y no se ha encontrado más actividad relcionada en volcado de memoria, por lo que no se puede confirmar con certeza si la exfiltración se completó a través de ese protocolo o si se empleó otro vector de transferencia no registrado en los artefactos disponibles.

3. El análisis de la memoria RAM proporciona indicios del método empleado, pero las cadenas recuperadas no constituyen por sí solas prueba definitiva sin un análisis de proceso más profundo mediante Volatility.

## 9. Conclusiones
El análisis forense realizado permite establecer con un alto grado de certeza que:

1. El servidor fue comprometido a través de una vulnerabilidad de inyección de comandos del sistema operativo presente en el archivo ping.php.
   
2. El atacante operó desde la dirección IP 192.168.1.6 utilizando Firefox 78.0 sobre un sistema Linux x86_64. 
   
3. El atacante aprovechó la ausencia de validación de entradas en dicho archivo para ejecutar comandos arbitrarios en el servidor con los privilegios del proceso web.

4. Como consecuencia de la explotación, se generó el archivo passwd.txt con el volcado de las credenciales del sistema, cuya fecha de modificación coincide con los eventos registrados en el registro de Apache. El archivo original /etc/passwd no muestra actividad porque fue únicamente leído, operación que no deja huella en sus metadatos de modificación.

## 10. Anexos

### Anexo 1. Sobre el Perito
El presente informe ha sido elaborado por los integrantes del Grupo 3 del módulo de Análisis Forense Informático, en el marco de la asignatura correspondiente al ciclo formativo de grado superior. Los autores actúan en calidad de peritos designados a efectos académicos y no ostentan ningún interés particular en el resultado del análisis.

### Anexo 2. Sumas de Verificación
La integridad de las evidencias analizadas fue verificada correctamente. Los valores obtenidos coincidieron con los registrados en el archivo hashes_sha256.txt proporcionado por el cliente, confirmando que las evidencias no fueron modificadas tras su adquisición.


| Evidencia                    | Estado de integridad          |
| ---------------------------- | ----------------------------- |
| Imagen de disco del servidor | Verificada — hash coincidente |
| Volcado de memoria RAM       | Verificada — hash coincidente |
| Perfil de memoria            | Verificada — hash coincidente |

[enlace al archivo de comprobación](./hallazgos/Tablas de Integridad Forense .pdf)

[enlace al archivo de comprobación](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Analisis_forense/Proyecto_05/hallazgos/Tablas%20de%20Integridad%20Forense.pdf)

### Anexo 3. Índice de Hallazgos
#### Hallazgo 1: ping.php

- **Ruta**: /var/www/html/ping.php
- **Descripción**: Archivo PHP con vulnerabilidad de inyección de comandos del sistema operativo (CWE-78). La entrada del usuario se concatena directamente en una llamada a system() sin saneamiento.
- **Relevancia**: Vector de ataque principal utilizado por el intruso.

#### Hallazgo 2: passwd.txt

- **Ruta**: /var/www/html/passwd.txt
- **Descripción**: Archivo de texto generado por el atacante que contiene el volcado de credenciales del sistema obtenido a través de la vulnerabilidad.
- **Relevancia**: Evidencia directa de los datos exfiltrados.

#### Hallazgo 3: access.log

- **Ruta**: /var/registro/apache2/access.registro
- **Descripción**: Registro de accesos del servidor web Apache. Contiene las peticiones realizadas por el atacante, incluyendo su dirección IP, agente de usuario y marcas temporales.
- **Relevancia**: Fuente principal para la atribución del ataque. 

#### Hallazgo 4: registro de Samba

- **Ruta**: /var/registro/samba/ (archivo correspondiente a la IP 192.168.1.6)
- **Descripción**: Registro de actividad del servicio Samba que recoge el intento de conexión desde la IP del atacante. El archivo se encontraba vacío.
- **Relevancia**: Indica un posible intento de exfiltración a través de SMB, aunque no se puede confirmar su consumación.

#### Hallazgo 5: Cadenas en memoria RAM

- **Fuente**: Volcado de memoria RAM analizado con Volatility.
- **Descripción**: Cadenas de texto recuperadas de la memoria que corresponden con los parámetros probablemente utilizados por el atacante para crear passwd.txt y recuperarlo del servidor.
- **Relevancia**: Corrobora el método de explotación y la intención de exfiltración.
