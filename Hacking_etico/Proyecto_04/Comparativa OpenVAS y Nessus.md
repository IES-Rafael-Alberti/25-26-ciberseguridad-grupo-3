# **Comparativa Herramientas OpenVas y Nessus**

## En Windows Server 2008 y Ubuntu Server 14.04

# **Integrantes:**

Ubuntu Server 14.04:

* Jose María Escalón Prada: Nessus  
* [Abel García Domínguez](mailto:agardom573@g.educaand.es): OpenVAS

Windows Server 2008:

* [Daniel Hernández Gómez](mailto:dhergom961@g.educaand.es): Nessus	  
* [David Jiménez Ruiz](mailto:djimrui878@g.educaand.es): OpenVAS

# **1\. Introducción**

En este documento comparamos Nessus y OpenVAS como escáneres de vulnerabilidades, tanto a nivel de enfoque como de resultados prácticos en dos sistemas de prueba. La idea no es “decir cuál es mejor” de forma absoluta, sino aterrizar qué aporta cada uno según el contexto: presupuesto, tiempo, facilidad de uso y profundidad del análisis.​

# **2\. Descripción de las herramientas**

## 

## **2.1. Nessus**

Nessus es una solución desarrollada por Tenable orientada al escaneo de vulnerabilidades en distintos sistemas operativos. A nivel de arquitectura, el análisis lo ejecuta el servicio nessusd, y la gestión/reporting se realiza desde la interfaz web. En la práctica, está pensado para desplegarse rápido, lanzar escaneos y generar informes claros, lo que encaja bien en entornos donde es importante la rapidez y la trazabilidad de los hallazgos y evidencias.​

Existe una versión gratuita limitada (Nessus Essentials) y una versión comercial con funcionalidades avanzadas y soporte. Esto hace que sea una opción típica cuando se necesita estabilidad, actualizaciones continuas y soporte formal, aunque el coste puede ser problemático si el presupuesto es ajustado.​

## **2.2. OpenVAS (GVM)**

OpenVAS es un escáner de código abierto integrado dentro del marco Greenbone Vulnerability Management (GVM). Permite identificar vulnerabilidades, puertos abiertos y problemas de configuración, con bastante margen para ajustar perfiles y comportamiento del escaneo. A cambio, suele requerir más trabajo inicial (puesta a punto, actualización de feeds y ajuste de parámetros) para que la experiencia sea fluida.​

OpenVAS es gratuito y existe una variante empresarial (Greenbone Security Manager) orientada a organizaciones que buscan soporte adicional. En nuestro caso lo tratamos como alternativa realista cuando el coste es una restricción y el equipo es lo bastante técnico como para asumir la configuración, afinado y revisión posterior de resultados.​

# **3\. Resultados de las pruebas**

## **3.1. Ubuntu Server 14.04**

| Impacto | Nessus | OpenVAS |
| :---- | ----: | ----: |
| Crítico | 10 | 3 |
| Alto | 14 | 3 |
| Medio | 20 | 13 |
| Bajo | 7 | 2 |
| Informativo | 69 | 0 |

## 

## **3.2. Windows Server 2008**

| Impacto | Nessus | OpenVAS |
| :---- | ----: | ----: |
| Crítico | 6 | 17 |
| Alto | 9 | 47 |
| Medio | 13 | 134 |
| Bajo | 3 | 12 |
| Informativo | 64 | 0 |

## 

En Ubuntu Server 14.04, Nessus reportó más hallazgos en prácticamente todas las categorías, incluyendo vulnerabilidades críticas (por ejemplo, menciona RCE de Drupal y mod\_copy de ProFTPD), además de aportar contexto de mitigación. En ese mismo escenario, OpenVAS también detectó vulnerabilidades, pero en menor número según los datos que obtuvimos.​

En Windows Server 2008, OpenVAS reportó muchos más “Altos” y “Medios”, pero el propio análisis del equipo ya indica que puede haber repeticiones y falsos positivos, lo que obliga a dedicar tiempo a depurar y priorizar. Nessus devolvió menos findings en ese caso, pero con una clasificación más limpia y con detalles útiles para la remediación (parches disponibles, servicios expuestos).​

# **4\. Fortalezas y limitaciones** 

## 

## **4.1. Nessus**

En esta práctica, Nessus destaca por facilidad de uso: configurar objetivo, lanzar y obtener resultados es rápido. También resalta la parte de reporting, porque genera informes detallados y personalizables (por ejemplo, HTML y PDF), lo que facilita entregar evidencias y justificar decisiones. A nivel de operación, lo hemos tratado como una opción “industrial”: buena compatibilidad, buena experiencia de uso y menor dificultad en general.​

Su limitación principal es el licenciamiento, y creemos que este puede ser el factor decisivo, porque la versión gratuita tiene bastantes restricciones. Además, comparado con OpenVAS en nuestras pruebas, hay escenarios donde reporta menos cantidad total de vulnerabilidades, lo que puede interpretarse como menor cobertura o como una salida más depurada, pero en cualquier caso conviene tenerlo en cuenta.​

## 

## **4.2. OpenVAS**

OpenVAS encaja bien cuando se busca control y personalización, y cuando el equipo tiene perfil técnico para invertir tiempo en ajustar el escaneo y revisar resultados. En nuestro Windows Server 2008, arrojó un volumen muy alto de hallazgos “Altos” y “Medios”, lo que demuestra que puede ser agresivo detectando, aunque luego haya que dedicar tiempo a filtrar. También puede aportar más detalle técnico en ciertos hallazgos, especialmente si se plantea un enfoque más “auditoría” que “check rápido”.​

Su punto débil, según lo observado, es que un mayor número de findings puede venir acompañado de más falsos positivos y de una experiencia menos cómoda si se necesita presentar resultados agrupados y claros. Además, en la práctica suele requerir más trabajo de mantenimiento (feeds/actualizaciones) y puede consumir más recursos, lo que se nota si el entorno es limitado.​

# **5\. Conclusión**

En base a los resultados obtenidos, Nessus gana por rapidez, usabilidad, facilidad de instalación e informes listos para explotar, con el coste como principal problema. OpenVAS es una alternativa buena si el presupuesto manda y se asume el esfuerzo extra de configuración y validación, a cambio de un mayor volumen de detecciones en algunos escenarios. 

La elección final depende del contexto: si buscamos operativa e informes “para entregar”, Nessus es más directo; si buscamos flexibilidad con coste cero y podemos dedicar tiempo a depurar resultados, OpenVAS es viable.​