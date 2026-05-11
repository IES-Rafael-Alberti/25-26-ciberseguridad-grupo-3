# Plan de Respuesta a Incidentes de Seguridad de la Información para la Empresa de Asesoría para Autónomos y PYMES

Autor: Equipo de Seguridad / Dirección TIC  
Revisión 1.0, Publicado 2026-05-11  
Fue revisado por última vez el 2026-05-11. Fue probado por última vez en simulacro interno anual.

Este plan establece el marco operativo para detectar, evaluar, contener, erradicar, recuperar y cerrar incidentes de seguridad de la información en la organización. Su finalidad es reducir el impacto técnico, operativo, económico, legal y reputacional de los incidentes, asegurando una respuesta coordinada, documentada y proporcional al riesgo.

El plan se alinea con la situación descrita en el Plan Director de Seguridad de la empresa, especialmente con la criticidad del CRM/ERP, los servidores de archivos y aplicaciones, los datos personales de clientes y proveedores, la página web y tienda online, el correo corporativo y las copias de seguridad. También se alinea con los objetivos de continuidad, cumplimiento, fortalecimiento de accesos, recuperación ante desastres y madurez organizativa.

Aplica a las dos sedes de la organización, al personal interno, a personal externo con acceso a sistemas corporativos y a proveedores que gestionen o procesen información de la empresa. Cubre sistemas on-premise, servicios en la nube, endpoints, infraestructura de red, correo electrónico, CRM/ERP, servidores, copias de seguridad, web corporativa, tienda online y cualquier repositorio de información de negocio.

# Evaluar

1. Mantenga la calma y la profesionalidad.
2. Reúna la información pertinente: alarmas, eventos, logs, avisos de usuario, datos, suposiciones razonables e intuiciones técnicas.
3. Considere las categorías de impacto y determine si existe un posible incidente.
4. Inicie una respuesta si hay un incidente o si existe sospecha razonable con potencial impacto real. En caso de duda, inicie respuesta y ajuste después la clasificación.

## Evaluar el impacto funcional

¿Cuál es el impacto directo o probable en la misión de la organización, sus operaciones, empleados, clientes, usuarios o proveedores?

- Degradación o interrupción de CRM/ERP, correo, web/tienda online, servidores de archivos, acceso remoto o cualquier servicio crítico: incidente.
- Afectación limitada pero real a usuarios, departamentos o procesos de negocio: incidente.
- Sin impacto funcional apreciable: continúe evaluando el impacto de la información.

## Evaluar el impacto de la información

¿Cuál es el impacto directo o probable en la información, especialmente en los datos sensibles o regulados?

- Acceso no autorizado, toma, modificación, cifrado, borrado, exposición o pérdida de datos: incidente.
- Sospecha razonable de afectación a datos personales, financieros, jurídicos o de negocio: incidente.
- Sin afectación a la información y sin indicios de compromiso: tratar por soporte ordinario o seguimiento técnico.

**Cada miembro del equipo está facultado para iniciar este proceso.** Si ves algo, di algo.

## Matriz transversal de severidad y escalado

La severidad de cada incidente se clasificará usando dos ejes comunes para toda la organización: impacto funcional sobre la operación e impacto sobre la información. La clasificación se aplicará a todos los activos incluidos en el alcance del plan, con especial atención a CRM/ERP, servidores de archivos y aplicaciones, datos personales, web/tienda online, correo corporativo y copias de seguridad.

### Niveles de severidad

| Nivel | Criterios de clasificación | Ejemplos orientativos | Respuesta mínima obligatoria | Escalado mínimo |
|---|---|---|---|---|
| S1 - Baja | Evento con impacto nulo o muy limitado, sin evidencia de compromiso real, sin afectación a activos críticos y sin acceso confirmado a información sensible | Phishing reportado sin interacción, malware bloqueado sin ejecución, intento fallido de acceso, alerta aislada sin confirmación | Registro del caso, validación técnica, seguimiento por TIC o seguridad, cierre documentado si se descarta incidente | Escalado al responsable técnico del área; no requiere elevar a Dirección salvo recurrencia o patrón anómalo |
| S2 - Media | Incidente confirmado pero contenido, con impacto limitado en un único usuario, equipo o servicio no crítico, sin interrupción grave del negocio y sin indicios de brecha masiva de datos | Compromiso de una cuenta estándar sin privilegios, infección contenida en un puesto, caída parcial de un servicio interno no crítico, borrado accidental recuperable | Activación formal del expediente, asignación de responsable del incidente, investigación, contención y comunicación interna a los responsables afectados | Escalado al responsable del incidente, TIC implicado y propietario del sistema o servicio |
| S3 - Alta | Incidente con afectación relevante a un servicio importante, a varios equipos o a datos sensibles, o con riesgo claro de expansión, fraude, movimiento lateral o impacto reputacional | Compromiso de correo corporativo, acceso no autorizado a datos personales, afectación parcial de CRM/ERP, defacement acotado, ransomware limitado pero confirmado | Activación completa del equipo de respuesta, apertura de canales de coordinación, investigación y remediación en paralelo, valoración legal y revisión de necesidad de notificación externa | Escalado a Responsable de Seguridad, Dirección operativa, Legal/DPO si hay datos personales y proveedores críticos si el incidente afecta a servicios externalizados |
| S4 - Crítica | Incidente con impacto grave o inminente sobre la continuidad del negocio, activos críticos, múltiples sistemas, privilegios elevados, copias de seguridad, o con brecha relevante de datos y posible obligación regulatoria | Ransomware en varios sistemas, compromiso de cuentas privilegiadas, caída de CRM/ERP, indisponibilidad de web/tienda online, pérdida o cifrado de copias, acceso masivo a datos personales, compromiso simultáneo de correo y acceso remoto | Gestión de crisis, priorización de continuidad del negocio, medidas de contención de emergencia, coordinación ejecutiva, comunicación formal y activación de continuidad y recuperación | Escalado inmediato a Dirección, Responsable de Seguridad, Legal/DPO, responsables de proceso, proveedores críticos y terceros que deban intervenir |

### Reglas de decisión

1. Un incidente será al menos S3 si afecta a correo corporativo, datos personales, servicios cloud con información sensible o accesos a sistemas de negocio relevantes.
2. Un incidente será S4 desde el inicio si compromete CRM/ERP, servidores de archivos y aplicaciones, copias de seguridad, múltiples sedes, cuentas privilegiadas o la disponibilidad de la web/tienda online como canal principal de contacto y venta.
3. También será S4 cualquier incidente con cifrado de sistemas, exfiltración confirmada de datos sensibles, compromiso de varias cuentas o degradación severa de la operación que impida prestar servicio con normalidad.
4. Si el incidente afecta a datos personales, el responsable del incidente involucrará a Legal o al DPO para valorar si existe brecha de seguridad notificable.

### Tiempos máximos de clasificación y escalado

| Nivel | Tiempo máximo para clasificar | Tiempo máximo para escalar | Frecuencia orientativa de actualización |
|---|---|---|---|
| S1 - Baja | 1 jornada laboral | 1 jornada laboral | Al cierre del análisis o si cambia el alcance |
| S2 - Media | 4 horas laborables | 4 horas laborables | Cada jornada o por cambio relevante |
| S3 - Alta | 1 hora | 1 hora | Al menos dos veces al día y por evento relevante |
| S4 - Crítica | 30 minutos | Inmediato | Seguimiento continuo y actualizaciones dirigidas por el jefe del incidente |

### Escalado interno mínimo

| Severidad | Deben participar como mínimo |
|---|---|
| S1 - Baja | Técnico responsable del área afectada y registro del caso |
| S2 - Media | Responsable del incidente, SME del sistema afectado y propietario del servicio o activo |
| S3 - Alta | Responsable del incidente, líderes de investigación, remediación y comunicación, SME técnico, propietario del proceso, Responsable de Seguridad y Legal/DPO si aplica |
| S4 - Crítica | Todo lo anterior más Dirección, comité de crisis si procede, responsables de continuidad, responsables de comunicación externa y apoyo de proveedores críticos |

### Escalado externo mínimo

1. Se notificará a proveedores o socios cuando el incidente afecte a servicios externalizados, infraestructura alojada externamente, SaaS, nube, web/tienda online o accesos de terceros.
2. Se notificará a clientes solo cuando exista impacto real o potencial sobre sus datos, sus servicios o la confianza operacional, y siempre bajo coordinación del responsable del incidente, Dirección y el área de comunicación.
3. Se notificará a reguladores cuando el análisis legal determine obligación normativa, especialmente en incidentes con datos personales o impacto relevante sobre cumplimiento.
4. Se valorará contactar con aseguradora y fuerzas y cuerpos de seguridad en incidentes graves, especialmente ransomware, fraude, extorsión, intrusión relevante o compromiso con impacto económico o penal.

# Iniciar la respuesta

## Nombre del incidente

Cree una frase simple y única para referirse al incidente. Ese nombre se utilizará en el expediente, en los canales de coordinación, en la línea temporal y en los informes.

Formato recomendado: `AAAA-MM-DD - [tipo] - [activo o área]`.

Ejemplo: `2026-05-11 - Phishing - Correo corporativo`.

## Reunir el equipo de respuesta

1. Llame o movilice al Responsable de Seguridad o al responsable de guardia designado.
2. No hable del incidente fuera del equipo de respuesta salvo autorización expresa.
3. Inicie o únase al canal de chat de respuesta autorizado.
4. Inicie o únase a la llamada de respuesta si la severidad es S2 o superior, o si la situación es confusa y evolutiva.
5. Prefiera llamada de voz, chat corporativo y repositorio seguro sobre correo electrónico para la coordinación.
6. No utilice canales personales, mensajería informal ni cuentas no autorizadas para compartir evidencias, credenciales, logs o decisiones.
7. Invite al personal de guardia, a los responsables técnicos y a las partes interesadas necesarias según el nivel de severidad.
8. En incidentes complejos o graves, establezca una sala de colaboración virtual o física.

### Estructura del equipo de respuesta

| Rol del equipo de respuesta | Función principal |
|---|---|
| Jefe del incidente | Dirige la respuesta, clasifica, prioriza, asigna y decide escalado |
| Adjunto del incidente | Sustituye o apoya al jefe del incidente |
| Escribano | Mantiene cronología, decisiones, evidencias y estado del caso |
| Líder de investigación | Coordina hipótesis, análisis técnico y delimitación de alcance |
| Líder de remediación | Coordina contención, erradicación y acciones técnicas |
| Líder de comunicación | Coordina comunicación interna y externa autorizada |
| SME técnicos | Aportan conocimiento experto sobre red, sistemas, correo, cloud, web o aplicaciones |
| Propietarios de proceso o servicio | Valoran impacto funcional, prioridades y aceptación de recuperación |
| Legal / DPO | Evalúan obligaciones regulatorias, contractuales y de protección de datos |
| Dirección | Aprueba decisiones con alto impacto, activa recursos extraordinarios y continuidad |
| RRHH | Interviene si hay personal implicado o medidas disciplinarias |
| Proveedor crítico | Apoya cuando el incidente afecta a servicios contratados |

### Información de contacto del equipo de respuesta

La información de contacto detallada deberá mantenerse en un directorio operativo controlado y revisado, al menos, una vez al año. Ese directorio incluirá:

- Responsable de Seguridad y suplentes
- Dirección
- TIC / Sistemas / Red
- Responsables de CRM/ERP
- Responsable web / proveedor de hosting
- Help Desk
- Legal / DPO
- RRHH
- Proveedores críticos de EDR, correo, backup, nube, hosting y conectividad
- Contactos de aseguradora y fuerzas y cuerpos de seguridad cuando aplique

## Establecer el ritmo de la batalla

### Realizar la llamada de respuesta inicial

1. Tome asistencia e identifique roles.
2. Pida al informador inicial un resumen factual del incidente.
3. Confirme activo afectado, impacto aparente, severidad inicial, acciones ya tomadas y riesgos inmediatos.
4. Nombre responsables de investigación, remediación y comunicación si la severidad lo justifica.
5. Defina la siguiente actualización y el canal principal de coordinación.
6. Mantenga activa la llamada o programe actualizaciones periódicas según severidad.

### Referencia: estructura de la llamada de respuesta inicial

1. Presentación del jefe del incidente.
2. Confirmación de asistentes y roles.
3. Resumen inicial del caso.
4. Preguntas para entender síntomas, vector, alcance, impacto y cronología.
5. Confirmación de severidad provisional.
6. Asignación de líneas de trabajo.
7. Confirmación de acciones ya realizadas.
8. Confirmación de próximos hitos y hora de la siguiente actualización.

### Realizar actualizaciones de respuesta

Las actualizaciones programadas se usarán para revisar cambios de severidad, evolución del alcance, nuevas hipótesis, decisiones de contención, dependencias de negocio, necesidad de comunicación y apoyo adicional.

### Referencia: estructura de la llamada de actualización de la respuesta

1. Resumen actualizado del incidente.
2. Cambio de impacto, vector, resumen o línea temporal.
3. Actualización del equipo de investigación.
4. Actualización del equipo de remediación.
5. Actualización del equipo de comunicación.
6. Decisiones nuevas, tareas aprobadas y bloqueos.
7. Confirmación del siguiente punto de control.

## Supervisar el alcance

Supervise el alcance de la respuesta para asegurarse de que no excede la capacidad del equipo y de que la cadena de mando sigue siendo clara.

### Crear subequipos

En incidentes complejos o graves se predefinen tres subequipos:

1. Investigación
2. Remediación
3. Comunicación

Cada subequipo podrá contar con su propio canal operativo, pero responderá al jefe del incidente.

### Incidente dividido

Si un incidente resulta ser dos o más incidentes distintos:

1. Establezca un expediente separado para cada línea de incidente.
2. Coordine investigación, remediación y comunicación en el expediente correspondiente.
3. Mantenga un jefe del incidente de alto nivel para conservar unidad de mando y priorización común.

## Crear el archivo del incidente

Cree un expediente único y seguro para el incidente. Debe incluir, como mínimo:

1. Identificador único del incidente.
2. Nombre del incidente.
3. Fecha y hora de apertura.
4. Clasificación y severidad inicial.
5. Activos, usuarios, cuentas y sedes afectadas.
6. Resumen ejecutivo del incidente.
7. Línea temporal de hechos y acciones.
8. Evidencias y su ubicación.
9. Decisiones de contención, erradicación y recuperación.
10. Comunicaciones realizadas.
11. Severidad final, causa raíz o hipótesis más probable y acciones correctivas.


# Investigar

Investigar, remediar y comunicar deben desarrollarse en paralelo siempre que sea posible. El jefe del incidente coordinará estas actividades y priorizará las acciones de investigación en función de la severidad, el impacto en negocio y la urgencia de contención.

## Recoger las pistas iniciales

1. Entreviste al informador inicial.
2. Recoja alarmas, eventos, mensajes, capturas, nombres de host, cuentas, rutas de archivos y cualquier detalle temporal relevante.
3. Entreviste a SME con experiencia en el sistema o dominio afectado para comprender detalles técnicos, contexto y riesgo.
4. Entreviste a responsables de negocio para comprender el impacto funcional, la prioridad del activo y la tolerancia a la interrupción.
5. Asegúrese de que las pistas recogidas sean relevantes, detalladas y accionables.

### Referencia: lista de recursos de respuesta

| Recurso | Ubicación o responsable |
|---|---|
| Inventario de activos críticos | Responsable de Seguridad / inventario corporativo |
| Inventario de información crítica | Responsable de Seguridad / propietarios de información |
| Diagrama de red | TIC / administrador de red |
| Consola SIEM | Equipo TIC / Seguridad |
| Consola EDR | TIC / proveedor de seguridad |
| Firewall, VPN y red | Administrador de red |
| Consola de correo | TIC / proveedor de correo |
| Consola cloud / SaaS | Responsable del servicio |
| Backups y registro de restauraciones | TIC / almacenamiento |
| Repositorio seguro de evidencias | Responsable de Seguridad |
| Directorio de contactos y guardias | Dirección / Seguridad / TIC |

## Actualizar el plan de investigación y el archivo de incidentes

1. Revise y refine el impacto del incidente.
2. Revise y refine el vector del incidente.
3. Revise y refine el resumen del incidente.
4. Revise y perfeccione la línea de tiempo con hechos e inferencias.
5. Cree hipótesis sobre lo ocurrido y su nivel de confianza.
6. Identifique y priorice las preguntas clave para apoyar o descartar las hipótesis.
7. Consulte los playbooks específicos aplicables.

El plan de investigación es fundamental para una respuesta eficaz, porque orienta la recogida de datos, la asignación de esfuerzos y las decisiones de contención y remediación.

### Referencia: táctica del atacante a la matriz de preguntas clave

| Táctica o fase | Preguntas clave orientativas |
|---|---|
| Acceso inicial | ¿Cómo entró? ¿Desde cuándo? ¿Qué sistema o cuenta fue la puerta de entrada? |
| Ejecución | ¿Qué código, herramienta o acción se ejecutó? |
| Persistencia | ¿Qué mecanismo quedó activo para volver a entrar? |
| Escalada de privilegios | ¿Qué permisos obtuvo y cómo? |
| Evasión de defensa | ¿Qué controles se desactivaron o evitaron? |
| Acceso a credenciales | ¿Qué cuentas, secretos o tokens quedaron expuestos? |
| Descubrimiento | ¿Qué aprendió el atacante sobre la red o la organización? |
| Movimiento lateral | ¿A qué sistemas o segmentos se movió y con qué cuenta? |
| Recogida | ¿Qué datos se buscaron o agruparon? |
| Exfiltración | ¿Qué datos salieron, cuándo y por qué canal? |
| Impacto | ¿Qué se cifró, borró, alteró o interrumpió? |

## Crear y desplegar indicadores de compromiso (IOC)

1. Identifique IOC de red, host, correo, cloud y comportamiento a partir de las pistas iniciales y del análisis.
2. Valide si son relevantes antes de desplegarlos.
3. Priorice los IOC que permitan detectar expansión lateral, nuevos sistemas afectados o repetición del ataque.
4. Utilice formatos compatibles con las herramientas corporativas siempre que sea posible.
5. Correlacione varios tipos de IOC en los mismos sistemas para aumentar precisión.

## Identificar los sistemas de interés

1. Valide si los sistemas afectados o sospechosos son relevantes para la investigación.
2. Categorice por motivo de interés: malware, cuenta comprometida, datos sensibles, acceso remoto, privilegios elevados, dependencia de negocio o exposición pública.
3. Priorice recogida, análisis y remediación en función del impacto de negocio, la severidad y el plan de investigación.

## Recoger las pistas iniciales

1. Entreviste al informador inicial.
2. Recoja alarmas, eventos, mensajes, capturas, nombres de host, cuentas, rutas de archivos y cualquier detalle temporal.
3. Entreviste a SME con experiencia en el sistema o dominio afectado.
4. Entreviste a responsables de negocio para comprender el impacto funcional y la prioridad real del activo.
5. Garantice que las pistas sean relevantes, detalladas y accionables.

### Referencia: lista de recursos de respuesta

| Recurso | Ubicación o responsable |
|---|---|
| Inventario de activos críticos | Responsable de Seguridad / inventario corporativo |
| Inventario de información crítica | Responsable de Seguridad / propietarios de información |
| Diagrama de red | TIC / administrador de red |
| Consola SIEM | Equipo TIC / Seguridad |
| Consola EDR | TIC / proveedor de seguridad |
| Firewall, VPN y red | Administrador de red |
| Consola de correo | TIC / proveedor de correo |
| Consola cloud / SaaS | Responsable del servicio |
| Backups y registro de restauraciones | TIC / almacenamiento |
| Repositorio seguro de evidencias | Responsable de Seguridad |
| Directorio de contactos y guardias | Dirección / Seguridad / TIC |

## Actualizar el plan de investigación y el archivo de incidentes

1. Revise y refine el impacto del incidente.
2. Revise y refine el vector del incidente.
3. Revise y refine el resumen del incidente.
4. Revise y perfeccione la línea de tiempo con hechos e inferencias.
5. Cree hipótesis sobre lo ocurrido y su nivel de confianza.
6. Identifique y priorice las preguntas clave para apoyar o descartar las hipótesis.
7. Consulte los playbooks específicos aplicables.

### Referencia: táctica del atacante a la matriz de preguntas clave

| Táctica o fase | Preguntas clave orientativas |
|---|---|
| Acceso inicial | ¿Cómo entró? ¿Desde cuándo? ¿Qué sistema o cuenta fue la puerta de entrada? |
| Ejecución | ¿Qué código, herramienta o acción se ejecutó? |
| Persistencia | ¿Qué mecanismo quedó activo para volver a entrar? |
| Escalada de privilegios | ¿Qué permisos obtuvo y cómo? |
| Evasión de defensa | ¿Qué controles se desactivaron o evitaron? |
| Acceso a credenciales | ¿Qué cuentas, secretos o tokens quedaron expuestos? |
| Descubrimiento | ¿Qué aprendió el atacante sobre la red o la organización? |
| Movimiento lateral | ¿A qué sistemas o segmentos se movió y con qué cuenta? |
| Recogida | ¿Qué datos se buscaron o agruparon? |
| Exfiltración | ¿Qué datos salieron, cuándo y por qué canal? |
| Impacto | ¿Qué se cifró, borró, alteró o interrumpió? |

## Crear y desplegar indicadores de compromiso (IOC)

1. Identifique IOC de red, host, correo, cloud y comportamiento a partir de las pistas iniciales y del análisis.
2. Valide si son relevantes antes de desplegarlos.
3. Priorice los IOC que permitan detectar expansión lateral, nuevos sistemas afectados o repetición del ataque.
4. Utilice formatos compatibles con las herramientas corporativas siempre que sea posible.
5. Correlacione varios tipos de IOC en los mismos sistemas para aumentar precisión.

## Identificar los sistemas de interés

1. Valide si los sistemas afectados o sospechosos son relevantes para la investigación.
2. Categorice por motivo de interés: malware, cuenta comprometida, datos sensibles, acceso remoto, privilegios elevados, dependencia de negocio o exposición pública.
3. Priorice recogida, análisis y remediación en función del impacto de negocio, la severidad y el plan de investigación.

# Recogida de pruebas

Recoja y almacene las pruebas de acuerdo con la política interna y con cadena de custodia adecuada cuando exista potencial disciplinario, contractual, regulatorio o judicial.

## Ejemplo de artefactos útiles

- Procesos y servicios en ejecución
- Hashes y rutas de binarios relevantes
- Aplicaciones instaladas y cambios recientes
- Usuarios locales y de dominio
- Puertos de escucha y conexiones de red establecidas
- Persistencia de arranque y autoejecución
- Tareas programadas y cron
- Registros de eventos del sistema y de aplicaciones
- Artefactos EDR y detecciones antivirus
- Actividad de acceso remoto: RDP, VPN, SSH u otras herramientas
- Telemetría DNS, proxy, firewall y flujo de red
- Actividad en correo electrónico, adjuntos, reglas, reenvíos y accesos al buzón
- Actividad en CRM/ERP, servicios cloud y almacenamiento compartido

## Analizar las pruebas

1. Priorice el análisis según el plan de investigación.
2. Analice logs, telemetría, evidencias en vivo y artefactos adquiridos.
3. Clasifique los hallazgos por certeza, criticidad y relación con la hipótesis principal.
4. Documente nuevos IOC, nuevos sistemas afectados y cualquier cambio de severidad.
5. Actualice el expediente del incidente tras cada hallazgo significativo.

## Ejemplo de indicadores útiles

- Comportamiento inusual de autenticación
- Horarios atípicos o ubicaciones remotas no esperadas
- Nombres de usuario con formato no estándar
- Binarios no firmados que se conectan a la red
- Balizamiento o transferencias de datos significativas
- Uso excesivo de compresión o archivado en sistemas sensibles
- Conexiones en puertos no utilizados previamente
- Cambios en tablas de rutas, reglas de firewall o configuraciones de VPN
- Reglas de reenvío de correo no autorizadas o nuevos consentimientos SaaS

## Iterar la investigación

Actualice el plan de investigación y repita hasta el cierre. Investigar, remediar y comunicar deben desarrollarse en paralelo cuando sea posible.

# Remediar

Investigar, remediar y comunicar en paralelo, utilizando equipos separados cuando sea posible. El jefe del incidente coordinará estas actividades.

## Actualizar el plan de remediación

1. Revise el expediente del incidente.
2. Revise los playbooks aplicables.
3. Revise la lista de recursos de respuesta.
4. Considere qué tácticas del atacante están presentes en el incidente.
5. Desarrolle acciones de proteger, detectar, contener y eliminar para cada táctica aplicable.
6. Priorice en base a estrategia temporal, impacto, urgencia y riesgo de negocio.
7. Documente la estrategia aprobada en el expediente.

### Proteger

¿Cómo podemos evitar que esto se repita o reducir el riesgo?

- Parchear aplicaciones y sistemas operativos.
- Actualizar firmas y políticas de IPS, IDS, EDR o antimalware.
- Reducir ubicaciones con datos críticos.
- Reducir cuentas administrativas o privilegiadas.
- Habilitar MFA en sistemas críticos, correo, VPN y accesos privilegiados.
- Reforzar requisitos de contraseñas y bloqueo de intentos.
- Bloquear puertos y protocolos no utilizados.
- Aplicar listas blancas de conexión para servicios críticos.
- Revisar reglas de VPN, segmentación y correo autenticado.

### Detectar

¿Cómo podemos detectar esto en el futuro y mejorar investigación y detección?

- Mejorar registro y retención de logs del sistema, aplicaciones y SaaS.
- Mejorar agregación de logs y casos de uso del SIEM.
- Crear o ajustar alertas basadas en IOC y comportamiento.
- Revisar cobertura EDR, correo, VPN, directorio, CRM/ERP y cloud.
- Incorporar métricas y lecciones aprendidas en la detección futura.

### Contener

¿Cómo podemos evitar que esto se extienda o se agrave?

- Aislar endpoints o servidores de la red.
- Deshabilitar o bloquear cuentas comprometidas.
- Revocar sesiones, tokens y accesos remotos.
- Bloquear IP, dominios, URLs, adjuntos u otros IOC.
- Retirar servicios expuestos o pasar a modo degradado.
- Activar bloqueos perimetrales y segmentación temporal.
- Coordinar con proveedores la contención en servicios externos.
- Bloquear o eliminar accesos de terceros cuando sea necesario.

### Eliminar

¿Cómo podemos eliminar esto de nuestros activos?

- Reconstruir o restaurar sistemas y datos comprometidos desde un estado bueno conocido.
- Restablecer contraseñas y secretos.
- Eliminar cuentas, claves, reglas o persistencias hostiles.
- Borrar malware específico cuando sea viable y seguro.
- Corregir vulnerabilidades o errores de configuración que originaron el incidente.
- Migrar temporalmente a ubicaciones, servicios o proveedores alternativos cuando sea necesario.

## Elegir el momento de la remediación

Determine la estrategia de tiempo involucrando al jefe del incidente, a los SME, a los propietarios del sistema, a los propietarios del proceso de negocio y, si procede, a Dirección.

- **Remediación inmediata**: cuando sea más importante detener de inmediato la actividad del atacante que seguir investigando.
- **Remediación retrasada**: cuando convenga completar investigación, identificar alcance o no alertar prematuramente al atacante.
- **Remediación combinada**: cuando haya que contener de inmediato una parte crítica mientras se sigue investigando otra parte del incidente.

## Ejecutar la remediación

1. Evalúe y explique los riesgos de las acciones de remediación a las partes interesadas.
2. Implemente de inmediato las acciones de bajo riesgo y alto valor.
3. Programe y asigne acciones según la estrategia temporal aprobada.
4. Ejecute las acciones de remediación en lotes coordinados cuando eso minimice riesgo e interrupción.
5. Documente estado, hora de ejecución, aprobaciones y resultados, especialmente para medidas temporales.

## Iterar la remediación

Actualice el plan de remediación y repita hasta el cierre.

# Comunicar

Investigar, remediar y comunicar en paralelo, utilizando equipos separados cuando sea posible. Toda comunicación debe incluir la información más precisa disponible. No comunique especulaciones.

## Comunicar internamente

### Notificar y actualizar a las partes interesadas

- Comuníquese con las partes interesadas como parte de las llamadas iniciales y de actualización, así como mediante actualizaciones impulsadas por eventos.
- Coordine actualizaciones independientes para Dirección, Legal, RRHH u otras áreas solo cuando sean necesarias.
- Céntrese en vector, impacto, resumen, línea temporal y pasos de remediación.
- No especule.

### Notificar y actualizar la organización

- No notifique al personal que no participa en la respuesta hasta autorización del jefe del incidente.
- Coordine las actualizaciones organizativas con Dirección y comunicación.
- Explique impacto, medidas adoptadas y cualquier instrucción que deban seguir los usuarios.
- No comparta detalles técnicos innecesarios ni información sensible del expediente.

### Crear informe de incidentes

Tras el cierre del incidente, el expediente servirá de base para elaborar el informe final. El informe incluirá:

1. Resumen ejecutivo.
2. Vector y causa raíz o hipótesis más probable.
3. Impacto funcional, técnico, legal y reputacional.
4. Línea temporal principal.
5. Sistemas, cuentas y datos afectados.
6. Acciones de contención, erradicación y recuperación.
7. Decisiones clave y aprobaciones.
8. Obligaciones regulatorias y comunicaciones realizadas.
9. Lecciones aprendidas y plan de mejora.

## Comunicar externamente

### Notificar a los reguladores

- No notifique a reguladores hasta validación por Legal/DPO y autorización del jefe del incidente y Dirección.
- Coordine requisitos, formato y calendario con Legal/DPO.
- Si hay brecha de datos personales, valore notificación conforme al RGPD y normativa aplicable.

### Notificar a los clientes

- No notifique a clientes sin autorización del jefe del incidente, Dirección y Legal/DPO cuando aplique.
- Coordine las notificaciones con comunicación o Dirección.
- Céntrese en hechos, impacto real, medidas adoptadas y recomendaciones prácticas.
- No use fórmulas vacías ni especule sobre terceros salvo información ya pública y confirmada.
- Sea claro sobre qué información o servicio ha sido afectado y cómo les impacta.

### Notificar a los proveedores y socios

- Notifique a proveedores y socios cuando el incidente les afecte o requiera su participación.
- Contacte preferentemente con sus equipos de seguridad o responsables operativos.
- Coordine esfuerzos de respuesta, tiempos y compartición de información relevante.

### Notificar a las fuerzas de seguridad

- Coordine con Dirección y Legal antes de interactuar con fuerzas y cuerpos de seguridad.
- Valore esta notificación especialmente en ransomware, extorsión, fraude, intrusión relevante o compromiso con impacto económico o penal.
- Preserve evidencias antes de cualquier actuación externa que pueda afectar su integridad.

### Contactar apoyo externo de respuesta

- Active apoyo externo cuando el alcance, la complejidad o la falta de capacidades internas lo exijan.
- Considere proveedor de respuesta a incidentes, aseguradora, asesoría legal especializada o apoyo de comunicación de crisis.

### Compartir inteligencia

Comparta IOC o aprendizaje relevante con comunidades o terceros de confianza cuando proceda y siempre que Legal, Dirección y el jefe del incidente lo consideren adecuado.

# Recuperación

La recuperación suele estar dirigida por las unidades de negocio y por los propietarios de los sistemas. Las acciones de recuperación se tomarán solo en colaboración con las partes interesadas pertinentes.

1. Ponga en marcha planes de continuidad y recuperación ante desastres cuando el incidente impida mantener niveles mínimos de servicio.
2. Integre las acciones de seguridad con los esfuerzos de recuperación de la organización.
3. Priorice restauración de servicios esenciales según criticidad de negocio.
4. Restaure desde backups conocidos como limpios y verificados cuando proceda.
5. Valide integridad, trazabilidad y seguridad antes de devolver un servicio a producción.
6. Aplique monitorización reforzada en la fase de retorno al servicio.

## Prioridades de recuperación

| Prioridad | Activo o servicio | Objetivo de recuperación |
|---|---|---|
| 1 | CRM/ERP | Restablecer la operativa de negocio con la mayor rapidez posible |
| 1 | Servidores de archivos y aplicaciones críticos | Recuperar acceso a documentación y herramientas de trabajo esenciales |
| 1 | Copias de seguridad y capacidad de restauración | Confirmar posibilidad real de recuperación segura |
| 2 | Correo corporativo | Restablecer comunicación interna y externa |
| 2 | Web corporativa y tienda online | Recuperar el canal público y comercial |
| 3 | Endpoints y servicios auxiliares | Recuperación escalonada según impacto y dependencia |

## Criterio de continuidad

La organización tomará como referencia las metas definidas en su PDS: mantener la disponibilidad del negocio digital, recuperar servicios críticos en menos de 4 horas cuando sea viable y evitar pérdidas de datos superiores a 1 hora en los procesos prioritarios soportados por copias adecuadas y procedimientos probados.

# Cuadernos de juego

Los siguientes playbooks recogen los pasos comunes de investigación, remediación y comunicación para determinados tipos de incidentes. Deben mantenerse vivos, revisarse al menos anualmente y actualizarse tras simulacros, cambios tecnológicos o incidentes reales.

## Playbooks prioritarios

| Playbook | Escenario principal | Activos principales |
|---|---|---|
| Ransomware | Cifrado, borrado o impacto en continuidad | CRM/ERP, servidores, backups, endpoints |
| Phishing | Suplantación, malware, robo de credenciales | Correo, identidades, usuarios, endpoints |
| Compromiso de identidad y acceso | Uso indebido de cuentas, MFA, privilegios | Directorio, VPN, correo, CRM/ERP |
| Website defacement / compromiso web | Alteración o caída del sitio | Web, tienda online, hosting |
| Supply chain compromise | Incidente originado en proveedor o tercero | Hosting, nube, software, servicios gestionados |

## Escenarios prioritarios según el PDS

| Código | Escenario | Activos principales afectados | Impacto esperado |
|---|---|---|---|
| R01 | Ransomware o cifrado malicioso en CRM/ERP | CRM/ERP, datos operativos, datos personales | Parada de negocio, pérdida de integridad y disponibilidad |
| R02 | Intrusión o compromiso de servidores | Servidores de archivos y aplicaciones | Interrupción operativa, acceso no autorizado, borrado o corrupción |
| R04 | Compromiso web, defacement o caída del canal online | Página web y tienda online | Pérdida de imagen, caída del servicio, posible fraude a clientes |
| R05 | Phishing o compromiso de correo | Correo corporativo, identidades, usuarios | Fraude, robo de credenciales, malware, suplantación |
| R06 | Fallo o inutilización de copias de seguridad | Backups, almacenamiento, continuidad | Imposibilidad de recuperación ante desastre o ransomware |
| R08 | Compromiso de puesto de trabajo | Endpoints, credenciales, datos locales | Entrada inicial, movimiento lateral, exfiltración |
| R11 | Incidente ligado a proveedor o nube | Hosting web, SaaS, almacenamiento cloud, terceros | Dependencia externa, pérdida de control, indisponibilidad |

# Anexos operativos

## Matriz de escalado por tipo de incidente

| Tipo de incidente | Severidad inicial recomendada | Escalado mínimo obligatorio |
|---|---|---|
| Ransomware en CRM/ERP o servidores | S4 - Crítica | Dirección, Responsable de Seguridad, TIC, Legal/DPO, responsables de proceso |
| Phishing con robo de credenciales corporativas | S3 - Alta | Responsable de Seguridad, TIC, Help Desk, responsables del área afectada |
| Compromiso de cuenta privilegiada | S4 - Crítica | Dirección, Responsable de Seguridad, TIC, Legal/DPO |
| Defacement o caída de web corporativa/tienda | S3 o S4 según impacto | Responsable de Seguridad, TIC, proveedor web, Dirección, Comunicación |
| Brecha de datos personales confirmada | S3 o S4 | Dirección, DPO/Legal, Responsable de Seguridad, TIC |
| Malware aislado en puesto sin expansión | S2 - Media | TIC, Help Desk, Responsable de Seguridad |
| Incidente en proveedor crítico o SaaS | S3 - Alta | Responsable de Seguridad, Dirección, Legal, proveedor, responsables del servicio |

## Tiempos objetivo de gestión

| Hito | S4 - Crítica | S3 - Alta | S2 - Media | S1 - Baja |
|---|---|---|---|---|
| Registro inicial | 15 min | 30 min | 2 h | 1 jornada |
| Convocatoria del equipo | 15 min | 30 min | 4 h | Según necesidad |
| Primer resumen ejecutivo | 60 min | 2 h | 1 jornada | Según necesidad |
| Primera decisión de contención | 30 min | 1 h | 4 h | 1 jornada |
| Revisión de impacto regulatorio | 4 h | 1 jornada | 2 jornadas | Según necesidad |
| Revisión post-incidente | 5 días hábiles | 10 días hábiles | 15 días hábiles | 30 días hábiles |

## Documentación mínima del expediente

Todo expediente de incidente deberá contener como mínimo:

1. Identificador único del incidente.
2. Fecha y hora de apertura y cierre.
3. Clasificación y severidad inicial y final.
4. Activos, usuarios, cuentas y sedes afectadas.
5. Resumen ejecutivo del incidente.
6. Línea temporal de hechos y acciones.
7. Evidencias y su ubicación.
8. Decisiones de contención, erradicación y recuperación.
9. Impacto funcional, técnico, legal y reputacional.
10. Comunicaciones realizadas.
11. Causa raíz o hipótesis más probable.
12. Acciones correctivas y responsables.
13. Lecciones aprendidas.

## Métricas de seguimiento

La eficacia del plan se medirá, como mínimo, con las siguientes métricas:

1. Tiempo medio de detección.
2. Tiempo medio de activación.
3. Tiempo medio hasta contención inicial.
4. Tiempo medio de recuperación por tipo de activo.
5. Número de incidentes por categoría y severidad.
6. Porcentaje de incidentes con expediente completo.
7. Porcentaje de acciones correctivas cerradas en plazo.
8. Número de brechas notificables y tiempo de evaluación legal.
9. Tasa de recurrencia por misma causa raíz.
10. Resultados de simulacros y pruebas del plan.

## Mantenimiento del plan

El plan será revisado al menos una vez al año y, además, cada vez que ocurra alguna de estas circunstancias:

1. Incidente alto o crítico con lecciones relevantes.
2. Cambios importantes en la infraestructura, proveedores o servicios críticos.
3. Modificación de requisitos regulatorios o contractuales.
4. Cambios en roles, responsables o canales de comunicación.
5. Implantación de nuevos proyectos del PDS que alteren la capacidad de respuesta.

La revisión anual incluirá validación de contactos, canales, roles, inventario de activos críticos, playbooks vigentes, procedimientos de escalado y coordinación con continuidad.

## Pruebas y ejercicios

La organización realizará, como mínimo, un simulacro anual de incidente relevante y ejercicios parciales cuando se implanten cambios significativos en capacidades de seguridad.

Los escenarios prioritarios para ejercicios serán:

1. Ransomware con impacto en CRM/ERP y backups.
2. Phishing con compromiso de credenciales y buzón corporativo.
3. Caída o manipulación de la web y tienda online.
4. Brecha de datos personales ligada a proveedor o nube.

Cada ejercicio deberá generar acta, resultados, desviaciones detectadas, decisiones de mejora y responsable de seguimiento.

## Criterios de aprobación

Este plan entrará en vigor tras su aprobación por Dirección. El Responsable de Seguridad custodiará la versión vigente, controlará revisiones y asegurará su difusión controlada a las áreas implicadas.

La versión operativa del plan deberá estar disponible para Dirección, TIC, Seguridad, Legal/DPO, RRHH, Help Desk y responsables de proceso con participación en incidentes.

## Anexo operativo breve

Ante cualquier sospecha de incidente, el orden práctico de actuación será el siguiente:

1. Registrar el caso.
2. Evaluar impacto funcional, impacto sobre la información y severidad.
3. Activar responsables, expediente y canal de coordinación.
4. Preservar evidencias y detener cambios no esenciales.
5. Investigar, contener y comunicar en paralelo.
6. Erradicar causa y persistencia.
7. Recuperar con validación reforzada.
8. Cerrar expediente y ejecutar mejoras.

Este anexo no sustituye al resto del plan. Su función es servir como recordatorio operativo inmediato durante los primeros minutos del incidente.
