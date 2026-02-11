# **Informe de análisis de vulnerabilidades**

## Windows Server 2008 y Ubuntu Server 14.04

# **Integrantes:**

Ubuntu Server 14.04:

* Jose María Escalón Prada: Nessus  
* [Abel García Domínguez](mailto:agardom573@g.educaand.es): OpenVAS

Windows Server 2008:

* [Daniel Hernández Gómez](mailto:dhergom961@g.educaand.es): Nessus	  
* [David Jiménez Ruiz](mailto:djimrui878@g.educaand.es): OpenVAS

# **Introducción**

La empresa SecureLogistics solicitó una evaluación de seguridad en dos de sus servidores principales para identificar vulnerabilidades y establecer un plan de mitigación. Este análisis se centra en caja negra, evaluando los sistemas desde la perspectiva de un atacante sin credenciales, lo que permite detectar fallos explotables desde el exterior. El documento detalla la metodología, los resultados obtenidos y las recomendaciones derivadas del análisis.​

# **Objetivos**

El objetivo central es identificar y evaluar vulnerabilidades en los servidores mediante un análisis de caja negra, proporcionando una visión clara de los riesgos y proponiendo soluciones efectivas para reducir la superficie de ataque.​

# **Alcance**

El análisis cubrió lo siguiente:​  
Sistemas evaluados: Windows Server 2008 y Ubuntu 14.04  
Metodología aplicada: Escaneos sin credenciales (caja negra)  
Herramientas utilizadas: Nessus y OpenVAS (GreenBone)  
Limitaciones: No se realizaron pruebas de explotación activa para evitar interrupciones en los sistemas

# **Metodología**

Para evaluar la seguridad en los servidores de SecureLogistics aplicamos una metodología de caja negra estructurada en varias fases, intentando replicar el comportamiento de un atacante sin credenciales.:

* **Preparación y configuración de herramientas:** Se seleccionaron Nessus y  OpenVAS (GreenBone), se definieron rangos de IP, puertos y servicios expuestos, y se verificó la accesibilidad de los objetivos.​  
    
* **Reconocimiento y enumeración de servicios:** Se recopiló información sobre los servicios que estaban accesibles, se identificaron versiones de software y se evaluaron puertos abiertos y protocolos para detectar exposiciones.​  
    
* **Escaneo de vulnerabilidades:** Se ejecutaron análisis automatizados para detectar fallos en configuraciones, software desactualizado y servicios expuestos, documentando los hallazgos según su criticida.​  
    
* **Análisis y priorización de resultados:** Se aplicó CVSS 3.0 para clasificar las vulnerabilidades según impacto y probabilidad de explotación, se analizaron vías de explotación y se compararon resultados entre herramientas.​  
    
* **Documentación y elaboración de recomendaciones:** Se elaboró el informe con vulnerabilidades identificadas, su impacto y soluciones concretas por orden de prioridad según su criticidad y nuestro criterio.​

# **Resultados obtenidos**

## **Nessus**

### **Ubuntu Server 14.04**

En el escaneo del servidor Ubuntu con **Nessus** obtuvimos los siguientes resultados globales.​

Aquí se muestran algunas de las vulnerabilidades detectadas:​

|  | Vulnerabilidad 1 |
| :---- | :---- |
| **Nombre** | Drupal Coder Module Deserialization RCE |
| **Descripción** | Drupal tiene una falla de seguridad en el módulo Coder que permite a un atacante sin autenticación ejecutar código malicioso en el servidor mediante una petición manipulada. |
| **Severidad** | Crítico |
| **CVSS V.3.0** | 10.0 |
| **CVE/CWE** | [CWE-502](https://cwe.mitre.org/data/definitions/502.html) |
| **Solución** | Actualiza el módulo Coder a la versión 7.x-1.3 / 7.x-2.6 o posterior. Como alternativa, elimina el directorio completo del módulo Coder de cualquier sitio web accesible públicamente. |

|  | Vulnerabilidad 2 |
| :---- | :---- |
| **Nombre** | ProFTPD mod\_copy Information Disclosure |
| **Descripción** | El host remoto ejecuta una versión de ProFTPD con una vulnerabilidad en el módulo mod\_copy, que permite a atacantes no autenticados usar los comandos SITE CPFR y SITE CPTO para leer y escribir archivos en cualquier ruta accesible del servidor. |
| **Severidad** | Crítico |
| **CVSS** | 9.8 |
| **CVE/CWE** | [CVE-2015-3306](https://nvd.nist.gov/vuln/detail/CVE-2015-3306) |
| **Solución** | Mejorar la versión a ProFTPD 1.3.5a / 1.3.6rc1 o posterior. |

|  | Vulnerabilidad 3 |
| :---- | :---- |
| **Nombre** | Drupal Database Abstraction API SQLi |
| **Descripción** | El servidor web remoto ejecuta una versión de Drupal con una vulnerabilidad de inyección SQL en su API de abstracción de base de datos. Esto permite a un atacante remoto enviar solicitudes manipuladas para ejecutar comandos SQL arbitrarios, lo que podría llevar a la escalación de privilegios, ejecución de código PHP o incluso ejecución remota de código. |
| **Severidad** | Alta |
| **CVSS** | 7.5 |
| **CVE/CWE** | [CVE-2014-3704](https://nvd.nist.gov/vuln/detail/CVE-2014-3704) |
| **Solución** | Mejorar a la versión 7.32 o posterior. |

|  | Vulnerabilidad 4 |
| :---- | :---- |
| **Nombre** | SSL Medium Strength Cipher Suites Supported (SWEET32) |
| **Descripción** | El host remoto admite cifrados SSL con una encriptación de fuerza media. Nessus considera de fuerza media cualquier cifrado con claves de entre 64 y 112 bits, o que use el conjunto de cifrado 3DES. |
| **Severidad** | Alta |
| **CVSS** | 7.5 |
| **CVE/CWE** | [CVE-2016-2183](https://nvd.nist.gov/vuln/detail/CVE-2016-2183) |
| **Solución** | Reconfigura la aplicación afectada para evitar el uso de cifrados de fuerza media. |

|  | Vulnerabilidad 5 |
| :---- | :---- |
| **Nombre** | SSH Terrapin Prefix Truncation Weakness (CVE-2023-48795) |
| **Descripción** | El servidor SSH remoto es vulnerable a la debilidad Terrapin, que permite a un atacante man-in-the-middle omitir verificaciones de integridad y debilitar la seguridad de la conexión. Este análisis solo detecta servidores SSH que usan ChaCha20-Poly1305 o CBC con Encrypt-then-MAC sin medidas estrictas de intercambio de claves, pero no verifica versiones específicas del software. |
| **Severidad** | Media |
| **CVSS** | 5.9 |
| **CVE/CWE** | [CVE-2023-48795](https://nvd.nist.gov/vuln/detail/CVE-2023-48795) |
| **Solución** | Contacta al proveedor para obtener una actualización con las contramedidas estrictas de intercambio de claves o desactiva los algoritmos afectados. |

|  | Vulnerabilidad 6 |
| :---- | :---- |
| **Nombre** | Apache Multiviews Arbitrary Directory Listing |
| **Descripción** | El servidor web Apache en el host remoto está afectado por una vulnerabilidad de divulgación de información. Un atacante remoto no autenticado puede explotarla enviando una solicitud manipulada para mostrar el contenido de un directorio, incluso si existe un archivo índice válido en dicho directorio. |
| **Severidad** | Media |
| **CVSS** | 5.3 |
| **CVE/CWE** | [CVE-2001-0731](https://nvd.nist.gov/vuln/detail/CVE-2001-0731) |
| **Solución** | Actualiza a la versión 1.3.22 o posterior de Apache. Como solución alternativa, desactiva la opción Multiviews. |

|  | Vulnerabilidad 7 |
| :---- | :---- |
| **Nombre** | SMB Signing not required |
| **Descripción** | La firma no está habilitada en el servidor SMB remoto. Un atacante remoto no autenticado puede aprovechar esta vulnerabilidad para realizar ataques man-in-the-middle contra el servidor SMB. |
| **Severidad** | Media |
| **CVSS** | 5.3 |
| **CVE/CWE** | [CVE-2023-27354](https://nvd.nist.gov/vuln/detail/CVE-2023-27354) |
| **Solución** | Habilita la firma de mensajes en la configuración del host. En Windows, esto se encuentra en la opción de política 'Microsoft network server: Digitally sign communications (always)'. En Samba, la configuración se llama 'server signing'. Consulta los enlaces "ver también" para más detalles. |

|  | Vulnerabilidad 8 |
| :---- | :---- |
| **Nombre** | IP Forwarding Enabled |
| **Descripción** | El host remoto tiene habilitado el reenvío de IP. Un atacante puede explotar esto para enrutar paquetes a través del host y, potencialmente, eludir algunos filtros de cortafuegos, enrutadores o NAC. |
| **Severidad** | Media |
| **CVSS** | 6.5 |
| **CVE/CWE** | [CVE-1999-0511](https://nvd.nist.gov/vuln/detail/CVE-1999-0511) |
| **Solución** | En Linux, puedes deshabilitar el reenvío de IP ejecutando el siguiente comando: echo 0 \> /proc/sys/net/ipv4/ip\_forward |

Informe completo generado por Nessus: [Anexo](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_NESSUS/Nessus_Ubuntu.pdf)

### **Windows Server 2008**

En el escaneo del servidor Windows con **Nessus** obtuvimos los siguientes resultados globales.​

Aquí se muestran algunas de las vulnerabilidades detectadas:​

|  | Vulnerabilidad 1 |
| :---- | :---- |
| **Nombre** | MS11-030: Vulnerability in DNS Resolution Could Allow Remote Code Execution |
| **Descripción** | Un fallo en la forma en que el cliente DNS de Windows instalado procesa las consultas de resolución de nombres multicast de enlace local (LLMNR) puede ser explotado para ejecutar código arbitrario en el contexto de la cuenta NetworkService. |
| **Severidad** | Crítico |
| **CVSS** | 10 |
| **CVE/CWE** | [CVE-2011-0657](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-0657) |
| **Solución** | Microsoft ha publicado un conjunto de parches para Windows XP, 2003, Vista, 2008, 7 y 2008 R2. |

|  | Vulnerabilidad 2 |
| :---- | :---- |
| **Nombre** | Microsoft RDP RCE |
| **Descripción** | El host remoto está afectado por una vulnerabilidad de ejecución remota de código en el Protocolo de Escritorio Remoto (RDP). Un atacante remoto no autenticado puede explotarla mediante una serie de solicitudes especialmente diseñadas para ejecutar código arbitrario. |
| **Severidad** | Crítico |
| **CVSS** | 9.4 |
| **CVE/CWE** | [CVE-2019-0708](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2019-0708) |
| **Solución** | Microsoft ha publicado un conjunto de parches para Windows XP, 2003, Vista, 2008, 7 y 2008 R2. |

|  | Vulnerabilidad 3 |
| :---- | :---- |
| **Nombre** | Apache Tomcat AJP Connector Request Injection |
| **Descripción** | Se ha encontrado una vulnerabilidad de lectura/inclusión de archivos en el conector AJP. Un atacante remoto no autenticado podría explotarla para leer archivos de aplicaciones web desde un servidor vulnerable. En los casos en que el servidor vulnerable permita la carga de archivos, un atacante podría subir código malicioso en JavaServer Pages (JSP) dentro de distintos tipos de archivos y lograr la ejecución remota de código (RCE). |
| **Severidad** | Crítico |
| **CVSS** | 9.8 |
| **CVE/CWE** | [CVE-2020-1938](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2020-1938) ,  [CVE-2020-1745](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2020-1745) |
| **Solución** | Actualice la configuración de AJP para requerir autorización y/o actualice el servidor Tomcat a la versión 7.0.100, 8.5.51, 9.0.31 o una posterior. |

|  | Vulnerabilidad 4 |
| :---- | :---- |
| **Nombre** | MS12-020: Vulnerabilities in Remote Desktop Could Allow Remote Code Execution |
| **Descripción** | Existe una vulnerabilidad de ejecución remota de código arbitrario en la implementación del Protocolo de Escritorio Remoto (RDP) en el host de Windows remoto. La vulnerabilidad se debe a la forma en que RDP accede a un objeto en memoria que no ha sido inicializado correctamente o que ha sido eliminado. Si RDP está habilitado en el sistema afectado, un atacante remoto no autenticado podría aprovechar esta vulnerabilidad para ejecutar código arbitrario enviando una secuencia de paquetes RDP especialmente diseñados. |
| **Severidad** | Alto |
| **CVSS** | 9.3 |
| **CVE/CWE** | [CVE-2012-0152](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2012-0152) ,  [CVE-2012-0002](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2012-0002) |
| **Solución** | Microsoft ha publicado un conjunto de parches para Windows XP, 2003, Vista, 2008, 7 y 2008 R2. |

|  | Vulnerabilidad 5 |
| :---- | :---- |
| **Nombre** | MS14-066: Vulnerability in Schannel Could Allow Remote Code Execution |
| **Descripción** | El host de Windows remoto está afectado por una vulnerabilidad de ejecución remota de código debido a un procesamiento inadecuado de paquetes por parte del paquete de seguridad Secure Channel (Schannel). Un atacante puede explotar esta vulnerabilidad enviando paquetes especialmente diseñados a un servidor Windows. |
| **Severidad** | Alto |
| **CVSS** | 8.8 |
| **CVE/CWE** | [CVE-2014-6321](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6321) |
| **Solución** | Microsoft ha publicado un conjunto de parches para Windows XP, 2003, Vista, 2008, 7 y 2008 R2. |

|  | Vulnerabilidad 6 |
| :---- | :---- |
| **Nombre** | SSL Self-Signed Certificate |
| **Descripción** | La cadena de certificados X.509 de este servicio no está firmada por una autoridad de certificación reconocida. Si el host remoto es un servidor público en producción, esto anula el uso de SSL, ya que cualquier persona podría llevar a cabo un ataque de intermediario (man-in-the-middle) contra el host remoto. |
| **Severidad** | Media |
| **CVSS** | 6.4 |
| **CVE/CWE** | [CVE-2018-5466](https://nvd.nist.gov/vuln/detail/cve-2018-5466) |
| **Solución** | Adquiera o genere un certificado SSL válido para este servicio. |

|  | Vulnerabilidad 7 |
| :---- | :---- |
| **Nombre** | ManageEngine Desktop Central 9 \< Build 92027 |
| **Descripción** | La aplicación ManageEngine Desktop Central que se ejecuta en el host remoto es de la versión 9 anterior a la construcción 92027\. Por lo tanto, está afectada por varias vulnerabilidades, incluyendo una de ejecución remota de código y tres vulnerabilidades de cross-site scripting (XSS). |
| **Severidad** | Media |
| **CVSS** | 6.1 |
| **CVE/CWE** | [CVE-2018-8722](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2018-8722) |
| **Solución** | Actualice a la versión 9 de ManageEngine Desktop Central, construcción 92027 o posterior. |

Informe completo generado por Nessus: [Anexo](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_NESSUS/Nessus_Windows_Server.pdf)

## **OpenVAS**

### **Ubuntu Server 14.04**

En el escaneo del servidor Ubuntu con **OpenVAS** obtuvimos los siguientes resultados globales.​

### **Vulnerabilidades críticas**

| Puerto | Nivel | Vulnerabilidad |
| :---- | :---- | :---- |
| 80/tcp | Critical | Drupal Coder RCE Vulnerability (SA-CONTRIB-2016-039) |
| 22/tcp | Critical | SSH Brute Force Logins With Default Credentials |
| 21/tcp | Critical | ProFTPD 'mod\_copy' Unauthenticated Copying Of Files |

Aquí se muestran algunas de las vulnerabilidades críticas detectadas:​

| Campo | Información |
| :---- | :---- |
| **Severidad** | Critical (CVSS: 10.0) |
| **Vulnerabilidad** | Drupal Coder RCE Vulnerability (SA-CONTRIB-2016-039) \- Active Check |
| **URL Vulnerable** | [http://192.168.1.166/drupal/sites/all/modules/coder/coder\_upgrade/scripts/coder\_upgrade.run.php](http://192.168.1.166/drupal/sites/all/modules/coder/coder_upgrade/scripts/coder_upgrade.run.php) |
| **Descripción** | El módulo Coder no valida suficientemente las entradas de usuario en un archivo script con extensión php. Un atacante malintencionado no autenticado puede realizar peticiones directamente a este archivo para ejecutar código php arbitrario. |
| **Impacto** | Bajo ciertas circunstancias podría resultar en ejecución remota de código. |
| **Solución** | Instalar la última versión del módulo. |
| **Calidad de Detección** | 95% |
| **CVE** | N/A (SA-CONTRIB-2016-039) |
| **Referencia** | [https://www.drupal.org/node/2765575](https://www.drupal.org/node/2765575) |

| Campo | Información |
| :---- | :---- |
| **Severidad** | Critical (CVSS: 9.8) |
| **Vulnerabilidad** | SSH Brute Force Logins With Default Credentials Reporting |
| **Credenciales Comprometidas** | vagrant:vagrant |
| **Descripción** | Es posible iniciar sesión en el servidor SSH remoto usando credenciales por defecto. |
| **Impacto** | Este problema puede ser explotado por un atacante remoto para obtener acceso a información sensible o modificar la configuración del sistema. |
| **Solución** | Cambiar la contraseña lo antes posible. |
| **Calidad de Detección** | 95% |
| **CVE Relacionados** | CVE-2017-16523, CVE-2020-29583, CVE-2021-27797, CVE-2023-1944, CVE-2024-22902, CVE-2025-12592, entre otros |
| **Referencia CISA** | Known Exploited Vulnerability (KEV) catalog |

| Campo | Información |
| :---- | :---- |
| **Severidad** | Critical (CVSS: 10.0) |
| **Vulnerabilidad** | ProFTPD 'mod\_copy' Unauthenticated Copying Of Files Via SITE CPFR/CPTO Vulnerability |
| **Descripción** | ProFTPD es vulnerable a copia no autenticada de archivos. El módulo mod\_copy permite copiar archivos usando los comandos SITE CPFR/CPTO sin autenticación. |
| **Resultado de Detección** | El objetivo fue encontrado vulnerable |
| **Impacto** | Bajo ciertas circunstancias esto podría resultar en ejecución remota de código. |
| **Método de Detección** | Intentó copiar /etc/passwd a /tmp/passwd.copy usando comandos SITE CPFR/CPTO. |
| **Solución** | Solicitar actualización al fabricante. |
| **Calidad de Detección** | 99% |
| **CVE** | CVE-2015-3306 |
| **Referencia** | [http://bugs.proftpd.org/show\_bug.cgi?id=4169](http://bugs.proftpd.org/show_bug.cgi?id=4169) |

EL informe completo generado por OpenVAS está aquí: [Anexo](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_OPENVAS/report-Ubuntu-Server.pdf)

### **Windows Server 2008**

En el escaneo del servidor Windows con **OpenVAS** obtuvimos los siguientes resultados globales.​

| Host | Críticas | Altas | Medias | Bajas |
| :---- | :---- | :---- | :---- | :---- |
| 192.168.1.207 | 17 | 47 | 134 | 12 |

#### **Vulnerabilidades críticas por puerto**

| Puerto / Servicio | Severidad | Vulnerabilidad |
| :---- | :---- | :---- |
| 8009/tcp | Critical (CVSS 9.8) | Apache Tomcat AJP RCE Vulnerability (Ghostcat) |
| 8282/tcp | Critical (CVSS 10.0) | Apache Tomcat End of Life (EOL) Detection – Windows |
| 8282/tcp | Critical (CVSS 9.8) | Apache Tomcat Rewrite Rule Bypass Vulnerability (Apr 2025\) – Windows |
| 8282/tcp | Critical (CVSS 9.8) | Apache Tomcat RCE Vulnerability (Mar 2025\) – Windows |
| 8282/tcp | Critical (CVSS 9.1) | Apache Tomcat Security Bypass and Information Disclosure Vulnerabilities – Windows |
| 8282/tcp | Critical (CVSS 9.1) | Apache Tomcat ‘SecurityManager’ Information Disclosure Vulnerability (Apr 2017\) – Windows |
| 3306/tcp | Critical (CVSS 9.8) | Oracle MySQL Server ≤ 5.7.41, 8.x ≤ 8.0.31 Security Update (cpuapr2023) – Windows (InnoDB / zlib) |
| 3306/tcp | Critical (CVSS 9.8) | Oracle MySQL Server ≤ 5.7.43, 8.x ≤ 8.0.34, 8.1.0 Security Update (cpuoct2023) – Windows |
| 3306/tcp | Critical (CVSS 9.8) | Oracle MySQL Server ≤ 5.7.35 / 8.0 ≤ 8.0.26 Security Update (cpuoct2021) – Windows |
| 3306/tcp | Critical (CVSS 9.8) | Oracle MySQL Server ≤ 5.7.40, 8.x ≤ 8.0.31 Security Update (cpujan2023) – Windows (libcurl) |
| 3306/tcp | Critical (CVSS 9.8) | Oracle MySQL Server ≤ 5.5.52 / 5.6 ≤ 5.6.33 / 5.7 ≤ 5.7.15 Security Update (cpuoct2016) – Windows |
| 3306/tcp | Critical (CVSS 9.8) | Oracle MySQL Security Update (cpuoct2018 – 02\) – Windows |
| 3306/tcp | Critical (CVSS 9.0) | Oracle MySQL Server Multiple Vulnerabilities – 01 (Nov 2012\) – Windows |
| 9200/tcp | Critical (CVSS 10.0) | Elasticsearch End of Life (EOL) Detection |
| 9200/tcp | Critical (CVSS 9.8) | Elasticsearch \< 1.6.1 Multiple Vulnerabilities – Windows |
| 22/tcp | Critical (CVSS 9.8) | OpenSSH \< 7.2 X11 Forwarding Security Bypass Vulnerability – Windows |
| general/tcp | Critical (CVSS 10.0) | Operating System (OS) End of Life (EOL) Detection – Windows Server 2008 R2 SP1 |

Aquí se muestran algunas de las vulnerabilidades detectadas:​

#### **Apache Tomcat AJP RCE (Ghostcat) \- 8009/tcp**

| Campo | Información |
| :---- | :---- |
| Puerto | 8009/tcp |
| Severidad | Critical (CVSS 9.8) |
| Producto | Apache Tomcat AJP Connector |
| Evidencia | Lectura remota de /WEB-INF/web.xml vía AJP |
| Riesgo | RCE / lectura de ficheros de configuración y código |
| Solución | Actualizar Tomcat a 7.0.100, 8.5.51, 9.0.31 o superior |

#### **Apache Tomcat EOL – 8282/tcp**

| Campo | Información |
| :---- | :---- |
| Puerto | 8282/tcp |
| Severidad | Critical (CVSS 10.0) |
| Versión | Apache Tomcat 8.0.33 (rama 8.0 EOL) |
| EOL | 2018-06-30 |
| Riesgo | Sin parches de seguridad; múltiples CVEs activos |
| Solución | Migrar a versión soportada (rama 9.x/10.x/11.x) |

#### **Apache Tomcat RCE/Bypass (consolidadas) – 8282/tcp**

| Campo | Información |
| :---- | :---- |
| Puerto | 8282/tcp |
| Severidades críticas | CVSS 9.8 / 9.1 |
| Vulnerabilidades clave | Rewrite Rule Bypass (CVE-2025-31651), RCE parcial PUT (CVE-2025-24813), múltiples bypass/Info Disclosure 2016–2017 |
| Versión detectada | 8.0.33 |
| Solución | Actualizar a ≥ 9.0.107 / 10.1.x / 11.x según cada aviso |

#### **Elasticsearch críticas – 9200/tcp**

| Campo | Información |
| :---- | :---- |
| Puerto | 9200/tcp |
| Severidad | Critical (CVSS 10.0 / 9.8) |
| Versión | Elasticsearch 1.1.1 (EOL) |
| Fallos | EOL \+ CVE‑2015‑5531 / CVE‑2015‑5377 (RCE/lectura de ficheros, DoS) |
| Solución | Actualizar a rama 7.x/8.x soportada; mínimo ≥ 6.8.17 según avisos |

#### **OpenSSH crítico – 22/tcp**

| Campo | Información |
| :---- | :---- |
| Host | 192.168.1.207 |
| SO | Windows Server 2008 R2 SP1 |
| Severidad | Critical (CVSS 10.0) |
| Estado | Fin de vida desde 2020-01-14 (sin parches) |
| Solución | Migrar a versión soportada o usar ESU/terceros y documentar excepción |

EL informe completo generado por OpenVAS está aquí: [Anexo](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_OPENVAS/report-Windows-Server08.pdf)

# **Conclusión**

El análisis de caja negra ha permitido identificar vulnerabilidades críticas que exponen los sistemas de SecureLogistics a amenazas reales. Se han detectado fallos en servicios como Apache Tomcat y ProFTPD, además de configuraciones inseguras en cifrados SSL/TLS que facilitan ataques de intercepción y ejecución remota de código. En el servidor Windows Server 2008, las vulnerabilidades en RDP y Schannel pueden ser explotadas para comprometer la integridad del sistema.​

# **Recomendaciones**

Para mitigar los riesgos identificados es necesario aplicar medidas correctivas que reduzcan la superficie de ataque. La actualización de software y aplicación de parches debe ejecutarse de inmediato, priorizando los servicios más expuestos. También se requiere reforzar la configuración de seguridad eliminando cifrados inseguros y mejorando las políticas de acceso en SSH y SMB.​

El monitoreo continuo y las auditorías de seguridad periódicas permitirán detectar nuevas amenazas a tiempo y prevenir incidentes graves. El establecimiento de controles de acceso basados en el principio de mínimo privilegio reducirá la exposición ante accesos no autorizados.

Por último, se recomienda capacitar al personal en ciberseguridad para minimizar el riesgo de ataques internos y externos. La implementación de estas medidas fortalecerá significativamente la seguridad de la empresa, reduciendo la probabilidad de incidentes que puedan comprometer la continuidad del negocio y la integridad de los datos.

# **Anexos**

[Informe OpenVAS Ubuntu](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_OPENVAS/report-Ubuntu-Server.pdf)  
[Informe OpenVAS Windows Server](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_OPENVAS/report-Windows-Server08.pdf)  
[Informe Nessus Ubuntu](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_NESSUS/Nessus_Ubuntu.pdf)  
[Informe Nessus Windows](https://github.com/IES-Rafael-Alberti/25-26-ciberseguridad-grupo-3/blob/main/Hacking_etico/Proyecto_04/reportes_NESSUS/Nessus_Windows_Server.pdf)