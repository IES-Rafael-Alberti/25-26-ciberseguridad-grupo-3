# Anexos Proyecto 9 — Caso Forense Digital

## Indice

- 1. [Metodologia](#metodologia)
- 2. [Herramientas Empleadas](#herramientas)
- 3. [Imagenes](#imagenes)
- 4. [Vestigios](#vestigios)
- 4.1. [vestigio 1: Transcripciones](#vestigio1)

---

<div id="metodologia"></div>

## 1. Metodologia

El proceso de investigacion se estructuro en tres fases diferenciadas:

**Adquisicion de evidencias**

Se siguieron los criterios estandar de la forensia digital para garantizar la
integridad de cada artefacto:

1. Registro exacto de la fecha y hora de cada extraccion.
2. Minimizacion de la interaccion con los dispositivos analizados para evitar
   cualquier modificacion del estado original.
3. Recogida de evidencias respetando el orden de volatilidad.
4. Documentacion exhaustiva del proceso para asegurar su reproducibilidad por
   parte de cualquier otro perito.

**Preservacion y cadena de custodia**

Para cada evidencia se registro la siguiente informacion:

- Lugar, fecha y hora de descubrimiento y recogida.
- Identidad del responsable de la recogida y de cada acceso posterior.
- Condiciones y metodo de almacenamiento. Los dispositivos moviles se conservaron
  en bolsas de Faraday para impedir cualquier comunicacion inalambrica que pudiera
  comprometer su contenido.
- En caso de traspaso de custodia: nombre del nuevo responsable, fecha y hora,
  y verificacion de hashes para confirmar que no se ha producido alteracion alguna.

**Analisis**

Todas las actuaciones analiticas se llevaron a cabo respetando los principios de
metodicidad, auditabilidad, repetibilidad y defensa en juicio de cada conclusion.


<div id="herramientas"></div>

## 2. Herramientas Empleadas

Las siguientes herramientas fueron empleadas durante el proceso de adquisicion, revision y analisis de las evidencias digitales:

| Herramienta | Version | Uso principal |
| --- | --- | --- |
| DBeaver | 26.0.4 | Apertura y consulta de bases de datos SQLite, incluyendo `babel1.db`, `settings-victima.db` y `settings_marido.db`. |
| FTK Imager | 3.1.2 | Adquisicion, montaje y verificacion de imagenes y artefactos forenses. |
| Autopsy | 1.2 | Exploracion de volumenes, sistemas de ficheros y artefactos recuperados de los dispositivos intervenidos. |
| Wireshark | 4.6.4 | Revision de capturas de red del entorno Smart Home. |
| Visual Studio Code | 15.6.2 | Lectura, documentacion y revision de archivos de texto plano, registros y documentos del informe. |

<div id="imagenes"></div>

## 3. Imagenes

Las siguientes imagenes documentan visualmente los artefactos, registros y capturas citados en el informe tecnico:

| Figura | Archivo | Descripcion |
| --- | --- | --- |
| Figura 1 | [`2026-05-13 09_34_36-DBeaver 26.0.4 - messages.png`](./img/2026-05-13%2009_34_36-DBeaver%2026.0.4%20-%20messages.png) | Conversacion entre la victima y un tercero. |
| Figura 2 | [`2026-05-13 14_24_54-DBeaver 26.0.4 - conversations.png`](./img/2026-05-13%2014_24_54-DBeaver%2026.0.4%20-%20conversations.png) | Nombre del usuario con el que la victima mantuvo la conversacion encontrada y ultimo mensaje. |
| Figura 3 | [`2026-05-13 14_27_19-DBeaver 26.0.4 - participants.png`](./img/2026-05-13%2014_27_19-DBeaver%2026.0.4%20-%20participants.png) | Nombre de la victima y nombre del segundo usuario, junto a sus GAIA ID. |
| Figura 4 | [`2026-05-14 12_15_16-mili_log.txt_ Bloc de notas.png`](./img/2026-05-14%2012_15_16-mili_log.txt_%20Bloc%20de%20notas.png) | Registro de actividad de la pulsera `mili_log.txt`. |
| Figura 5 | [`2026-05-13 10_52_08-.png`](./img/2026-05-13%2010_52_08-.png) | Captura de pantalla `cf092f21.jpg` encontrada en la television inteligente. |
| Figura 6 | [`timezone.png`](./img/timezone.png) | Archivo de zona horaria de la television. |
| Figura 7 | [`kodi-log.png`](./img/kodi-log.png) | Registro `kodi.log` localizado en la Raspberry Pi usada como Smart TV. |
| Figura 8 | [`2026-05-14 12_44_49-Alexa - Explorador de archivos.png`](./img/2026-05-14%2012_44_49-Alexa%20-%20Explorador%20de%20archivos.png) | Registro de Alexa donde se muestra la orden de poner la estacion de radio Pandora. |
| Figura 9 | [`2026-05-14 12_57_24-Alexa - Explorador de archivos.png`](./img/2026-05-14%2012_57_24-Alexa%20-%20Explorador%20de%20archivos.png) | Transcripcion de comando de voz detectado e interpretado incorrectamente por Alexa. |
| Figura 10 | [`2026-05-14 13_25_09-Alexa - Explorador de archivos.png`](./img/2026-05-14%2013_25_09-Alexa%20-%20Explorador%20de%20archivos.png) | Transcripcion del ultimo registro. |
| Figura 11 | [`2026-05-14 18_43_24-DBeaver 26.0.4 - system.png`](./img/2026-05-14%2018_43_24-DBeaver%2026.0.4%20-%20system.png) | Nombre del dispositivo de la victima con identificador. |
| Figura 12 | [`2026-05-14 18_45_43-NVIDIA GeForce Overlay.png`](./img/2026-05-14%2018_45_43-NVIDIA%20GeForce%20Overlay.png) | Direccion Bluetooth del dispositivo de la victima. |
| Figura 13 | [`2026-05-14 19_14_26-.png`](./img/2026-05-14%2019_14_26-.png) | Nombre del dispositivo del marido de la victima. |
| Figura 14 | [`2026-05-14 19_15_17-.png`](./img/2026-05-14%2019_15_17-.png) | Direccion Bluetooth del dispositivo del marido de la victima. |
| Figura 15 | [`2026-05-14 19_40_33-Parsec.png`](./img/2026-05-14%2019_40_33-Parsec.png) | Direccion Bluetooth de la television. |
| Figura 16 | [`2026-05-14 19_50_13-Parsec.png`](./img/2026-05-14%2019_50_13-Parsec.png) | Registro de deteccion del dispositivo Echo. |
| Figura 17 | [`2026-05-14 19_56_08-Parsec.png`](./img/2026-05-14%2019_56_08-Parsec.png) | Registro de deteccion de dispositivo `mi1a`. |
| Figura 18 | [`2026-05-14 19_51_57-Parsec.png`](./img/2026-05-14%2019_51_57-Parsec.png) | Busqueda realizada sobre el dispositivo detectado. |

<div id="vestigios"></div>

## 4. Vestigios

<div id="vestigio1"></div>

## 4.1 Vestigio 1: Transcripcion de audios de echo

| Archivo / fuente                         | Fecha UTC+9 | Hora UTC+9   | Texto registrado                                                     | Observación forense                                                                                              |
| ---------------------------------------- | ----------- | ------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 11.json 11.json                          | 2017-07-17  | 15:01:55.220 | turn on tv 11.json                                                   | Orden clara de encendido de TV. 11.json                                                                          |
| 10.json 10.json                          | 2017-07-17  | 15:06:03.907 | alexa 10.json                                                        | Activación previa a otra orden. 10.json                                                                          |
| 9.json 9.json                            | 2017-07-17  | 15:06:06.327 | turn on pandora 9.json                                               | Inicio de reproducción de Pandora. 9.json                                                                        |
| 8.json 8.json                            | 2017-07-17  | 15:12:39.818 | alexa how could you do this what are the flooding 8.json             | JSON conserva frase larga; Alexa solo interpretó formalmente What are the flooding?. 8.json                      |
| Historial visual aportado por el usuario | 2017-07-17  | 15:12 aprox. | alexa what do this to me stop we said we would what are you thinking | Posible evento adicional no integrado aún en la tanda de JSON ya revisada; conviene localizar su archivo exacto. |
| 6.json 6.json                            | 2017-07-17  | 15:12:58.358 | alexa 6.json                                                         | Nueva activación pocos segundos después. 6.json                                                                  |
| 5.json 5.json                            | 2017-07-17  | 15:13:02.196 | stop 5.json                                                          | Orden de detener reproducción o acción en curso. 5.json                                                          |
| 4.json 4.json                            | 2017-07-17  | 15:20:05.858 | alexa 4.json                                                         | Activación previa. 4.json                                                                                        |
| 3.json 3.json                            | 2017-07-17  | 15:20:07.632 | turn off tv 3.json                                                   | Orden clara de apagado de TV. 3.json                                                                             |
| 2.json 2.json                            | 2017-07-17  | 15:20:32.631 | alexa 2.json                                                         | Activación previa. 2.json                                                                                        |
| 1.json 1.json                            | 2017-07-17  | 15:20:34.384 | who yes, interpretado como Who is Yes? 1.json                        | Consulta de conocimiento, no domótica. 1.json                                                                    |
