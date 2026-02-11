# **Informe de análisis de caja blanca**

## Windows Server 2008 y Ubuntu Server 14.04

# **Integrantes:**

Ubuntu Server 14.04:

* Jose María Escalón Prada: Nessus  
* [Abel García Domínguez](mailto:agardom573@g.educaand.es): OpenVAS

Windows Server 2008:

* [Daniel Hernández Gómez](mailto:dhergom961@g.educaand.es): Nessus	  
* [David Jiménez Ruiz](mailto:djimrui878@g.educaand.es): OpenVAS

# **Introducción**

SecureLogistics solicitó una evaluación de seguridad en dos de sus servidores principales para identificar vulnerabilidades y establecer estrategias de mitigación. Este análisis se centra en caja blanca, evaluando los sistemas con acceso a credenciales para detectar fallos en configuraciones internas, permisos de usuarios y vulnerabilidades no visibles en un análisis externo. El documento detalla la metodología aplicada, los resultados obtenidos y las recomendaciones derivadas del análisis.​

# **Objetivo**

El objetivo central es identificar y evaluar vulnerabilidades en los servidores mediante un análisis de caja blanca, proporcionando una visión clara de los riesgos y proponiendo soluciones efectivas para reducir la superficie de ataque y mejorar la postura de seguridad de la empresa.​

# **Alcance**

El análisis cubrió lo siguiente:​  
Sistemas evaluados: Windows Server 2018 y Ubuntu 14.04  
Metodología aplicada: Escaneos con credenciales (caja blanca)  
Herramientas utilizadas: Nessus y GreenBone  
Limitaciones: No se realizaron pruebas de explotación activa para evitar interrupciones en los sistemas

# **Metodología**

Para evaluar la seguridad en los servidores de SecureLogistics aplicamos una metodología de caja blanca estructurada en varias fases, permitiendo un análisis interno más detallado con acceso a credenciales legítimas.​

## **Preparación y configuración de herramientas**

Se seleccionaron Nessus y GreenBone, se configuraron con credenciales de usuario, se definieron rangos de IP, puertos y servicios internos a analizar, y se verificó la correcta autenticación en los sistemas.​

## **Análisis de configuraciones internas** 

Se revisaron permisos de usuarios y grupos para identificar configuraciones excesivamente permisivas, se evaluaron políticas de autenticación, gestión de contraseñas y configuración de servicios internos, y se analizaron los registros del sistema en busca de patrones de actividad sospechosa o indicadores de compromiso.​

## **Escaneo de vulnerabilidades con credenciales**

Se ejecutaron análisis automatizados para detectar fallos en configuraciones internas, software desactualizado y servicios mal configurados, documentando los hallazgos según su criticidad y validándolos manualmente para minimizar falsos positivos.​

## **Análisis y priorización de resultados**

Se aplicó CVSS 3.0 para clasificar las vulnerabilidades según impacto y probabilidad de explotación, se analizaron vías de explotación y se compararon resultados entre herramientas.​

## **Documentación y elaboración de recomendaciones**

Se elaboró el informe con vulnerabilidades identificadas, su impacto y soluciones concretas priorizadas, además de estrategias de mejora en la configuración y gestión de seguridad.​

# **Resultados obtenidos**

## **Ubuntu Server 14.04**

En el escaneo del servidor Ubuntu con Nessus, utilizando credenciales para un análisis interno, obtuvimos los siguientes resultados globales.​  
Aquí se muestran algunas de las vulnerabilidades detectadas:  
​

|  | Vulnerabilidad 1 |
| :---- | :---- |
| Nombre | PHP Unsupported Version Detection |
| Descripción | Según su versión, la instalación de PHP en el host remoto ya no es compatible. La falta de soporte significa que el proveedor no lanzará nuevos parches de seguridad, lo que puede generar vulnerabilidades. |
| Severidad | Crítica |
| CVSS V.3.0 | 10.0 |
| CVE/CWE | [CWE-1104](https://cwe.mitre.org/data/definitions/1104.html) |
| Solución | Actualiza a una versión de PHP que tenga soporte vigente. |

|  | Vulnerabilidad 2 |
| :---- | :---- |
| Nombre | phpMyAdmin prior to 4.8.6 SQLi vulnerability (PMASA-2019-3) |
| Descripción | Según su número de versión autodetectado, la aplicación phpMyAdmin alojada en el servidor web remoto es anterior a la 4.8.6. Por lo tanto, está afectada por una vulnerabilidad de inyección SQL (SQLi) en la función de diseño. Un atacante remoto no autenticado puede explotarla para inyectar o manipular consultas SQL en la base de datos, lo que podría permitir la divulgación o manipulación de datos arbitrarios. |
| Severidad | Crítica |
| CVSS | 9.8 |
| CVE/CWE | [CVE-2019-11768](https://nvd.nist.gov/vuln/detail/CVE-2019-11768) |
| Solución | Actualizar phpMyAdmin a la versión 4.8.6 o posterior. Como alternativa, aplica los parches mencionados en los avisos del proveedor. |

|  | Vulnerabilidad 3 |
| :---- | :---- |
| Nombre | Node.js Module node-tar \< 6.2.1 DoS |
| Descripción | En el módulo de Node.js node-tar, en versiones anteriores a la 6.2.1, no se valida la cantidad de carpetas creadas al descomprimir un archivo. Como resultado, un atacante puede usar un archivo malicioso para agotar la CPU y la memoria del host, causando la caída del cliente de Node.js. Nessus no ha probado estas vulnerabilidades, sino que se ha basado en el número de versión autodetectado de la aplicación. |
| Severidad | Medio |
| CVSS | 6.5 |
| CVE/CWE | [CVE-2024-28863](https://nvd.nist.gov/vuln/detail/CVE-2024-28863) |
| Solución | Actualiza el módulo node-tar a la versión 6.2.1 o posterior. |

|  | Vulnerabilidad 4 |
| :---- | :---- |
| Nombre | Linux Sudo Privilege Escalation (Out-of-bounds Write) |
| Descripción | Sudo, en versiones anteriores a la 1.9.5p2, tiene una vulnerabilidad de desbordamiento de búfer en la memoria dinámica (heap), lo que permite la escalación de privilegios a root mediante \`sudoedit \-s\` y un argumento en la línea de comandos que termina con una barra invertida (\`\\\`). |
| Severidad | Alta |
| CVSS | 7.8 |
| CVE/CWE | [CVE-2021-3156](https://nvd.nist.gov/vuln/detail/CVE-2021-3156) |
| Solución | n/a. |

|  | Vulnerabilidad 5 |
| :---- | :---- |
| Nombre | TLS Version 1.0 Protocol Detection |
| Descripción | El servicio remoto acepta conexiones cifradas con TLS 1.0, el cual presenta fallos de diseño criptográfico. Aunque algunas implementaciones modernas mitigan estos problemas, se recomienda usar TLS 1.2 o 1.3, que han sido diseñados para evitar estas vulnerabilidades. Desde el 31 de marzo de 2020, los sistemas que no admitan TLS 1.2 o superior podrían dejar de funcionar con los principales navegadores y proveedores. Además, PCI DSS v3.2 exige la desactivación completa de TLS 1.0 desde el 30 de junio de 2018, excepto en terminales POS POI que se verifiquen como seguras ante ataques conocidos. |
| Severidad | Medio |
| CVSS | 6.5 |
| CVE/CWE | [CWE-327](https://cwe.mitre.org/data/definitions/327) |
| Solución | Habilita el soporte para TLS 1.2 y 1.3 y desactiva TLS 1.0. |

|  | Vulnerabilidad 6 |
| :---- | :---- |
| Nombre | MySQL Denial of Service (Jul 2020 CPU) |
| Descripción | La versión de MySQL en el host remoto (5.7.29 o anterior, 8.0.19 o anterior) es vulnerable a una falla en la replicación que puede ser explotada por un atacante con acceso a la red, lo que podría causar un bloqueo o caída repetida del servidor MySQL. Esta vulnerabilidad fue documentada en el aviso de actualización crítica de julio de 2020\. |
| Severidad | Medio |
| CVSS | 4.9 |
| CVE/CWE | [CVE-2020-14567](https://nvd.nist.gov/vuln/detail/CVE-2020-14567) |
| Solución | Consulta el aviso del proveedor. |

Anexo completo: abel pon aquí el anexo

## **Windows Server 2018**

En el escaneo del servidor Windows con Nessus, utilizando credenciales para un análisis interno, obtuvimos los siguientes resultados globales.​  
Aquí se muestran algunas de las vulnerabilidades detectadas:​

|  | Vulnerabilidad 1 |
| :---- | :---- |
| Nombre | Apache Log4j SEoL (\<= 1.x) |
| Descripción | Según su versión, Apache Log4j es igual o inferior a la 1.x. Por lo tanto, ya no cuenta con mantenimiento por parte de su proveedor o desarrollador. La falta de soporte implica que no se lanzarán nuevos parches de seguridad para el producto por parte del proveedor. Como resultado, puede contener vulnerabilidades de seguridad. |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CWE-200](https://cwe.mitre.org/data/definitions/200.html) |
| Solución | Actualiza a una versión de Apache Log4j que actualmente esté soportada. |

|  | Vulnerabilidad 2 |
| :---- | :---- |
| Nombre | ManageEngine Desktop Central 8 / 9 \< Build 91100 Multiple RCE |
| Descripción | La aplicación ManageEngine Desktop Central que se ejecuta en el host remoto es de la versión 8 o de la versión 9 anterior a la construcción 91100\. Por lo tanto, está afectada por múltiples vulnerabilidades de ejecución remota de código: \- Existe un fallo en el script \*statusUpdate\* debido a la falta de sanitización adecuada de la entrada proporcionada por el usuario al parámetro 'fileName'. Un atacante remoto no autenticado puede explotarlo mediante una solicitud manipulada para cargar un archivo PHP que tenga múltiples extensiones de archivo y, al manipular el parámetro 'applicationName', realizar una solicitud directa al archivo cargado, lo que resulta en la ejecución de código arbitrario con privilegios de NT-AUTHORITY\\SYSTEM. (CVE-2015-82001) Existe un fallo no especificado en varios servlets que permite a un atacante remoto no autenticado ejecutar código arbitrario. No se dispone de más detalles. |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CVE-2015-82001](https://www.tenable.com/cve/CVE-2015-82001) |
| Solución | Actualice a la versión 9 de ManageEngine Desktop Central, construcción 91100 o posterior. |

|  | Vulnerabilidad 3 |
| :---- | :---- |
| Nombre | MS KB3118753: Update for ActiveX Kill Bits |
| Descripción | El host remoto de Windows no tiene configurados uno o más killbits para los controles ActiveX que se sabe contienen vulnerabilidades. Si alguno de estos controles ActiveX se instala en el host (ya sea ahora o en el futuro), podría exponer al sistema a diversos problemas de seguridad. Los controles afectados provienen de proveedores de terceros que han solicitado a Microsoft evitar que sus controles se ejecuten en Internet Explorer. |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CWE-1104](https://cwe.mitre.org/data/definitions/1104.html) |
| Solución | Microsoft ha lanzado un conjunto de parches para Windows Vista, 2008, 7, 2008 R2, 8, RT, 2012, 8.1, RT 8.1, 2012 R2 y 10\. |

|  | Vulnerabilidad 4 |
| :---- | :---- |
| Nombre | Microsoft Internet Explorer Unsupported Version Detection |
| Descripción | Según el número de versión reportado por sí mismo, la instalación de Microsoft Internet Explorer en el host remoto de Windows ya no está soportada. La falta de soporte implica que no se lanzarán nuevos parches de seguridad para el producto por parte del proveedor. Como resultado, es probable que contenga vulnerabilidades de seguridad. |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CWE-1104](https://cwe.mitre.org/data/definitions/1104.html) |
| Solución | Actualice a una versión de Internet Explorer que esté actualmente soportada o desactive Internet Explorer en el dispositivo de destino. |

|  | Vulnerabilidad 5 |
| :---- | :---- |
| Nombre | MS11-020: Vulnerability in SMB Server Could Allow Remote Code Execution |
| Descripción | El host remoto está afectado por una vulnerabilidad en el servidor SMB que podría permitir a un atacante ejecutar código arbitrario o realizar un ataque de denegación de servicio (DoS) contra el host remoto. |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CVE-2011-0661](https://nvd.nist.gov/vuln/detail/CVE-2011-0661) |
| Solución | Microsoft ha publicado un conjunto de parches para Windows XP, Vista, 2008, 7 y 2008 R2. |

|  | Vulnerabilidad 6 |
| :---- | :---- |
| Nombre | MS14-066: Vulnerability in Schannel Could Allow Remote Code Execution |
| Descripción | El host remoto de Windows está afectado por una vulnerabilidad de ejecución remota de código debido a un procesamiento incorrecto de paquetes por parte del paquete de seguridad Secure Channel (Schannel). Un atacante puede explotar esta vulnerabilidad enviando paquetes especialmente diseñados a un servidor Windows. |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CVE-2014-6321](https://nvd.nist.gov/vuln/detail/CVE-2014-6321) |
| Solución | Microsoft ha publicado un conjunto de parches para Windows 2003, Vista, 2008, 7, 2008 R2, 8, 2012, 8.1 y 2012 R2. |

|  | Vulnerabilidad 7 |
| :---- | :---- |
| Nombre | PHP 5.3.x \< 5.3.15 Multiple Vulnerabilities |
| Descripción | Según su banner, la versión de PHP instalada en el host remoto es 5.3.x anterior a la 5.3.15, y por lo tanto, puede estar afectada por las siguientes vulnerabilidades: \- Existe una vulnerabilidad de desbordamiento no especificada en la función '\_php\_stream\_scandir' en el archivo 'main/streams/streams.c'. (CVE-2012-2688) \- Existe un error no especificado que puede permitir sortear la restricción 'open\_basedir'. (CVE-2012-3365) |
| Severidad | Crítico |
| CVSS | 10.0 |
| CVE/CWE | [CVE-2012-2688](https://nvd.nist.gov/vuln/detail/CVE-2012-2688) ,  [CVE-2012-3365](https://nvd.nist.gov/vuln/detail/CVE-2012-3365) |
| Solución | Actualice a la versión 5.3.15 de PHP o posterior. |

|  | Vulnerabilidad 8 |
| :---- | :---- |
| **Nombre** | MySQL 5.5.x \< 5.5.62 Multiple Vulnerabilities (October 2018 CPU) |
| **Descripción** | La versión de MySQL que se ejecuta en el host remoto es 5.5.x anterior a la 5.5.62. Por lo tanto, está afectada por múltiples vulnerabilidades como se indica en el aviso de la Actualización Crítica de Parches de octubre de 2018\. Consulte los detalles del CVRF para obtener información adicional sobre los CVEs aplicables. Tenga en cuenta que Nessus no ha probado estas vulnerabilidades, sino que se ha basado únicamente en el número de versión reportado por la aplicación. |
| **Severidad** | Crítico |
| **CVSS** | 9.8 |
| **CVE/CWE** | [CVE-2016-9843](https://nvd.nist.gov/vuln/detail/CVE-2016-9843) ,  [CVE-2018-3133](https://nvd.nist.gov/vuln/detail/CVE-2018-3133) ,  [CVE-2018-3174](https://nvd.nist.gov/vuln/detail/CVE-2018-3174) ,  [CVE-2018-3282](https://nvd.nist.gov/vuln/detail/CVE-2018-3282) |
| **Solución** | Actualice a la versión 5.5.62 de MySQL o posterior. |

# **Comparativa entre los análisis**

## **Caja negra**

El análisis de caja negra se realiza desde una perspectiva externa, simulando el comportamiento de un atacante sin acceso privilegiado ni conocimiento previo sobre la infraestructura interna del sistema. Este enfoque se centra en evaluar la funcionalidad y la seguridad del sistema tal como se presenta al exterior, identificando vulnerabilidades que podrían ser explotadas sin información interna. Las pruebas de caja negra son útiles para determinar cómo un intruso podría interactuar con el sistema y qué riesgos representan para los servicios expuestos.​

## **Caja blanca**

El análisis de caja blanca implica una evaluación profunda del sistema con acceso completo al código fuente, configuraciones internas y credenciales de usuario. Esto permite realizar un examen detallado de la lógica interna, los flujos de datos y las condiciones de control, proporcionando una visión más exhaustiva de las posibles vulnerabilidades. Este tipo de pruebas es ideal para detectar errores en el diseño o implementación que no serían evidentes desde una perspectiva externa.​

En conclusión, mientras que las pruebas de caja negra se centran en evaluar la seguridad desde el exterior, las pruebas de caja blanca permiten un análisis interno más detallado. Un ejemplo práctico sería que los escáneres con credenciales proporcionadas descubrieron vulnerabilidades críticas como "Canonical Ubuntu Linux SEoL" en servidores internos, algo que no fue posible identificar mediante pruebas externas. Esto demuestra que el acceso interno facilita una comprensión más completa del sistema y la detección de problemas profundos.​

# **Conclusiones**

El análisis de caja blanca ha permitido identificar vulnerabilidades críticas que comprometen la seguridad interna de los sistemas de la empresa. Se han detectado fallos en permisos de usuarios, configuraciones inseguras en servicios esenciales y debilidades en políticas de autenticación.​

Para mitigar los riesgos detectados es necesario aplicar medidas correctivas que reduzcan la superficie de ataque. Es fundamental reforzar la gestión de accesos, implementando controles más estrictos y aplicando políticas de contraseñas robustas. También se recomienda la actualización de software y aplicación de parches de seguridad, eliminando configuraciones obsoletas y optimizando la protección de servicios críticos.​

El monitoreo continuo y las auditorías de seguridad permitirán detectar nuevas amenazas a tiempo y prevenir incidentes graves. El establecimiento de políticas de control de acceso y segmentación de redes contribuirá a reducir la exposición de los sistemas ante accesos no autorizados.​