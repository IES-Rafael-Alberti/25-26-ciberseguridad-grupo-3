# Anexos — Caso Forense Digital

## Indice

1. [Metodologia](#metodologia)
2. [Herramientas Empleadas](#herramientas)
3. [Imagenes](#imagenes)
4. [Vestigios](#vestigios)

---

## 1. Metodologia<div id='metodologia' />

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

---

## 2. Herramientas Empleadas<div id='herramientas' />

| Herramienta | Version | Uso |
| --- | --- | --- |
| WhatsApp Msgstore Viewer | Ultima disponible | Lectura y visualizacion de mensajes desde msgstore.db |
| DB Browser for SQLite | 3.12.2.0 | Inspeccion manual de bases de datos SQLite |
| FTK Imager | 3.1.2 | Adquisicion y verificacion de imagenes forenses |
| Android Backup Extractor | master-20221109063121 | Extraccion de copias de seguridad ADB |
| telegram_extractor.py | 1.0 (script propio) | Extraccion de mensajes desde cache4.db de Telegram |
| USB Detective | 1.2 | Analisis de artefactos de conexion de dispositivos USB |

---

## 3. Imagenes<div id='imagenes' />

[Imagen 1](#1) | [Imagen 2](#2) | [Imagen 3](#3) | [Imagen 4](#4) | [Imagen 5](#5) |
[Imagen 6](#6) | [Imagen 7](#7) | [Imagen 8](#8) | [Imagen 9](#9) | [Imagen 10](#10) |
[Imagen 11](#11) | [Imagen 12](#12) | [Imagen 13](#13) | [Imagen 14](#14) |
[Imagen 15](#15) | [Imagen 16](#16) | [Imagen 17](#17) | [Imagen 18](#18) |
[Imagen 19](#19) | [Imagen 20](#20) | [Imagen 21](#21) | [Imagen 22](#22) |
[Imagen 23](#23)

Imagen 1<div id='1' />
![whats-Atalus_Lassandra.png](img/whats-Atalus_Lassandra.png)

Imagen 2<div id='2' />
![whats-Atalus_Lassandra_2.png](img/whats-Atalus_Lassandra_2.png)

Imagen 3<div id='3' />
![whats-Atalus_Lassandra_3.png](img/whats-Atalus_Lassandra_3.png)


Imagen 4<div id='4' />
![whats-Atalus_Camilo.png](img/whats-Atalus_Camilo.png)

Imagen 5<div id='5' />
![whats-Atalus_Camilo_2.png](img/whats-Atalus_Camilo_2.png)

Imagen 6<div id='6' />
![whats-Atalus_Camilo_3.png](img/whats-Atalus_Camilo_3.png)

Imagen 7<div id='7' />
![whats-Atalus_Camilo_4.png](img/whats-Atalus_Camilo_4.png)

Imagen 8<div id='8' />
![whats-Atalus_Camilo_5.png](img/whats-Atalus_Camilo_5.png)

Imagen 9<div id='9' />
![whats-Atalus_Camilo_6.png](img/whats-Atalus_Camilo_6.png)

Imagen 10<div id='10' />
![Telegram_Lassandra.png](img/Telegram_Lassandra.png)

Imagen 11<div id='11' />
![Busqueda-Atalus_Ruberducky.png](img/Busqueda-Atalus_Ruberducky.png)

Imagen 12<div id='12' />
![Busqueda-Atalus_Ruberducky_2.png](img/Busqueda-Atalus_Ruberducky_2.png)

Imagen 13<div id='13' />
![IMAGEN_USB.png](img/IMAGEN_USB.png)

Imagen 14<div id='14' />
![IMAGEN_INICIO_PC.png](img/IMAGEN_INICIO_PC.png)

Imagen 15<div id='15' />
![INICIO_SESION_INSTAGRAM.png](img/INICIO_SESION_INSTAGRAM.png)

Imagen 16<div id='16' />
![INICIO_SESION_INSTAGRAM_2_Atalus.png](img/INICIO_SESION_INSTAGRAM_2_Atalus.png)

Imagen 17<div id='17' />
![Atalus_Sesion.png](img/Atalus_Sesion.png)

Imagen 18<div id='18' />
![IMAGEN_INSTAGRAM.png](img/IMAGEN_INSTAGRAM.png)

Imagen 19<div id='19' />
![BUSQUEDA_ATALUS_IMAGEN_INSTAGRAM.png](img/BUSQUEDA_ATALUS_IMAGEN_INSTAGRAM.png)

Imagen 20<div id='20' />
![MAS_CAMBIOS_INSTAGRAM.png](img/MAS_CAMBIOS_INSTAGRAM.png)

Imagen 21<div id='21' />
![CORREOS_LASSANDRA.png](img/CORREOS_LASSANDRA.png)

## 4. Vestigios<div id='vestigios' />

[Vestigio 1](#v1) | [Vestigio 2](#v2) | [Vestigio 3](#v3) | [Vestigio 4](#v4) |
[Vestigio 5](#v5) | [Vestigio 6](#v6) | [Vestigio 7](#v7) | [Vestigio 8](#v8) |
[Vestigio 9](#v9) | [Vestigio 10](#v10)

Vestigio 1<div id='v1' />

| Campo | Valor |
| --- | --- |
| Ruta | WhatsApp-Database-Lassandra-Cordalis/msgstore.db |
| Tamano | 1.228.800 bytes |
| HASH MD5 | 4f7e0758d093ce4cf33e1c851dc62c9f |
| HASH SHA256 | dcc837420c7d72b7b3ea09483ff0586daa7a50ca9c8c78b790db95866dcae0f5 |
| Contenido | ![whats-Atalus_Lassandra.png](img/whats-Atalus_Lassandra.png) |

Vestigio 2<div id='v2' />

| Campo | Valor |
| --- | --- |
| Ruta | WhatsApp-Database-Atalus-Grasstem/msgstore.db |
| Tamano | 1.273.856 bytes |
| HASH MD5 | abfacf6b7a029fe358d0a13c3ce7e2a8 |
| HASH SHA256 | 4a053239cfacab3f674a875c84cc0d80d873a418e608e1be249a26f93870f3cc |
| Contenido | ![whats-Atalus_Camilo.png](img/whats-Atalus_Camilo.png) |

Vestigio 3<div id='v3' />

| Campo | Valor |
| --- | --- |
| Ruta | Google-Data-Atalus-Grasstem/takeout-20230505T011442Z-001/Takeout/Mi actividad/Busqueda/MiActividad.html |
| Tamano | 168.832 bytes |
| HASH MD5 | 107aa75dd60145151336cccaab37f21e |
| HASH SHA256 | dcbd51ba2f77917998623ae88b82ff10697bd8b53c78a46bbc9d6a8e28bcf1fe |
| Contenido | ![Busqueda-Atalus_Ruberducky.png](img/Busqueda-Atalus_Ruberducky.png) |

Vestigio 4<div id='v4' />

| Campo | Valor |
| --- | --- |
| Ruta | telegram/apps/org.telegram.messenger/f/cache4.db |
| Tamano | 4.096 bytes |
| HASH MD5 | 48fd1091cab6792ec9f4f79184fc4a8e |
| HASH SHA256 | 7c0cbac0764d013f7a25b5fddabdc2e74706cd17c04d7c30c4d51c58b254b5eb |
| Contenido | ![Telegram_Lassandra.png](img/Telegram_Lassandra.png) |

Vestigio 5<div id='v5' />

| Campo | Valor |
| --- | --- |
| Ruta | 17.39.20-17.39.44[M][0@0][0].dav |
| Tamano | 2.996 bytes |
| HASH MD5 | D3FA864032CD8FFD1CEF129A36CF12F2 |
| HASH SHA256 | 021D1FCECC68A891511F68C289DA96A1685BFD07191653B7950DA74B9403CC30 |
| Contenido | ![IMAGEN_USB.png](img/IMAGEN_USB.png) |

Vestigio 6<div id='v6' />

| Campo | Valor |
| --- | --- |
| Ruta | 17.59.49-18.01.13[M][0@0][0].dav |
| Tamano | 3.254 bytes |
| HASH MD5 | 12ECF537472C82E6BF0E468943DDB3AF |
| HASH SHA256 | C1AC93D989B1001AE5B86BEA7CDAD34144A52A39E91B381D2CCC4518578209C7 |
| Contenido | ![IMAGEN_INICIO_PC.png](img/IMAGEN_INICIO_PC.png) |

Vestigio 7<div id='v7' />

| Campo | Valor |
| --- | --- |
| Ruta | Instagram-lassandracordalis-20230504/login_and_account_creation/login_activity.html |
| Tamano | 17.298 bytes |
| HASH MD5 | 689EB9D3D2A866648F68F76E6A8C3D46 |
| HASH SHA256 | 2A8C5AF4B19E1144088FF271EC893E963A454107FACB5F7155C2EC33CFA17B6A |
| Contenido | ![INICIO_SESION_INSTAGRAM.png](img/INICIO_SESION_INSTAGRAM.png) |

Vestigio 8<div id='v8' />

| Campo | Valor |
| --- | --- |
| Ruta | Google-Data-Atalus-Grasstem/takeout-20230505T011442Z-001/Takeout/Cuenta de Google/atalusgrasstem.SubscriberInfo.html |
| Tamano | 2.986 bytes |
| HASH MD5 | 71548337338d0d7c2aecb330cc04be68 |
| HASH SHA256 | 49069e702aebb747b41c2e9ecb50064c85e237b2cda207f5974b718599fe57a8 |
| Contenido | ![Atalus_Sesion.png](img/Atalus_Sesion.png) |

Vestigio 9<div id='v9' />

| Campo | Valor |
| --- | --- |
| Ruta | adb-backup-Atalus-Grasstem.ab\apps\com.android.browser\db\browser2.db |
| Tamano | 1.093.632 bytes |
| HASH MD5 | d454901677e278c43884799496ba7a9f |
| HASH SHA256 | a2be3a1c3bf4f32bcea3cff31dde9de2363a5fca2792835543b15c9654d4d1b8 |
| Contenido | ![BUSQUEDA_ATALUS_IMAGEN_INSTAGRAM.png](img/BUSQUEDA_ATALUS_IMAGEN_INSTAGRAM.png) |

Vestigio 10<div id='v10' />

| Campo | Valor |
| --- | --- |
| Ruta | Google-Data-Lassandra-Cordalis/takeout-20230430T183453Z-002/Takeout/Correo/Todo el correo, incluido Spam y Papelera.mbox |
| Tamano | 178.038 bytes |
| HASH MD5 | 6e723fa81c3a0377d9f01ab4e4f9181a |
| HASH SHA256 | 783807d627db0248bb0aff40544bc5078fcd8d882dd88d223819e10456f6b3af |
| Contenido | ![CORREOS_LASSANDRA.png](img/CORREOS_LASSANDRA.png) |