# **Proyecto 3: Unfaithful Employee**

## **Informe de Análisis Forense**

**Analistas:** Jose M\!ª Escalón Prada, Daniel Hernández Gómez, Abel García Dominguez, David Jimenez.  
**Fecha:** 02 de febrero de 2026  
**Caso:** Investigación interna de la empresa InnovaTech Solutions  
**Sujeto:** Richard Eduardo Warner

# **1\. Investigación del Incidente**

A continuación, se presentan las respuestas a las cuestiones planteadas en la fase de investigación, basadas en el análisis de la imagen forense del disco duro del empleado.

## **1.1 Verificación de Integridad de la Imagen**

Se ha procedido a la verificación de la integridad de la evidencia digital comparando los hashes de la imagen adquirida con los proporcionados originalmente por el departamento de sistemas (Alan).

**Hashes Proporcionados (Cadena de Custodia):**

* **MD5:** dfdfba2231e3fa409676b1b737474208  
* **SHA-1:** f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c  
* **SHA-256:** 66d6ee7a61ea7a986e8f6bb54b9986f79d95b5a0278bef86678ed42ace320d96  
  **Hashes Calculados (Evidencia Analizada):**  
* **MD5:** DFDFBA2231E3FA409676B1B737474288   
* **SHA-1:** F476A81089A10F9D5393AA8C2F8BBCCDB87F7D3C   
* **SHA-256:** 66D6EE7A61EA7A986E8F6BB54B9986F79D95B5A0278BEF86678ED42ACE320D9B  
  **Conclusión:** Existen discrepancias en los valores MD5 y SHA-256. Aunque el SHA-1 coincide, la integridad de la imagen podría estar comprometida o haber errores en la documentación inicial de los hashes. Se procede con el análisis, documentando esta anomalía.

  ## **1.2 Identificación de Usuario y Última Conexión**

  Mediante el análisis del registro SAM (C:/Windows/System32/config/SAM/) utilizando la herramienta **Windows Registry Recovery (WRR)**, se confirma la existencia de la cuenta de usuario asociada al empleado.  
* **Usuario:** Richard  
* **Último inicio de sesión:** 22 de febrero de 2023 a las 13:55:18 (UTC/Local).

  ## **1.3 Información del Sistema**

  El análisis de los registros SYSTEM y SOFTWARE ha revelado la siguiente configuración del equipo:  
* **Nombre del Equipo (Hostname):** LADRONERA  
  * *Fuente:* \\SYSTEM\\ControlSet001\\Control\\ComputerName\\ComputerName  
* **Sistema Operativo:** Windows 10 Pro Education N  
  * *Fuente:* \\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion

  ## **1.4 Uso de Dispositivos USB**

  A pesar de las políticas corporativas, se ha detectado la conexión de un dispositivo de almacenamiento externo.

* **Dispositivo:** Kingston DataTraveler 3.0 USB Device  
* **Primera conexión registrada:** 22 de febrero de 2023 a las 00:27:42.  
  * *Evidencia:* Clave de registro \\SYSTEM\\CurrentControlSet\\Enum\\STORAGE\\... analizada con **Registry Explorer**.

  ## **1.5 Actividad en Línea (Navegación Web)**

  El análisis del historial de navegación (Firefox y Opera) muestra un uso indebido de los recursos de la empresa con fines de ocio y personales:

* **Streaming y Cine:** Búsquedas relacionadas con la película "Trabajo Basura" y acceso a la plataforma "CUEVANAHD".  
* **Compras y Moda:** Navegación en portales como El Corte Inglés y Bershka.  
* **Apuestas:** Acceso a la plataforma de trading y apuestas eToro.  
* **Deportes:** Búsquedas recurrentes de noticias deportivas en el navegador Opera.

  ## **1.6 Planes de Viaje y Movilidad**

  Se ha identificado actividad reciente relacionada con la planificación de un viaje tras su salida de la empresa:  
* **Vuelos:** Búsquedas de vuelos en el portal Vueling.  
* **Alojamiento:** Búsqueda activa de hoteles en "Las Palmas de Gran Canaria" a través de Booking.com.

  ## **1.7 Software no Autorizado al Inicio**

  Se ha verificado la persistencia de aplicaciones en el inicio del sistema mediante el análisis del fichero NTUSER.DAT del usuario Richard (\\Software\\Microsoft\\Windows\\CurrentVersion\\Run).  
* **Hallazgo:** El navegador **Opera** está configurado para ejecutarse automáticamente al iniciar sesión.  
* **Otros navegadores:** Se detectó la instalación de Mozilla Firefox (ruta ROOT\\Mozilla\\Mozilla Firefox en registro SOFTWARE), pero no está configurado en el inicio automático.

  ## **1.8 Exfiltración de Información**

  El análisis del cliente de correo **Thunderbird** (C:\\Users\\Richard\\AppData\\Roaming\\Thunderbird\\Profiles\\tvtlv94f.default-release\\) mediante SysTools M**BOX Viewer** confirma la filtración de datos confidenciales.  
* **Interlocutor:** `proba2.seguridade@gmail.com` (Competencia).  
* **Remitente:** `proba1.seguridade@gmail.com` (Richard).  
* **Hechos:**  
  1. Richard solicita un aumento salarial a la competencia.  
  2. Envía como "prueba" un archivo confidencial **pom.xml** (perteneciente al proyecto *reverb-master*) el 22/02/2023.  
  3. Posteriormente, envía un enlace a Google Drive protegido con contraseña, exigiendo un pago en Bitcoin para liberar el acceso completo al material exfiltrado.

  # **2\. Informe Técnico Detallado**

  ## **2.1 Introducción y Objetivos**

  El presente informe técnico recoge los resultados del análisis forense digital realizado sobre el disco duro asignado al empleado Richard Eduardo Warner. La investigación fue solicitada por InnovaTech Solutions tras detectar comportamientos anómalos y una salida abrupta del empleado.

  Los objetivos principales han sido:

1. Verificar la integridad de la evidencia.  
2. Reconstruir la línea de tiempo de actividades del usuario.  
3. Detectar fugas de información y uso indebido de recursos corporativos.

   ## **2.2 Metodología y Herramientas**

   Se ha seguido una metodología forense estándar de identificación, preservación, análisis y documentación. Las herramientas utilizadas incluyen:  
* **Windows Registry Recovery (WRR) y Registry Explorer:** Para el análisis de colmenas del registro (SAM, SYSTEM, SOFTWARE, NTUSER.DAT).  
* **SysTools MBOX Viewer:** Para el análisis de correos electrónicos locales de Thunderbird.  
* **DB Browser for SQLite:** Para la inspección de historiales de navegación basados en bases de datos SQLite (Firefox/Opera).  
* **PowerShell:** Para la verificación de hashes criptográficos.

  ## **2.3 Análisis de Hallazgos y Evidencias**

  La investigación ha revelado un patrón claro de comportamiento desleal. El equipo, irónicamente nombrado "LADRONERA", fue utilizado activamente para negociar con la competencia.  
  El hallazgo más crítico es la **exfiltración de propiedad intelectual**. Se ha recuperado la traza completa de correos donde el usuario envía el fichero `pom.xml`, ubicado originalmente en `C:\Users\Richard\Proyectos\reverb-master\reverb-master\models\pom.xml`. Este archivo es parte de la estructura de un proyecto de software interno. La comunicación culmina con una extorsión, solicitando criptomonedas a cambio de más información alojada en la nube (Google Drive).  
  Adicionalmente, el usuario dedicó tiempo laboral a actividades de ocio (películas, apuestas) y planificación personal (viajes a Canarias), violando las políticas de uso aceptable de la empresa. La conexión de un USB Kingston el mismo día de su última conexión sugiere una posible copia local de datos antes de la exfiltración o como medio de transporte de los mismos.

  ## **2.4 Conclusiones**

  Basado en las evidencias digitales recolectadas, se concluye que:  
1. **Hubo exfiltración de datos confirmada:** Richard Warner compartió código fuente y documentación interna con terceros ajenos a la organización.  
2. **Violación de políticas de seguridad:** Se utilizaron dispositivos de almacenamiento externo no autorizados y se accedió a sitios web de riesgo/ocio en horario laboral.  
3. **Intencionalidad:** La planificación del viaje y la negociación económica (Bitcoin) demuestran que las acciones fueron premeditadas.  
   Se recomienda a InnovaTech Solutions revocar inmediatamente todas las credenciales del usuario, auditar el repositorio de código afectado y considerar acciones legales basadas en la evidencia de espionaje industrial.

   # **Anexo: Inventario de Hallazgos**.

| ID | Descripción | Ubicación (Ruta completa) | MAC Time (Fecha/Hora) | Contenido / Observaciones |
| :---- | :---- | :---- | :---- | :---- |
| **H-01** | Registro de Usuario | C:/Windows/System32/config/SAM | 22/02/2023 13:55:18 | Último login del usuario "Richard". |
| **H-02** | Registro de Sistema | C:/Windows/System32/config/SYSTEM | N/A | Hostname: "LADRONERA". |
| **H-03** | Registro USB | \\SYSTEM\\CurrentControlSet\\Enum\\STORAGE\\... | 22/02/2023 00:27:42 | Conexión USB Kingston DataTraveler 3.0. |
| **H-04** | Historial Firefox | C:/Users/Richard/AppData/Roaming/Mozilla/Firefox/Profiles/mt13hmmn.default-release/places.sqlite | Varios registros | Búsquedas: "Trabajo Basura","CuevanaHD". |
| **H-05** | Persistencia (Run) | \\Software\\Microsoft\\Windows\\CurrentVersion\\Run (en NTUSER.DAT) | N/A | Navegador Opera configurado en inicio. |
| **H-06** | Correo Thunderbird | C:\\Users\\Richard\\AppData\\Roaming\\Thunderbird\\Profiles\\tvtlv94f.default-release\\ | 22/02/2023 00:59:00 | Email con adjunto "pom.xml" enviado a competencia. |
| **H-07** | Código Fuente | C:\\Users\\Richard\\Proyectos\\reverb-master\\reverb-master\\models\\pom.xml | 22/02/2023 | Archivo XML de configuración Maven exfiltrado. |

   *(Nota: Las imágenes de evidencia correspondientes a cada hallazgo se encuentran adjuntas en la carpeta de documentación del caso)*

   