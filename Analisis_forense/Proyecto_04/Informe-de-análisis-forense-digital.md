# **Informe de análisis forense digital**

## Caso: amenaza de bomba en centro educativo Equipo analizado: DESKTOP-01S7HH9

# **Integrantes**

[Abel García Domínguez](mailto:agardom573@g.educaand.es)  
[David Jiménez Ruiz](mailto:djimrui878@g.educaand.es)  
Jose Mª Escalón Prada  
[Daniel Hernández Gómez](mailto:dhergom961@g.educaand.es)

# **Introducción**

Este informe documenta el análisis forense de un volcado de memoria RAM del ordenador personal de un alumno identificado como Francisco José Jiménez, alias “Pacopepe”, en el contexto de una investigación por una falsa amenaza de bomba realizada contra un centro educativo. El objetivo principal es determinar si el equipo analizado pertenece al sospechoso y si en la memoria del sistema existen indicios que lo vinculen con la llamada amenazante.

# **Fundamentación teórica**

El análisis forense de memoria (memory forensics) permite extraer artefactos digitales directamente desde la RAM, como procesos en ejecución, variables de entorno, conexiones de red, handles de archivos y fragmentos de comunicaciones, que reflejan el estado dinámico del sistema en un momento concreto.   
Esta aproximación resulta especialmente útil en incidentes donde el usuario puede haber borrado archivos o limpiado rastros en disco, pero parte de la actividad sigue residente en memoria.

Herramientas como Volatility 3 y Volatility 2 permiten interpretar el volcado de memoria, reconstruir la lista de procesos y sus relaciones, identificar módulos cargados y recorrer el espacio de direcciones para localizar cadenas de texto relevantes, entre otros artefactos. 

En combinación con utilidades de cálculo de hashes, es posible además garantizar la integridad de la evidencia mediante la comparación entre los valores hash proporcionados en la adquisición y los calculados localmente.

# **Objetivos del análisis**

Los objetivos específicos fijados para este análisis son los siguientes:

* Confirmar que la imagen de memoria pertenece al ordenador del alumno, identificado como DESKTOP-01S7HH9.  
* Determinar el PID del proceso de la aplicación utilizada para visualizar documentos PDF y establecer cuál es su proceso padre.

* Identificar, a través de los manejadores de archivos, qué documento estaba siendo editado o abierto por el alumno durante la intervención policial.

* Buscar en el volcado de memoria pruebas que vinculen al usuario del equipo con la realización de la falsa amenaza de bomba, tanto de forma directa (confesión explícita) como indirecta (planificación, comentarios, búsquedas, etc.).

# **Adquisición de la evidencia e integridad**

## **Descripción de la evidencia**

Se ha proporcionado una imagen de memoria del equipo del sospechoso con la siguiente denominación:

*DESKTOP-01S7HH9-20220408-171552.dmp*

Junto a la imagen principal se han facilitado un archivo de log generado por DumpIt en formato JSON y un archivo de hashes para verificar la integridad tanto del volcado como de su archivo comprimido y el archivo de dumpit. Estos ficheros sirven como referencia para comprobar que la evidencia no ha sido alterada desde su adquisición, y que se ha mantenido la cadena de custodia.

## **Verificación de integridad (SHA-256)**

Se calcularon los hashes SHA-256 de los siguientes ficheros y se compararon con los valores proporcionados:

***DESKTOP-01S7HH9-20220408-171552.dmp***  
Hash proporcionado: edcdbcac27263a45d6dfe27f6c8baff55952b2357a70031de20de057730cd359  
Hash calculado: EDCDBCAC27263A45D6DFE27F6C8BAFF55952B2357A70031DE20DE057730CD359  
Resultado: coincidencia (integridad verificada).

***DESKTOP-01S7HH9-20220408-171552.json***  
Hash proporcionado: cbcd0ac591b4fc425550eb1292ad8f1dddc4b0146a6d0df7b23f6d13fa84b049  
Hash calculado: CBCD0AC591B4FC425550EB1292AD8F1DDDC4B0146A6D0DF7B23F6D13FA84B049  
Resultado: coincidencia (integridad verificada).

***DESKTOP-01S7HH9-20220408-171552.dmp.zip***  
Hash proporcionado: 2246b2abb178b3a508b5c8207d50e7e6f86d5c1f09487b50daaa6387bef639f0  
Hash calculado: 2246B2ABB178B3A508B5C8207D50E7E6F86D5C1F09487B50DAAA6387BEF639F0  
Resultado: coincidencia (integridad verificada).

La coincidencia exacta entre los hashes calculados y los proporcionados confirma que la imagen de memoria y los archivos asociados no han sido modificados desde su captura y que la cadena de custodia ha sido respetada.

# **Metodología de análisis**

## **Herramientas empleadas**

Para el análisis de la memoria se utilizaron:

Volatility 3, marco de análisis de memoria en Python orientado a la extracción de artefactos desde imágenes de RAM.  
Volatility 2, en particular para el uso de ciertos plugins y la generación de un espacio de direcciones raw compatible con herramientas externas de strings.  
Utilidades de sistema (strings y findstr) para la extracción y búsqueda de cadenas de texto en el volcado de memoria convertido.

## **Procedimiento general**

1. Verificación de integridad de la imagen de memoria y ficheros asociados mediante SHA-256.  
2. Carga de la imagen en Volatility 3 y obtención de información básica del sistema, incluyendo variables de entorno para confirmar el nombre del equipo.  
3. Enumeración de procesos y árbol de procesos para localizar la aplicación relacionada con la visualización de documentos PDF.  
4. Uso del plugin de manejadores (handles) para identificar archivos abiertos en el momento de la captura, con especial atención a documentos de trabajo del usuario.  
5. Conversión de la imagen al formato raw (.dd) con Volatility 2 y generación de un archivo de cadenas (strings.txt) a partir de dicho volcado.  
6. Búsqueda de términos relacionados con la amenaza (“bomba”, etc.) dentro del archivo de cadenas para localizar fragmentos de conversaciones o textos relevantes.

# **Resultados del análisis**

1. ## **Confirmación de la propiedad del equipo DESKTOP-01S7HH9**

Para confirmar que la imagen de memoria corresponde al equipo del alumno identificado como DESKTOP-01S7HH9 se utilizó Volatility 3 junto con el plugin orientado a mostrar las variables de entorno del sistema (Envar). Este plugin permite visualizar información como el nombre del equipo, el nombre de usuario y otras variables del entorno de ejecución de Windows.  
En la salida del análisis se observa que el valor de la variable correspondiente al nombre del equipo coincide con “DESKTOP-01S7HH9”, lo que confirma que el volcado de memoria pertenece al dispositivo asignado al alumno investigado. Esta coincidencia satisface el primer objetivo planteado, estableciendo la vinculación entre la imagen analizada y el equipo sospechoso.

2. ## **Identificación del proceso de visualización PDF**

Mediante el análisis de la lista de procesos en ejecución y su árbol de relaciones con Volatility (plugin pstree), se identificó la presencia de un proceso denominado AcroCEF.exe. AcroCEF.exe es un componente asociado a Adobe Acrobat/Adobe Reader que se encarga de funcionalidades como la renderización basada en Chromium, la conversión web‑to‑PDF y la integración con servicios en la nube.  
Aunque AcroCEF.exe no es el proceso principal de la interfaz del lector de PDF, su ejecución en el árbol de procesos indica que Adobe Acrobat o Adobe Reader estaban activos en el momento del volcado. A partir del pstree se obtuvo el PID de dicho proceso y se observó que su proceso padre corresponde al proceso principal de Adobe, lo que confirma la actividad de la aplicación de lectura/gestión de PDF durante la intervención.

3. ## **Documento en edición durante la intervención policial**

Para determinar qué documento estaba siendo editado o al menos abierto en el momento de la captura, se empleó el plugin handles de Volatility, que lista los manejadores de objetos (archivos, claves de registro, etc.) asociados a cada proceso. Este análisis permite identificar qué ficheros estaban siendo accedidos por procesos concretos en el instante en que se realizó el volcado.  
El examen de los manejadores de archivos mostró que el documento “Trabajo historia Pacopepe.odt” se encontraba abierto, asociado a un proceso de edición u ofimática. Además, el análisis de los manejadores y rutas indicó la existencia de un flujo de trabajo en el que un archivo .odt original se convertía a PDF, lo que sugiere que el usuario había descargado o utilizado una herramienta de conversión para transformar el documento de texto a formato PDF.  
Estos indicios permiten concluir que, durante la intervención policial, el alumno estaba trabajando con el documento “Trabajo historia Pacopepe.odt”, ya fuera editándolo directamente o manteniéndolo abierto mientras se generaba o visualizaba su versión en PDF.

4. ## **Evidencia relativa a la amenaza de bomba**

Para localizar evidencias que vincularan al usuario con la falsa amenaza de bomba fue necesario extraer cadenas de texto legibles desde el contenido de la memoria. Algunos plugins de Volatility 2 requieren trabajar sobre un espacio de direcciones en formato raw, por lo que se procedió a convertir el volcado original .dmp a un archivo .dd mediante el comando imagecopy de Volatility 2\.  
Una vez generado el archivo pacopepe\_dd\_dump.dd, se utilizó la herramienta strings para extraer todas las cadenas de caracteres legibles del volcado, redirigiendo la salida a un archivo de texto (strings.txt). Posteriormente, se empleó findstr con búsqueda insensible a mayúsculas para localizar apariciones de la palabra “bomba” en dicho archivo.  
En el contenido recuperado se identificó un fragmento de conversación en Discord entre el usuario “pakopepe88” y otro interlocutor, donde se hablaba específicamente de la amenaza de bomba. En este intercambio, “pakopepe88” reconoce explícitamente haber sido el autor de la amenaza falsa, constituyendo una confesión directa. Este hallazgo representa una evidencia clara que relaciona al usuario del equipo con la acción investigada, tanto por el alias utilizado (coherente con el apodo del sospechoso) como por el contenido incriminatorio del mensaje.

# **Presentación de los hallazgos principales**

**Nombre del equipo**  
Ruta/localización: Variable de entorno del sistema obtenida mediante plugin Windows.envar.Envar en Volatility 3\.  
Contenido relevante: Valor de la variable de nombre de equipo: “DESKTOP-01S7HH9”.

**Proceso AcroCEF.exe (componente de Adobe Acrobat/Reader)**  
Ruta/localización: Listado de procesos y pstree de Volatility, entrada correspondiente a AcroCEF.exe con su PID y PPID.  
Contenido relevante: Proceso asociado a la funcionalidad de Adobe Acrobat; indica que un lector/gestor de PDF se encontraba en ejecución.

**Documento “Trabajo historia Pacopepe.odt”**  
Ruta/localización: Manejadores de archivos (handles) asociados a procesos de ofimática, identificando un handle abierto hacia el fichero “Trabajo historia Pacopepe.odt”.  
Contenido relevante: Documento de trabajo del alumno, presumiblemente de la asignatura de Historia, abierto en el momento de la captura; evidencia adicional de la actividad legítima en el equipo en el instante de la intervención.

**Fragmento de conversación en Discord (usuario “pakopepe88”)**  
Ruta/localización: Cadenas de texto en memoria extraídas desde pacopepe\_dd\_dump.dd y filtradas en strings.txt mediante búsqueda de la palabra “bomba”.  
Contenido relevante: Conversación en la que el usuario “pakopepe88” admite ser el autor de la falsa amenaza de bomba, describiendo o reconociendo la acción.

# **Conclusiones**

A partir del análisis realizado sobre la imagen de memoria del equipo DESKTOP-01S7HH9 pueden extraerse las siguientes conclusiones:

La verificación mediante hashes SHA-256 confirma que la imagen de memoria y los archivos asociados no han sido modificados desde su adquisición, por lo que la evidencia analizada es íntegra y fiable.

Volatility 3 que el volcado pertenece al equipo denominado “DESKTOP-01S7HH9”, atribuible al alumno investigado. El árbol de procesos muestra que un componente de Adobe Acrobat/Reader (AcroCEF.exe) se encontraba en ejecución, lo que indica que en el momento de la captura el usuario utilizaba o tenía abierto algún documento en formato PDF. El análisis de manejadores revela que el documento “Trabajo historia Pacopepe.odt” estaba abierto y probablemente en edición durante la intervención policial, lo que sitúa al alumno utilizando su equipo para tareas académicas en ese momento.  
La extracción y búsqueda de cadenas de texto en la imagen de memoria permitió localizar una conversación en Discord donde el usuario “pakopepe88” reconoce explícitamente ser el autor de la falsa amenaza de bomba, aportando una evidencia directa que vincula al usuario del equipo con el incidente.

En conjunto, los hallazgos técnicos respaldan la hipótesis de que el volcado de memoria corresponde efectivamente al ordenador de Pacopepe y que, además de la actividad académica legítima, el mismo equipo fue utilizado para comunicaciones en las que el propio usuario admite haber realizado la amenaza de bomba falsa. Desde el punto de vista forense, la conversación localizada en Discord constituye la prueba más sólida que relaciona al sospechoso con la conducta investigada.

