# **Informe de Análisis Forense** **Proyecto 3: Unfaithful Employee**

Analistas: Jose Mª Escalón Prada, Daniel Hernández Gómez, Abel García Dominguez, David Jimenez​  
Fecha: 05 de febrero de 2026​  
Caso: Investigación interna de la empresa InnovaTech Solutions​  
Sujeto: Richard Eduardo Warner​

# **Introducción**

En este informe se documenta el análisis forense realizado sobre la imagen del disco duro asignado al empleado Richard Eduardo Warner, trabajador de InnovaTech Solutions. El objetivo principal es determinar si se han producido usos indebidos de los recursos de la empresa, exfiltración de información o cualquier otra actividad que pueda suponer un riesgo para la organización.​

Para ello se ha trabajado sobre la imagen forense proporcionada por el departamento de sistemas, combinando el uso de herramientas como Autopsy y Windows Registry Recovery para examinar el sistema operativo, el registro de Windows, los historiales de navegación y el correo electrónico.​

1. # **Verificación de la integridad de la evidencia**

El primer paso del análisis ha consistido en comprobar la integridad de la imagen forense comparando los hashes entregados por el departamento de sistemas con los hashes calculados localmente. Esta comprobación es fundamental para asegurar que la evidencia no ha sido modificada desde su adquisición.​

Hashes proporcionados por el departamento de sistemas (Alan):​  
MD5: dfdfba2231e3fa409676b1b737474208  
SHA-1: f476a81089a10f9d5393aa8c2f8bbccdb87f7d3c  
SHA-256: 66d6ee7a61ea7a986e8f6bb54b9986f79d95b5a0278bef86678ed42ace320d96

Hashes calculados sobre la imagen analizada:​  
MD5: DFDFBA2231E3FA409676B1B737474288  
SHA-1: F476A81089A10F9D5393AA8C2F8BBCCDB87F7D3C  
SHA-256: 66D6EE7A61EA7A986E8F6BB54B9986F79D95B5A0278BEF86678ED42ACE320D9B

Al comparar los resultados se observa que el valor SHA-1 coincide exactamente, mientras que existen diferencias en los valores MD5 y SHA-256 respecto a los hashes iniciales. Esto indica una posible anomalía en la cadena de custodia, ya sea por una modificación de la imagen o por un error de documentación en los hashes originales.​

Aunque esta discrepancia afecta a la confianza total en la evidencia, se ha decidido continuar con el análisis dejando claramente registrada esta incidencia en el informe.​

2. # **Identificación del usuario y último inicio de sesión**

Para confirmar la identidad del usuario y sus accesos se ha analizado el registro SAM del sistema (ruta C:/Windows/System32/config/SAM/) utilizando la herramienta Windows Registry Recovery. En este fichero se almacena la información de las cuentas locales de Windows.​

Del análisis se obtiene que existe una cuenta de usuario denominada “Richard”, asociada al empleado investigado. Además, los metadatos de la cuenta muestran que el último inicio de sesión se produjo el 22 de febrero de 2023 a las 13:55:18, hora del sistema.​

Este dato sitúa la última actividad autenticada de Richard en el equipo el mismo día en que se han detectado otras acciones relevantes, como la conexión de dispositivos USB y el envío de información por correo.​

3. # **Información del sistema**

A continuación se ha revisado la configuración general del equipo a partir de los registros SYSTEM y SOFTWARE del sistema operativo mediante las mismas herramientas de análisis del registro.​

Los resultados muestran que el nombre del equipo (hostname) es LADRONERA y que el sistema operativo instalado es Windows 10 Pro Education N. Esta información resulta útil para contextualizar el entorno de trabajo del usuario y entender qué aplicaciones y servicios pueden estar presentes.​

4. # **Uso de dispositivos USB**

Dado que la empresa tiene políticas estrictas sobre el uso de dispositivos externos, se ha revisado el registro de Windows en busca de evidencias de conexiones USB. Para ello se han analizado las claves de registro relacionadas con dispositivos de almacenamiento, utilizando Windows Registry Recovery sobre la rama SYSTEM\\\\CurrentControlSet\\\\Enum.​

En esta revisión se ha identificado la conexión de un dispositivo de almacenamiento externo con las siguientes características:​  
Dispositivo: Kingston DataTraveler 3.0 USB Device  
Primera conexión registrada: 22 de febrero de 2023 a las 00:27:42

La presencia de este dispositivo confirma que se ha utilizado un USB en el equipo a pesar de las políticas corporativas que lo prohíben. El momento de conexión es especialmente relevante, ya que coincide con el periodo de tensión laboral previo a la salida de Richard y con el resto de actividades sospechosas observadas en el sistema.​

5. # **Actividad en línea y uso de recursos corporativos**

La siguiente parte del análisis se ha centrado en el historial de navegación web para determinar si Richard hacía un uso adecuado de los recursos de la empresa o si dedicaba tiempo a actividades ajenas a sus funciones. Para ello se han revisado los historiales de los navegadores instalados, principalmente Firefox y Opera.​

Los resultados indican un uso intensivo del navegador para actividades de ocio:

Se han encontrado búsquedas relacionadas con la película “Trabajo Basura” y accesos a páginas de streaming como “CUEVANAHD” y “CINE24H”, lo que muestra que el usuario ha consumido contenido audiovisual online desde el equipo corporativo.​

También se ha detectado navegación en tiendas online como Amazon, lo que apunta a compras o consultas personales realizadas durante el uso del equipo de la empresa.​

Además, el historial muestra accesos a la plataforma de trading y apuestas eToro, lo que supone un uso del equipo para actividades económicas personales y potencialmente de riesgo.​

En relación con sus gustos personales, aparecen búsquedas de música rock y heavy, incluyendo canciones y contenido de grupos como AC/DC y Aerosmith, junto con visitas repetidas a páginas de noticias deportivas desde el navegador Opera.​

En conjunto, esta actividad confirma que Richard ha utilizado el equipo de la empresa para entretenimiento, apuestas y consumo de contenido en streaming, lo que puede considerarse un uso indebido de los recursos corporativos.​

6. # **Planes de viaje y movilidad tras su salida**

Otra de las preguntas planteadas es si Richard tenía previsto viajar tras abandonar la empresa y cómo planeaba hacerlo. Para responder a esto se ha seguido examinando el historial de navegación y las búsquedas recientes.​

En este análisis se han identificado búsquedas de vuelos a Gran Canaria a través del portal de la aerolínea Vueling, así como consultas de alojamiento en “Las Palmas de Gran Canaria” por medio de Booking.com.​

Estos indicios apuntan a que Richard estaba organizando un viaje a Gran Canaria, combinando transporte en avión y reserva de hotel, lo que encaja con la planificación de unas vacaciones o una estancia temporal tras su salida de la empresa.​

7. # **Software no autorizado al inicio de sesión**

También se ha revisado si existía algún navegador o programa adicional configurado para ejecutarse de forma automática al iniciar sesión el usuario Richard, distinto de los navegadores ofrecidos por defecto por Microsoft.​

Para ello se ha analizado el fichero NTUSER.DAT del perfil de Richard, concretamente la clave Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run, que almacena las entradas de programas configurados en el inicio.​

En esta clave se ha encontrado que el navegador Opera está configurado para iniciarse automáticamente cuando el usuario inicia sesión en el sistema. Además, se ha comprobado que Mozilla Firefox está instalado en el equipo (según las entradas de registro bajo SOFTWARE\\\\Mozilla\\\\Mozilla Firefox), pero no aparece configurado para ejecutarse al inicio.​

La presencia de Opera en el arranque refuerza la idea de que este navegador era uno de los principales medios de Richard para navegar, incluyendo su actividad de ocio, apuestas y búsquedas personales.​

8. # **Exfiltración de información y correos electrónicos**

Una parte crítica del análisis ha consistido en comprobar si Richard ha colaborado con terceros o competidores mediante la exfiltración de datos de la empresa usando el correo electrónico.​

En la revisión de los mensajes de correo se ha localizado una conversación entre las cuentas proba1.seguridade@gmail.com, asociada a Richard, y proba2.seguridade@gmail.com, vinculada a la competencia.​

En estos intercambios se observan los siguientes hechos:​

Richard contacta con la competencia para solicitar un aumento salarial o una oferta económica mejor, presentándose como empleado de InnovaTech Solutions.

Envía como “prueba” un archivo denominado pom.xml, perteneciente al proyecto “reverb-master”, el día 22/02/2023, que contiene información sensible ligada a un desarrollo de la empresa.​

En un mensaje posterior, remite un enlace a Google Drive protegido con contraseña y exige un pago en Bitcoin a cambio de conceder acceso completo al material exfiltrado.​

Este conjunto de acciones demuestra una exfiltración clara de datos confidenciales de la empresa y un intento de obtener un beneficio económico personal a costa de los activos de InnovaTech Solutions.​

9. # **Conclusiones**

Tras completar el análisis de la imagen del disco duro asociado a Richard Eduardo Warner, se pueden extraer las siguientes conclusiones generales sobre su comportamiento en el equipo corporativo.​

En primer lugar, la verificación de la integridad de la imagen revela discrepancias en los hashes MD5 y SHA-256 frente a los proporcionados inicialmente, aunque el valor SHA-1 coincide. Esto obliga a dejar constancia de una posible anomalía en la cadena de custodia, pero no impide continuar con la investigación siempre que se documente adecuadamente.​

En segundo lugar, se confirma la existencia del usuario “Richard” en el sistema y que su último inicio de sesión se produjo el 22 de febrero de 2023, fecha que coincide con la conexión de un dispositivo USB Kingston DataTraveler 3.0 y con el envío de información a la competencia.​

En tercer lugar, se comprueba que Richard ha usado el equipo de la empresa para actividades que no forman parte de sus funciones, incluyendo la visualización de películas online en plataformas de streaming, apuestas y trading en eToro, compras en tiendas online y búsquedas de contenido musical y deportivo. Este uso reiterado de los recursos corporativos para fines personales puede considerarse un mal uso del equipo.​

Además, el historial de navegación muestra que el usuario estaba planeando un viaje a Las Palmas de Gran Canaria, consultando vuelos y hoteles tras el conflicto con la empresa, lo que indica una intención clara de desplazarse tras su salida.​

Por último, el análisis del correo electrónico demuestra de forma directa la exfiltración de información sensible de InnovaTech Solutions hacia una cuenta vinculada a la competencia, así como la intención de obtener un beneficio económico mediante el envío de un archivo del proyecto reverb-master y un enlace protegido en Google Drive a cambio de un pago en Bitcoin.​

En conjunto, la evidencia recopilada indica que Richard no solo hizo un uso inadecuado de los recursos tecnológicos de la empresa, sino que también llevó a cabo acciones que comprometen la confidencialidad de los proyectos de InnovaTech Solutions y suponen un riesgo serio para la organización. Estas conclusiones podrían justificar medidas disciplinarias severas y servir de base para acciones legales por parte de la empresa.