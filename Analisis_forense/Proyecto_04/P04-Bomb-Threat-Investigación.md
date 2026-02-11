# **Investigación del incidente**

## P04. Bomb Threat, Análisis Forense

# 

# **Integrantes (en orden de longitud de su miembro viril)**

[Abel García Domínguez](mailto:agardom573@g.educaand.es)  
[David Jiménez Ruiz](mailto:djimrui878@g.educaand.es)  
Jose Mª Escalón Prada  
[Daniel Hernández Gómez](mailto:dhergom961@g.educaand.es)

# **Comprobación de Integridad (sha-256)**


<img width="1460" height="175" alt="Captura de pantalla 2026-02-11 125207" src="https://github.com/user-attachments/assets/42347449-2eaf-430b-841d-c60acfb428a6" />

**DESKTOP-01S7HH9-20220408-171552.dmp**  
Hash proporcionado: edcdbcac27263a45d6dfe27f6c8baff55952b2357a70031de20de057730cd359  
Hash calculado: EDCDBCAC27263A45D6DFE27F6C8BAFF55952B2357A70031DE20DE057730CD359  
**RESULTADO: COINCIDENCIA**  

<img width="1919" height="164" alt="Captura de pantalla 2026-02-11 132124" src="https://github.com/user-attachments/assets/dc6b4d46-6017-4a55-95c8-558ab844ff64" />


**DESKTOP-01S7HH9-20220408-171552.json**  
Hash proporcionado: cbcd0ac591b4fc425550eb1292ad8f1dddc4b0146a6d0df7b23f6d13fa84b049  
Hash calculado: CBCD0AC591B4FC425550EB1292AD8F1DDDC4B0146A6D0DF7B23F6D13FA84B049  
**RESULTADO: COINCIDENCIA**  

<img width="1919" height="190" alt="Captura de pantalla 2026-02-11 132116" src="https://github.com/user-attachments/assets/034625ed-9477-494d-8fde-f90c38f89abf" />


**DESKTOP-01S7HH9-20220408-171552.dmp.zip**  
Hash proporcionado: 2246b2abb178b3a508b5c8207d50e7e6f86d5c1f09487b50daaa6387bef639f0  
Hash calculado:  2246B2ABB178B3A508B5C8207D50E7E6F86D5C1F09487B50DAAA6387BEF639F0  
**RESULTADO: COINCIDENCIA**

1. # **Confirmación de propiedad del equipo DESKTOP-01S7HH9**

Para verificar que la imagen de memoria corresponde al ordenador del alumno identificado como DESKTOP-01S7HH9, utilizamos volatility 3 con Envar. Esta herramienta nos muestra todas las variables de entorno.

<img width="924" height="148" alt="image" src="https://github.com/user-attachments/assets/abdeea38-4200-435d-b7fe-34ef4fa83d2b" />

El nombre del equipo mostrado coincide con el dispositivo del alumno.

2. # **Identificación del proceso de visualización PDF**

Durante el análisis de procesos activos encontré AcroCEF.exe, un componente de Adobe Acrobat que maneja funcionalidades como conversión web-to-PDF y sincronización con servicios en la nube. Aunque no es directamente el lector de PDF, su presencia confirma que Adobe Acrobat o Reader estaba instalado y probablemente activo en el momento de la captura.

3. # **Documento en edición durante la intervención policial**

El análisis de la MFT reveló que el PDF localizado provenía de un archivo .odt original. Encontré evidencia de descarga y uso de una herramienta de conversión, lo que indica que el usuario transformó el documento original a formato PDF.

Mediante el plugin handles de Volatility identifiqué que el documento "Trabajo historia Pacopepe.odt" estaba abierto y posiblemente en edición. Este plugin lista los manejadores de objetos del sistema utilizados por procesos específicos, confirmando que el archivo estaba siendo accedido en el momento de la captura de memoria.

4. # **Evidencia de la amenaza de bomba**

Para buscar pruebas que vinculen al usuario con la falsa amenaza, primero convertí el volcado de memoria a formato raw, ya que el plugin strings de Volatility requiere un espacio de direcciones raw:

[vol.py](http://vol.py) \-f DESKTOP-01S7HH9-20220408-171552.dmp \--profile=Win10x64\_19041 imagecopy \-O raw\_memory.dd

Después generé un archivo de strings desde el volcado raw:

strings raw\_memory.dd \> strings.txt

Busqué la palabra clave "bomba" en el archivo de strings:

grep bomba strings.txt

El análisis reveló una conversación en Discord entre pakopepe88 y marcosheredia666. En esta conversación pakopepe88 admite ser el autor de la amenaza de bomba falsa. Esta evidencia directa vincula al usuario del equipo con el incidente investigado.

