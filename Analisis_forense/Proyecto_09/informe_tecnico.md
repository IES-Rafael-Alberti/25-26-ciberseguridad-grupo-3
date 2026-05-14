# Informe técnico: Proyecto 9. Caso de homicidio.

## Índice

1. [Juramento y declaración de abstención y tacha](#1-juramento-y-declaración-de-abstención-y-tacha)
2. [Palabras clave](#2-palabras-clave)
3. [Índice de figuras](#3-índice-de-figuras)
4. [Resumen ejecutivo](#4-resumen-ejecutivo)
5. [Introducción](#5-introducción)
   - 5.1 [Antecedentes](#51-antecedentes)
   - 5.2 [Objetivos](#52-objetivos)
   - 5.3 [Alcance](#53-alcance)
6. [Fuentes de información](#6-fuentes-de-información)
   - 6.1 [Adquisición de evidencias](#61-adquisición-de-evidencias)
7. [Análisis](#7-análisis)
   - 7.1 [Herramientas utilizadas](#71-herramientas-utilizadas)
   - 7.2 [Procesos](#72-procesos)
     - 7.2.1 [Verificación de integridad](#721-verificación-de-integridad)
     - 7.2.2 [Análisis de conversaciones WhatsApp](#722-análisis-de-conversaciones-whatsapp)
     - 7.2.3 [Análisis de actividad en Telegram](#723-análisis-de-actividad-en-telegram)
     - 7.2.4 [Análisis del historial de búsquedas de Atalus](#724-análisis-del-historial-de-búsquedas-de-atalus)
     - 7.2.5 [Análisis de grabaciones cámara IP](#725-análisis-de-grabaciones-cámara-ip)
     - 7.2.6 [Análisis de accesos a Instagram de Lassandra](#726-análisis-de-accesos-a-instagram-de-lassandra)
     - 7.2.7 [Análisis del correo electrónico de la víctima](#727-análisis-del-correo-electrónico-de-la-víctima)
8. [Limitaciones](#8-limitaciones)
9. [Conclusiones](#9-conclusiones)
10. [Anexo 1. Sobre el perito](#10-anexo-1-sobre-el-perito)
11. [Anexo 2. Sumas de verificación](#11-anexo-2-sumas-de-verificación)


# 1. Juramento y Declaración de Abstención y Tacha

El/la abajo firmante, en calidad de perito/a informático/a, jura o promete solemnemente haber procedido y proceder con la mayor objetividad posible, tomando en consideración tanto lo que pueda favorecer como lo que sea susceptible de causar perjuicio a cualquiera de las partes, y que conoce las sanciones penales en las que podría incurrir si incumpliere su deber como perito/a.

Asimismo, declara no encontrarse incurso/a en ninguna de las causas de abstención o tacha previstas en la legislación vigente en relación con las partes implicadas en el presente procedimiento, y que no existe ningún vínculo personal, profesional ni económico que pueda comprometer su imparcialidad en la emisión del presente dictamen.


## 2. Palabras clave

- **IOT**: Del inglés "Internet Of Things" o "internet de las cosas", se trata de los dispositivos inteligentes como televisiones, asistentes de voz, etc.
- **Echo**: Se refiere en este contexto al asistende de voz de Amazon. Se activa el dispositivo al decir la palabra "Alexa".
- **Hangouts**: Aplicación de mensajería de google. Asociada al id universal de google (GAIA ID)
- **GAIA ID**: ID único que idenfitica a una cuenta de google. Se asocian a él el nombre del usuario, reviews, etc.

## 3. Índice de figuras

(Figura 1) Conversación entre la víctima y un tercero.

## 4. Resumen ejecutivo

El análisis de los teléfonos, router y dispositivos IOT indican que el testomonio del marido de la víctima es cierto, y revelan indicios de la autoría de los hechos. Mensajes de texto de la aplicación hangouts sugieren un enfrentamiento verbal entre la víctima y un tercero. Posteriormente, el día de los hechos, el dispositivo de voz "Echo" graba un altercado entre dos personas, una de ellas la víctima, sin confirmarse la identidad de la otra. Las declaraciones del marido acerca de la situación antes del incidente se confirma mediante capturas de pantalla y registros de la televisión inteligente, así como por los registros de voz del dispositivo "Echo" que concuerdan con el marco de tiempo definido.


## 5. Introducción

### 5.1 Antecedentes
El presente análisis forense digital trae causa del homicidio de una mujer en su domicilio, ocurrido el 17 de julio de 2017 y comunicado a los servicios de emergencia por el conserje del edificio tras ser alertado por el marido de la víctima. Según la información inicial de la investigación, la policía recibió la llamada a las 15:31, llegó al lugar a las 15:40 y los servicios medicos confirmaron que la víctima se encontraba sin signos vitales en el salón de la vivienda, presentando lesiones compatibles con múltiples puñaladas.

En el momento de la intervención policial se encontraban en la escena el conserje y el marido de la víctima, quien manifestó que ambos habían regresado al domicilio alrededor de las 15:00 en zona horaria UTC+9 y que él permaneció en el dormitorio viendo una película con auriculares puestos, debido a que su mujer tenía puesta música, y fue por este motivo que afirmó no haber escuchado lo que pasaba en el salón. El marido permitió el acceso a los dispositivos presentes en la vivienda.

Dado que la vivienda disponía de varios dispositivos IOT, se ha realizado un análisis forense orientado a dispositivos móviles e IoT.

### 5.2 Objetivos
- Documentar y reconstruir cronológicamente los hechos ocurridos en la vivienda el 17 de julio de 2017, tomando como referencia la zona horaria UTC+9.

- Identificar y analizar los dispositivos digitales relevantes presentes en la escena, preservando la integridad de las evidencias durante todo el proceso.

- Determinar la actividad registrada en los dispositivos móviles, IoT, router, red doméstica y servicios cloud vinculados al ecosistema Smart Home de la vivienda.

- Contrastar la declaración del marido con las evidencias técnicas extraídas de la Raspberry Pi empleada como SmartTV, Amazon Echo, Google OnHub, SmartThings, smartphones y resto de artefactos intervenidos.

- Establecer relaciones temporales entre los eventos detectados en las distintas fuentes de evidencia.

- Evaluar, a partir de todo ello, la posibilidad de las hipótesis principales, en particular si el autor de los hechos fue el marido de la víctima o un tercero desconocido.

### 5.3 Alcance
El análisis comprende las fuentes de evidencia digital aseguradas y facilitadas por la policía científica en el marco del caso, incluyendo el smartphone de la víctima, el smartphone del marido, la televisión inteligente, el informe de diagnóstico del router Google OnHub, los datos de Amazon Echo y el volcado de tráfico de red del entorno Smart Home.

Este análisis se limita a las evidencias entregadas oficialmente y a los artefactos que puedan derivarse de ellas, sin extenderse a fuentes externas no incluidas en la adquisición ni a especulación carente de soporte técnico demostrable.

## 6. Fuentes de información.

Se realizaron extracciones de las siguientes fuentes:

- El smartphone de la víctima.

- El smartphone del marido de la víctima, sincronizado con la App Samsung SmartThings.

- Raspberry Pi (TV Inteligente).

- Informe de diagnóstico de Google OnHub.

- Datos de Amazon Echo Alexa.

- Tráfico de red del SmartHome.

- Hashes de la adquisición.

Se muestran las sumas de verificación y los comandos utilizados en el [Anexo 2](#102-anexo-2-sumas-de-verificación)

## 7. Análisis

### 7.1 Herramientas utilizadas

| Herramienta | Version | Uso |
| --- | --- | --- |
| DBeaver | 26.0.4 | Visualización de bases de datos |
| FTK Imager | 3.1.2 | Adquisicion y verificacion de imagenes forenses |
| Autopsy | 1.2 | Visualización de volúmenes e imágenes de adquisición |
| Wireshark | 4.6.4 | Visualización y seguimiento de tráfico de red |
| Visual Studio Code | 15.6.2 | Lectura de archivos de texto plano |


### 7.2 Procesos

Se muestran las sumas de verificación y los comandos utilizados en el [Anexo 2](#102-anexo-2-sumas-de-verificación)

#### 7.2.1 Análisis del teléfono de la víctima.

Se encontró, por medio de la herramienta de autopsy, una base de datos de la aplicación de mensajería "Hangouts" que contenía una conversación entre la víctima y un tercero. En ella, la víctima parece querer poner fin a la comunicación con esa ppersona.

![alt text](<img/2026-05-13 09_34_36-DBeaver 26.0.4 - messages.png>)

(Figura 1) Conversación entre la víctima y un tercero

De igual manera, pudimos encontrar que el tercero con el que mantenía esta conversación estaba guardado como "John Macron".

![alt text](<img/2026-05-13 14_24_54-DBeaver 26.0.4 - conversations.png>)

(Figura 2) Nombre del usuario con el que la víctima mantuvo la conversación encontrada y último mensaje.

Confirmamos el nombre de la víctima como Hallym Betty.

![alt text](<img/2026-05-13 14_27_19-DBeaver 26.0.4 - participants.png>)

(Figura 3) Nombre de la víctima y nombre del segundo usuario, junto a sus GAIA ID.


Se revisó el dispositivo en busca de cualquier relación con la pulsera deportiva hallada en la escena. Siguiendo ese hilo, obtuvimos un registro de la aplicación de pulseras de actividad de xiaomi en com.xiaomi.health. 

![alt text](<img/2026-05-14 12_15_16-mili_log.txt_ Bloc de notas.png>)

(Figura 4) Registro de actividad de la pulsera. No muestra información relevante en la ventana temporal de los hechos.

#### 7.2.2 Análisis del teléfono del marido de la víctima

Se revisó el dispositivo utilizando la herramienta Autopsy, pero no se pudo encontrar nada relevante para la investigación.




