# Playbook de respuesta a ransomware

## 1. Finalidad

Este playbook define la respuesta específica ante incidentes de ransomware que afecten, o puedan afectar, a la disponibilidad, integridad o confidencialidad de la información corporativa. Su objetivo es contener con rapidez la propagación, preservar evidencias, recuperar la operativa desde estados confiables y coordinar la comunicación interna y externa sin improvisación.

Este documento complementa al Plan de Respuesta a Incidentes y debe aplicarse junto con el procedimiento general de clasificación, escalado, documentación y gestión de evidencias. En caso de conflicto entre velocidad de recuperación y preservación de evidencias, la decisión la tomará el responsable del incidente con apoyo de Dirección, TIC y Legal cuando corresponda.

## 2. Alcance

Este playbook aplica a cualquier evento de cifrado malicioso, borrado destructivo simulado como ransomware, extorsión con amenaza de publicación de datos, o actividad preparatoria claramente compatible con ransomware. Se incluye tanto el ransomware ejecutado en un único endpoint como el que afecte a comparticiones, servidores, correo, copias de seguridad, servicios cloud o sistemas de negocio.

En esta organización, los activos prioritarios a proteger durante un incidente de ransomware son el CRM/ERP, los servidores de archivos y aplicaciones, los datos personales de clientes y proveedores, las copias de seguridad, el correo corporativo y los puestos de trabajo con acceso a información sensible.

## 3. Activación

Se activará este playbook ante cualquiera de las siguientes señales:

1. Aparición de notas de rescate, extensiones anómalas o ficheros cifrados.
2. Alertas del EDR o antivirus compatibles con comportamiento de ransomware.
3. Cambios masivos en archivos, borrados, renombrados o corrupción simultánea de datos.
4. Pérdida repentina de acceso a comparticiones, bases de datos o sistemas de negocio por cifrado.
5. Sospecha fundada de exfiltración previa seguida de amenaza de extorsión.
6. Alertas de proveedor, SOC, SIEM o personal TIC sobre ejecución masiva, movimiento lateral o uso de herramientas típicamente asociadas a ransomware.

La severidad inicial recomendada será crítica si el alcance incluye CRM/ERP, servidores, copias de seguridad, múltiples puestos o riesgo de afectación a datos personales. Si el indicio inicial está acotado a un equipo aislado, podrá abrirse como severidad alta o media, pero deberá reevaluarse de inmediato.

## 4. Objetivos de respuesta

Durante las primeras horas, la respuesta deberá perseguir estos objetivos por orden de prioridad:

1. Frenar la propagación hacia sistemas críticos, copias de seguridad y credenciales privilegiadas.
2. Determinar alcance real, vector de entrada y posibles accesos previos del atacante.
3. Preservar evidencias clave para análisis técnico, decisiones legales y mejora posterior.
4. Recuperar la operativa desde estados conocidos y limpios, sin reintroducir la amenaza.
5. Valorar el posible impacto regulatorio si existen datos personales afectados o exfiltrados.

## 5. Roles mínimos

La respuesta mínima ante ransomware requerirá, como poco, la participación coordinada de estas funciones:

| Rol | Función principal en este playbook |
|---|---|
| Responsable del incidente / CISO | Dirige la respuesta, decide prioridades, escala y valida medidas críticas |
| TIC sistemas y endpoints | Aislamiento, análisis técnico, reconstrucción y restauración |
| TIC red y correo | Bloqueos de red, segmentación, revisión de tráfico, acceso remoto y correo |
| Responsables de proceso | Priorización de servicios y validación funcional tras la recuperación |
| Legal / DPO | Evaluación de brecha, obligaciones regulatorias y preservación documental |
| Dirección | Aprobación de decisiones con impacto alto de negocio o comunicación externa |
| Help Desk | Recepción de avisos, soporte a usuarios y ejecución de medidas autorizadas |
| Proveedores críticos | Soporte en EDR, backup, nube, hosting o herramientas afectadas |

## 6. Investigación

La investigación, la contención y la comunicación deben ejecutarse en paralelo. En ransomware, la contención tiene prioridad, pero eso no elimina la necesidad de entender alcance, persistencia y vector de entrada.

### 6.1 Confirmación inicial

En los primeros minutos se comprobará si realmente se está ante un ransomware o ante otro tipo de incidente destructivo. Para ello se revisará:

1. Presencia de notas de rescate, nombres de familia o direcciones de contacto.
2. Extensiones nuevas en ficheros, cambios masivos de nombres o imposibilidad súbita de apertura.
3. Procesos activos o recientes compatibles con cifrado masivo.
4. Alertas del EDR, SIEM, firewall, proxy, DNS o antivirus.
5. Eventos de autenticación anómalos, uso de cuentas privilegiadas o conexiones remotas inusuales.

### 6.2 Preguntas clave

El equipo de investigación deberá responder lo antes posible a estas preguntas:

1. ¿Qué sistemas están afectados realmente y cuáles están todavía sanos?
2. ¿El atacante sigue activo en la red o el impacto ha terminado?
3. ¿Se trata de cifrado únicamente o hay indicios de exfiltración previa?
4. ¿Qué cuentas, grupos o credenciales han sido utilizados?
5. ¿Cuál ha sido el vector inicial: phishing, RDP/VPN, credenciales comprometidas, software vulnerable, movimiento lateral o dispositivo externo?
6. ¿Las copias de seguridad están accesibles, íntegras y libres de compromiso?
7. ¿Qué servicios deben recuperarse primero para mantener la actividad mínima del negocio?

### 6.3 Fuentes de evidencia prioritarias

La investigación se apoyará, como mínimo, en estas fuentes:

1. Consola EDR/antivirus y telemetría de endpoints.
2. Logs de autenticación, Active Directory o directorio equivalente.
3. Logs de VPN, firewall, proxy, DNS e IDS/IPS.
4. Registros de correo y pasarela antiphishing si existe.
5. Registros de servidores de archivos, bases de datos, aplicaciones y CRM/ERP.
6. Telemetría de copias de seguridad, repositorios y jobs fallidos o borrados.
7. Evidencias del proveedor cloud o SaaS cuando el incidente afecte a servicios externos.

### 6.4 Artefactos a recoger

Siempre que el impacto lo permita, se recogerán antes de reconstruir los sistemas estos artefactos:

1. Nombre del host, usuario afectado, IP, hora de detección y responsable del equipo.
2. Procesos en ejecución, conexiones de red, tareas programadas y mecanismos de persistencia.
3. Hashes, binarios sospechosos, scripts, herramientas de administración remota y archivos temporales.
4. Eventos de seguridad, inicio de sesión, creación de servicios, ejecución de PowerShell o cmd y movimientos laterales.
5. Notas de rescate, capturas de pantalla y ejemplos de archivos cifrados.
6. Exportación de eventos del EDR o SIEM relacionados con la cadena de ataque.
7. Evidencias de manipulación de backups, borrado de snapshots o cambios de políticas de retención.

### 6.5 Evaluación del alcance

La delimitación del alcance se hará por capas.

Primero, endpoints y servidores con cifrado confirmado. Segundo, sistemas con actividad previa del atacante aunque aún no estén cifrados. Tercero, activos críticos expuestos al mismo vector o a las mismas credenciales. Cuarto, repositorios de backup, almacenamiento cloud, correo y accesos remotos. El objetivo no es solo contar equipos cifrados, sino identificar el perímetro completo del compromiso.

### 6.6 Evaluación de impacto

La evaluación de impacto incluirá al menos estos elementos:

1. Servicios interrumpidos y duración estimada.
2. Datos inaccesibles, alterados o potencialmente exfiltrados.
3. Departamentos afectados y procesos detenidos.
4. Riesgo para clientes, proveedores y operaciones online.
5. Afectación a obligaciones de protección de datos.
6. Estado real de las copias de seguridad y viabilidad de restauración.

## 7. Contención

La contención es la fase más urgente en ransomware. Debe ejecutarse con decisión y de forma amplia, porque un aislamiento parcial suele permitir reinfección o expansión.

### 7.1 Medidas inmediatas

Ante confirmación o sospecha fuerte de ransomware se ordenará, según el alcance:

1. Aislar de red los endpoints o servidores afectados, preferiblemente mediante EDR o desconexión lógica controlada.
2. Bloquear temporalmente comparticiones, unidades de red o accesos a repositorios comunes cuando exista riesgo de propagación.
3. Deshabilitar o limitar cuentas comprometidas, especialmente administrativas, de servicio o con acceso a múltiples sistemas.
4. Revocar sesiones activas, accesos VPN, accesos remotos y tokens donde existan indicios de compromiso.
5. Proteger las copias de seguridad, desconectando o endureciendo el acceso a repositorios si fuera necesario.
6. Bloquear IOC de red y host ya validados: dominios, IPs, hashes, URLs, binarios o reglas maliciosas.
7. Suspender cambios no esenciales en sistemas críticos durante la respuesta.

### 7.2 Aislamiento por prioridad

Si el aislamiento total no puede hacerse de una vez, se priorizará en este orden:

1. Sistemas críticos aún no cifrados.
2. Repositorios de backup y servicios de recuperación.
3. Cuentas privilegiadas y accesos remotos.
4. Servidores con conectividad transversal.
5. Endpoints de usuarios con alto nivel de acceso a comparticiones o datos sensibles.

### 7.3 Medidas complementarias

En función de la investigación podrán adoptarse además estas acciones:

1. Purga de correos maliciosos si el vector fue phishing.
2. Deshabilitación temporal de RDP, SMB, PSExec, herramientas remotas o protocolos abusados.
3. Segmentación de emergencia entre departamentos o subredes.
4. Incremento del nivel de alerta en SIEM, EDR y firewall para detectar reinfección.
5. Coordinación inmediata con proveedores si hay infraestructura alojada externamente.

### 7.4 Lo que no debe hacerse

Durante la contención no se debe:

1. Apagar masivamente sistemas sin criterio cuando puedan perderse evidencias útiles.
2. Restaurar de backups sin validar que estén limpios.
3. Reutilizar credenciales que pudieran estar comprometidas.
4. Comunicar causas o alcance como hechos cerrados antes de confirmarlos.
5. Negociar o responder al atacante sin decisión formal de Dirección y asesoramiento legal.

## 8. Erradicación

La erradicación comenzará cuando el alcance esté razonablemente entendido y la propagación esté controlada. El objetivo es eliminar persistencia, accesos y causas técnicas, no solo volver a poner equipos en marcha.

### 8.1 Acciones técnicas

Las acciones de erradicación incluirán según el caso:

1. Reinstalación o reconstrucción de sistemas afectados desde medios o imágenes confiables.
2. Eliminación de servicios maliciosos, tareas programadas, scripts, claves de registro y persistencias detectadas.
3. Aplicación de parches al sistema operativo, software expuesto, VPN, correo o aplicaciones vulnerables.
4. Rotación completa de contraseñas afectadas y de cuentas privilegiadas, de servicio y administrativas.
5. Renovación de secretos, claves API, certificados o tokens si existe sospecha de exposición.
6. Revisión de reglas de correo, delegaciones, reenvíos y accesos sospechosos en buzones comprometidos.
7. Cierre del vector de entrada validado o más probable.

### 8.2 Tratamiento del vector inicial

La erradicación no se considerará completa sin actuar sobre el origen. Como guía:

1. Si el vector fue phishing, deberán sanearse buzones, dominios bloqueados, reglas y credenciales, además de revisar otros receptores del mismo mensaje.
2. Si el vector fue acceso remoto, deberán cerrarse accesos expuestos, reforzar MFA, limitar orígenes y revisar logs históricos.
3. Si el vector fue software vulnerable, deberá parchearse o retirarse el componente y comprobar otros sistemas con la misma exposición.
4. Si hubo movimiento lateral, deberán revisarse privilegios, segmentación, cuentas compartidas y administración remota.

### 8.3 Validación previa a recuperación

Antes de pasar a restauración o reincorporación de sistemas, TIC y el responsable del incidente validarán que:

1. No existan IOC activos en los sistemas pendientes de recuperar.
2. Las cuentas críticas ya hayan sido rotadas.
3. El vector de entrada esté corregido o mitigado.
4. Exista una estrategia de monitorización reforzada para los activos que vuelvan a producción.

## 9. Recuperación

La recuperación deberá ser ordenada, priorizada y siempre basada en estados limpios. En ransomware, recuperar deprisa pero mal suele provocar recaída.

### 9.1 Orden recomendado de recuperación

En esta organización, salvo decisión operativa distinta de Dirección, se propone este orden de recuperación:

1. Infraestructura mínima necesaria para autenticación, red y administración segura.
2. CRM/ERP y servicios que soportan facturación, atención y procesos de negocio esenciales.
3. Servidores de archivos y aplicaciones críticas.
4. Correo corporativo y servicios de colaboración.
5. Puestos de trabajo prioritarios por función.
6. Web corporativa y tienda online, si no estaban afectadas o una vez asegurado el núcleo operativo.

### 9.2 Reglas de restauración

Toda restauración deberá cumplir estas reglas:

1. Solo se restaurará desde copias o snapshots verificados como limpios.
2. La restauración se hará sobre sistemas reconstruidos o validados, no sobre sistemas dudosos sin saneamiento previo.
3. Cada servicio recuperado deberá pasar validación funcional por su responsable de proceso.
4. Tras la puesta en marcha se activará vigilancia reforzada de logs, EDR, autenticación y tráfico de red.

### 9.3 Criterios de éxito

Se considerará recuperado un servicio cuando:

1. Esté operativo para el negocio.
2. No presente IOC activos ni síntomas de cifrado o manipulación.
3. Sus cuentas asociadas estén saneadas.
4. Exista trazabilidad de lo restaurado, desde qué copia y a qué hora.

## 10. Comunicación

La comunicación debe ser rápida, precisa y controlada. En incidentes de ransomware, el daño reputacional crece cuando la organización comunica tarde o de forma contradictoria.

### 10.1 Comunicación interna

Durante la fase activa se realizarán comunicaciones diferenciadas.

Dirección recibirá resúmenes ejecutivos con impacto, estado, decisiones pendientes, riesgo regulatorio y previsión de recuperación. Los equipos técnicos recibirán instrucciones operativas concretas. Los usuarios afectados recibirán mensajes claros sobre indisponibilidad, cambios de credenciales, uso de canales alternativos y prohibiciones temporales.

### 10.2 Comunicación a usuarios

Las instrucciones mínimas para usuarios, cuando proceda, serán:

1. No encender, apagar ni reconectar equipos afectados sin instrucción de TIC.
2. No abrir notas de rescate, adjuntos ni archivos sospechosos adicionales.
3. No usar unidades compartidas o accesos remotos temporalmente bloqueados.
4. Cambiar contraseña cuando se les indique y confirmar recepción de la instrucción.
5. Informar de cualquier síntoma similar en otros equipos o cuentas.

### 10.3 Comunicación externa

Si el incidente afecta a clientes, proveedores o servicios visibles, la comunicación externa deberá validarse por Dirección y Legal. No se confirmará exfiltración ni brecha de datos personales sin evaluación razonada, pero tampoco se retrasará indebidamente una notificación obligatoria.

### 10.4 Notificación regulatoria

Si existen datos personales potencialmente afectados, Legal y el DPO valorarán si procede notificar a la autoridad de control y a los afectados. La evaluación considerará disponibilidad, acceso no autorizado, posible exfiltración, categorías de datos y riesgo para las personas.

## 11. Decisión sobre el pago

La organización no adoptará ninguna decisión sobre pago o negociación sin intervención expresa de Dirección, Legal y, en su caso, asesoramiento externo especializado. El mero hecho de disponer de una vía de pago o de una herramienta de descifrado ofrecida por el atacante no constituye garantía de recuperación, confidencialidad ni no repetición.

Cualquier deliberación sobre pago, contacto con el atacante o uso de intermediarios deberá quedar documentada en el expediente del incidente.

## 12. Recursos mínimos necesarios

Para ejecutar este playbook se consideran necesarios, como mínimo, los siguientes recursos:

1. Consola EDR o herramienta equivalente con capacidad de aislamiento.
2. Acceso a logs de red, autenticación, correo y sistemas críticos.
3. Inventario de activos, responsables y priorización de servicios.
4. Copias de seguridad verificadas y procedimiento de restauración.
5. Repositorio seguro para evidencias y cronología.
6. Capacidad de comunicación alternativa si el correo está afectado.
7. Contactos de proveedores críticos, Legal, DPO y Dirección.

## 13. Cierre y lecciones aprendidas

El incidente no se cerrará solo porque los sistemas vuelvan a funcionar. Antes del cierre deberán quedar completados, como mínimo, estos puntos:

1. Cronología técnica y ejecutiva del incidente.
2. Vector inicial confirmado o hipótesis más probable con justificación.
3. Relación de sistemas y cuentas afectadas.
4. Evidencias preservadas y ubicación.
5. Impacto real en negocio, datos y tiempos de indisponibilidad.
6. Acciones de contención, erradicación y recuperación ejecutadas.
7. Acciones de mejora obligatorias con responsable y fecha.

### 13.1 Mejoras esperables tras el incidente

En esta organización, un incidente de ransomware deberá traducirse normalmente en mejoras sobre estos frentes:

1. Refuerzo de copias 3-2-1 y pruebas de restauración.
2. Endurecimiento de accesos remotos, MFA y cuentas privilegiadas.
3. Formalización de EDR, listas blancas y capacidades de aislamiento.
4. Revisión de segmentación, comparticiones y permisos.
5. Refuerzo de correo, autenticidad y concienciación frente a phishing.
6. Actualización del inventario, del plan general y de los tiempos de respuesta.

## 14. Guía operativa rápida

Durante la primera hora, la secuencia práctica recomendada será la siguiente:

1. Confirmar indicios y abrir expediente.
2. Clasificar como alta o crítica según alcance inicial.
3. Aislar equipos, cuentas y comparticiones en riesgo.
4. Proteger backups y credenciales privilegiadas.
5. Recoger evidencias mínimas antes de reconstruir.
6. Delimitar alcance real y vector probable.
7. Informar a Dirección, Legal/DPO y responsables de proceso según impacto.
8. Preparar reconstrucción y restauración desde estados limpios.

Este resumen rápido no sustituye al resto del playbook. Su función es ayudar a actuar con orden durante los primeros minutos, cuando la presión operativa es más alta.
