# **Proyecto 3: Unfaithful Employee**

## **Informe de Análisis Forense**

**Analistas:** Jose M\!ª Escalón Prada, Daniel Hernández Gómez, Abel García Dominguez, David Jimenez.  
**Fecha:** 02 de febrero de 2026  
**Caso:** Investigación interna de la empresa InnovaTech Solutions  
**Sujeto:** Richard Eduardo Warner

# **1\. Investigación del Incidente**

A continuación, se presentan las respuestas a las cuestiones planteadas en la fase de investigación, basadas en el análisis de la imagen forense del disco duro del empleado. Hemos utilizado tanto Autopsy como Windows Resgistry Recovery para mejor acceso a la información.

## **1.1 Verificación de Integridad de la Imagen**

Se ha procedido a la verificación de la integridad de la evidencia digital comparando los hashes de la imagen adquirida con los proporcionados originalmente por el departamento de sistemas (Alan).

### **Hashes Proporcionados (Cadena de Custodia):**

* **MD5:** dfdfba2231e3fa409676b1b737474208  
* **SHA-1:** f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c  
* **SHA-256:** 66d6ee7a61ea7a986e8f6bb54b9986f79d95b5a0278bef86678ed42ace320d96
### **Hashes Calculados (Evidencia Analizada):**  
* **MD5:** DFDFBA2231E3FA409676B1B737474288
  <img width="1449" height="145" alt="Captura de pantalla 2026-02-03 131224" src="https://github.com/user-attachments/assets/6f5b7c2a-12af-42a0-8f8e-6190fe61774f" />
* **SHA-1:** F476A81089A10F9D5393AA8C2F8BBCCDB87F7D3C
  <img width="1348" height="151" alt="Captura de pantalla 2026-02-03 131536" src="https://github.com/user-attachments/assets/abeccffa-f09d-40a6-880e-d420bdde861a" />
* **SHA-256:** 66D6EE7A61EA7A986E8F6BB54B9986F79D95B5A0278BEF86678ED42ACE320D9B
<img width="1364" height="163" alt="Captura de pantalla 2026-02-03 131758" src="https://github.com/user-attachments/assets/5888a41d-40eb-45f2-80cc-6887c4c4eb1b" />

  **Conclusión:** Existen discrepancias en los valores MD5 y SHA-256. Aunque el SHA-1 coincide, la integridad de la imagen podría estar comprometida o haber errores en la documentación inicial de los hashes. Se procede con el análisis, documentando esta anomalía.

  ## **1.2 Identificación de Usuario y Última Conexión**

  Mediante el análisis del registro SAM (C:/Windows/System32/config/SAM/) utilizando la herramienta **Windows Registry Recovery (WRR)**, se confirma la existencia de la cuenta de usuario asociada al empleado.
  <img width="870" height="263" alt="image" src="https://github.com/user-attachments/assets/d26c1da7-1229-429e-b2e3-3fd680b2c6f6" />

* **Usuario:** Richard  
* **Último inicio de sesión:** 22 de febrero de 2023 a las 13:55:18 (UTC/Local).

  ## **1.3 Información del Sistema**

  <img width="1919" height="494" alt="image" src="https://github.com/user-attachments/assets/e6f57c9c-2bcb-4581-97d1-491dedcb9216" />


  El análisis de los registros SYSTEM y SOFTWARE ha revelado la siguiente configuración del equipo:  
* **Nombre del Equipo (Hostname):** LADRONERA  
* **Sistema Operativo:** Windows 10 Pro Education N  


  ## **1.4 Uso de Dispositivos USB**

  A pesar de las políticas corporativas, se ha detectado la conexión de un dispositivo de almacenamiento externo usando Windows Registry Recovery.

  <img width="1628" height="783" alt="image" src="https://github.com/user-attachments/assets/dfadf7a7-812a-4849-93a5-d3c76dfbc114" />


* **Dispositivo:** Kingston DataTraveler 3.0 USB Device  
* **Primera conexión registrada:** 22 de febrero de 2023 a las 00:27:42.  
  * *Evidencia:* Clave de registro \\SYSTEM\\CurrentControlSet\\Enum\\STORAGE\\... analizada con **Windows Registry Recovery**.

  ## **1.5 Actividad en Línea (Navegación Web)**

  El análisis del historial de navegación (Firefox y Opera) muestra un uso indebido de los recursos de la empresa con fines de ocio y personales:

  * **Streaming y Cine:** Búsquedas relacionadas con la película "Trabajo Basura" y acceso a la plataforma "CUEVANAHD" y "CINE24H".  
  <img width="1288" height="211" alt="image" src="https://github.com/user-attachments/assets/d18ea6e3-b9e6-41eb-a581-f913916e4b19" />
  * **Compras** Navegación en amazon y otras tiendas.  
  <img width="1226" height="140" alt="image" src="https://github.com/user-attachments/assets/a20b3dff-e2da-4d60-9e4c-8c11b1686dbd" />
  * **Apuestas:** Acceso a la plataforma de trading y apuestas eToro.  
  <img width="1176" height="201" alt="image" src="https://github.com/user-attachments/assets/3925915d-7f35-4bfd-aee6-31bd84302c7f" />
  * **Música:**Búsqueda de canciones de los grupos AC/DC y Aerosmith
  <img width="1204" height="418" alt="image" src="https://github.com/user-attachments/assets/4026ddc3-8334-42b8-ab68-06a882beb116" />
  <img width="1298" height="268" alt="image" src="https://github.com/user-attachments/assets/13fcba0b-40d2-4653-8cda-9b6f92151b4f" />
  * **Deportes:** Búsquedas recurrentes de noticias deportivas en el navegador Opera.
  <img width="1294" height="364" alt="image" src="https://github.com/user-attachments/assets/05f42c0c-bf0d-4670-8acc-6e7a9cab8cf3" />


  ## **1.6 Planes de Viaje y Movilidad**

  Se ha identificado actividad reciente relacionada con la planificación de un viaje tras su salida de la empresa:  
* **Vuelos:** Búsquedas de vuelos a Gran Canaria en el portal Vueling.
* **Alojamiento:** Búsqueda activa de hoteles en "Las Palmas de Gran Canaria" a través de Booking.com.
  <img width="1308" height="368" alt="image" src="https://github.com/user-attachments/assets/2d491a67-b1a7-44f5-be24-b1b049d8dd2e" />


  ## **1.7 Software no Autorizado al Inicio**

 <img width="1919" height="494" alt="image" src="https://github.com/user-attachments/assets/e6f57c9c-2bcb-4581-97d1-491deewb9216" />
  Se ha verificado la persistencia de aplicaciones en el inicio del sistema mediante el análisis del fichero NTUSER.DAT del usuario Richard (\\Software\\Microsoft\\Windows\\CurrentVersion\\Run).  
* **Hallazgo:** El navegador **Opera** está configurado para ejecutarse automáticamente al iniciar sesión.  
* **Otros navegadores:** Se detectó la instalación de Mozilla Firefox (ruta ROOT\\Mozilla\\Mozilla Firefox en registro SOFTWARE), pero no está configurado en el inicio automático.

  ## **1.8 Exfiltración de Información**

  El análisis de los mensajes de correo electrínico confirma la filtración de datos confidenciales.
  <img width="1665" height="526" alt="image" src="https://github.com/user-attachments/assets/4fdb9761-9f13-427f-9764-b050afaf0c80" />

  <img width="1591" height="723" alt="image" src="https://github.com/user-attachments/assets/fdcdc324-2a46-4698-8b69-33ce2e2dde67" />

 
* **Interlocutor:** `proba2.seguridade@gmail.com` (Competencia).  
* **Remitente:** `proba1.seguridade@gmail.com` (Richard).  
* **Hechos:**  
  1. Richard solicita un aumento salarial a la competencia.  
  2. Envía como "prueba" un archivo confidencial **pom.xml** (perteneciente al proyecto *reverb-master*) el 22/02/2023.  
  3. Posteriormente, envía un enlace a Google Drive protegido con contraseña, exigiendo un pago en Bitcoin para liberar el acceso completo al material exfiltrado.

   
