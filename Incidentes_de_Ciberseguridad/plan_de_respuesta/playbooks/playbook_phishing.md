# Playbook de respuesta a phishing

## 1. Finalidad

Este playbook establece la respuesta específica ante incidentes de phishing que afecten, o puedan afectar, al correo corporativo, a las credenciales de usuarios, a los puestos de trabajo o a los sistemas de negocio de la organización.

Su finalidad es detectar con rapidez el alcance real de la campaña, contener cuentas y mensajes relacionados, evitar que el incidente evolucione a compromiso de identidad, fraude o malware, y recuperar la operativa con evidencias suficientes para revisión posterior.

Este documento complementa al Plan de Respuesta a Incidentes general y debe aplicarse junto con el procedimiento de clasificación, escalado, documentación, comunicación y gestión de evidencias.

## 2. Alcance

Este playbook aplica a correos electrónicos, mensajes o campañas que intenten engañar a usuarios para que revelen credenciales, aprueben accesos multifactor, descarguen malware, realicen pagos fraudulentos, modifiquen datos de facturación o accedan a sitios falsos.

Incluye también variantes como spear phishing, business email compromise, phishing con robo de sesión, smishing cuando afecte al ámbito corporativo y campañas con adjuntos maliciosos.

En esta organización, los activos más sensibles frente a este tipo de incidente son el correo corporativo, las identidades de usuario, los accesos a CRM/ERP, los puestos de trabajo, la VPN, los móviles corporativos y cualquier buzón con capacidad de relación con clientes, proveedores o pagos.

## 3. Activación

Se activará este playbook ante cualquiera de estas situaciones:

1. Reporte de un usuario que ha recibido o abierto un correo sospechoso.
2. Detección por pasarela de correo, SIEM, EDR o proveedor de una campaña de phishing activa.
3. Evidencia de robo de credenciales, aprobación de MFA no reconocida o inicio de sesión anómalo tras un correo sospechoso.
4. Descarga o ejecución de adjuntos o enlaces vinculados a un mensaje fraudulento.
5. Comunicación de cliente o proveedor alertando de mensajes suplantando a la empresa.
6. Detección de reglas de buzón, reenvíos, respuestas automáticas o cambios no autorizados compatibles con compromiso de correo.

La severidad inicial recomendada será media si se trata de un mensaje aislado sin interacción del usuario, alta si existen clics, introducción de credenciales o múltiples usuarios afectados, y crítica si hay cuentas privilegiadas comprometidas, fraude económico, acceso confirmado a sistemas de negocio o afectación a datos personales sensibles.

## 4. Objetivos de respuesta

La respuesta deberá perseguir estos objetivos:

1. Identificar rápidamente a todos los usuarios, mensajes, buzones y sistemas relacionados.
2. Contener cuentas comprometidas y bloquear el contenido malicioso antes de que la campaña se extienda.
3. Determinar si el phishing ha derivado en malware, robo de credenciales, bypass de MFA o fraude.
4. Recuperar el control de las cuentas, accesos y dispositivos afectados.
5. Comunicar instrucciones claras a usuarios, dirección y áreas afectadas sin generar confusión.

## 5. Roles mínimos

| Rol | Función principal en este playbook |
|---|---|
| Responsable del incidente / CISO | Coordina, clasifica, escala y valida decisiones críticas |
| TIC correo e identidades | Analiza mensajes, purga correos, resetea cuentas y revisa accesos |
| TIC endpoints / EDR | Analiza y contiene equipos si hubo clics, descargas o ejecución |
| Help Desk | Recoge avisos, guía al usuario y ejecuta primeras acciones autorizadas |
| Responsables de área | Ayudan a localizar usuarios afectados y validan impacto funcional |
| Legal / DPO | Evalúa posibles brechas, fraude y notificaciones necesarias |
| Dirección | Aprueba comunicaciones externas o decisiones con alto impacto |
| Proveedores críticos | Apoyo en correo, EDR, MDM, MFA o SaaS afectados |

## 6. Investigación

La investigación, la contención y la comunicación deben ejecutarse en paralelo. En phishing, una buena investigación no se limita a analizar un correo, sino que debe determinar si se ha producido compromiso real de cuenta, acceso a sistemas o descarga de malware.

### 6.1 Confirmación inicial

En los primeros minutos se revisará:

1. Quién ha reportado el mensaje y cuándo lo recibió.
2. Si el usuario abrió el correo, hizo clic, descargó adjunto, introdujo credenciales o aprobó MFA.
3. Si el mismo mensaje ha llegado a más usuarios.
4. Si existen inicios de sesión anómalos relacionados en correo, VPN, SaaS, CRM/ERP u otros sistemas.
5. Si hay indicadores de ejecución de malware o comportamiento anómalo en el endpoint.

### 6.2 Preguntas clave

El equipo deberá responder cuanto antes a estas preguntas:

1. ¿Cuántos usuarios recibieron el mensaje y cuántos interactuaron con él?
2. ¿Qué tipo de phishing es: credenciales, malware, fraude de pago, suplantación interna, consentimiento OAuth, robo de sesión o mixto?
3. ¿Se han visto comprometidas cuentas corporativas o personales usadas para trabajo?
4. ¿Se ha accedido realmente a buzones, SaaS, CRM/ERP, VPN u otros sistemas?
5. ¿Existen reglas de reenvío, borrado, ocultación o persistencia en los buzones afectados?
6. ¿El incidente ha impactado a clientes, proveedores, pagos o datos personales?
7. ¿Hay indicios de que el correo sea la fase inicial de un incidente mayor?

### 6.3 Fuentes de evidencia prioritarias

La investigación se apoyará en estas fuentes, según disponibilidad:

1. Cabeceras completas del correo sospechoso.
2. Trazas de la pasarela de correo, antispam o servicio de correo en la nube.
3. Registros de autenticación de correo, VPN, CRM/ERP y otros SaaS.
4. Alertas del EDR, antivirus, navegador y sistema operativo del usuario afectado.
5. Logs de proxy, DNS, firewall y navegación saliente.
6. Registros de MFA, aprobaciones push, tokens y sesiones activas.
7. Configuración del buzón, reglas, reenvíos automáticos, permisos delegados y aplicaciones conectadas.

### 6.4 Artefactos a recoger

Siempre que sea posible, se recopilarán:

1. Correo original en formato que conserve cabeceras completas.
2. Asunto, remitente visible, remitente real, reply-to, dominios implicados y URL completas.
3. Adjuntos o hashes de adjuntos, sin abrirlos en el equipo del usuario.
4. Captura del sitio falso, si ya se ha accedido, usando un entorno seguro o evidencia del navegador del usuario.
5. Tiempos de recepción, clic, login, aprobación MFA y acceso posterior.
6. Eventos de inicio de sesión, cambios de contraseña, cambios de MFA y reglas de buzón.
7. Evidencias del endpoint si hubo descarga, ejecución o redirección a contenido malicioso.

### 6.5 Clasificación del incidente

A efectos operativos, el phishing se clasificará en una o varias de estas categorías:

1. Phishing de credenciales.
2. Phishing con malware o adjunto malicioso.
3. Business email compromise o fraude de suplantación.
4. Phishing con aprobación fraudulenta de MFA.
5. Phishing con robo de sesión o token.
6. Campaña de suplantación externa usando la identidad de la empresa.

### 6.6 Evaluación de impacto

El impacto se evaluará considerando:

1. Número de usuarios alcanzados y porcentaje de interacción.
2. Tipo de cuentas afectadas, especialmente si hay privilegios elevados.
3. Sistemas a los que podía acceder la cuenta comprometida.
4. Riesgo de fraude económico, engaño a clientes o proveedores, o pérdida reputacional.
5. Posible acceso a datos personales o información sensible.
6. Necesidad de ampliar la respuesta a endpoints, identidad o continuidad.

## 7. Contención

La contención debe comenzar en cuanto exista evidencia razonable de interacción del usuario o de propagación del mensaje. En phishing, el tiempo es determinante: purgar tarde un correo o resetear tarde una cuenta puede convertir un incidente controlable en un compromiso serio.

### 7.1 Medidas inmediatas

Se adoptarán, según el caso, estas acciones:

1. Bloquear o poner en cuarentena el mensaje y sus variantes en el sistema de correo.
2. Purgar el correo de las bandejas de entrada de otros usuarios si ya ha sido entregado.
3. Deshabilitar temporalmente o limitar cuentas comprometidas.
4. Forzar cambio de contraseña y revocación de sesiones activas.
5. Revocar tokens, sesiones web, consentimientos OAuth o accesos persistentes sospechosos.
6. Reforzar o volver a registrar MFA cuando exista riesgo de compromiso del segundo factor.
7. Aislar el endpoint si hubo descarga, ejecución de adjuntos o navegación a contenido malicioso.
8. Bloquear dominios, URLs, IPs, hashes o remitentes asociados en correo, DNS, proxy y firewall.

### 7.2 Acciones específicas por escenario

Según el tipo de phishing, se aplicarán además estas medidas:

1. Si hubo robo de credenciales, revisar accesos recientes, restablecer contraseña, cerrar sesiones y comprobar intentos posteriores en servicios críticos.
2. Si hubo aprobación fraudulenta de MFA, revocar sesiones, invalidar el factor comprometido y revisar fatiga MFA o notificaciones push abusivas.
3. Si hubo fraude de factura o cambio de cuenta bancaria, bloquear pagos relacionados, avisar a Finanzas y revisar correos enviados desde cuentas afectadas.
4. Si hubo adjunto malicioso, contener el endpoint, revisar otros receptores del mismo archivo y buscar indicadores comunes en EDR.
5. Si la empresa está siendo suplantada hacia terceros, activar revisión de autenticidad de correo y preparar comunicación externa controlada.

### 7.3 Aumento de vigilancia

Tras la contención inicial se elevará la monitorización sobre:

1. Cuentas relacionadas con los usuarios afectados.
2. Accesos desde ubicaciones, IPs o dispositivos inusuales.
3. Nuevas reglas de correo, delegaciones o reenvíos.
4. Dominios y remitentes similares a la campaña detectada.
5. Alertas de malware o conexiones sospechosas en los endpoints implicados.

### 7.4 Lo que no debe hacerse

Durante la contención no se debe:

1. Pedir al usuario que siga interactuando con el correo sospechoso.
2. Abrir adjuntos o enlaces desde sistemas de producción.
3. Mantener cuentas comprometidas activas por comodidad operativa.
4. Informar al conjunto de la organización con mensajes vagos o técnicamente incorrectos.
5. Dar por cerrado el incidente solo porque se haya borrado el correo.

## 8. Erradicación

La erradicación busca eliminar restos del compromiso y evitar que el phishing derive en un incidente persistente de identidad o malware.

### 8.1 Acciones técnicas

Podrán incluirse, según el caso:

1. Restablecimiento completo de credenciales y revisión de secretos asociados.
2. Eliminación de reglas de buzón maliciosas, reenvíos externos, delegaciones o permisos anómalos.
3. Revocación de aplicaciones conectadas o consentimientos indebidos.
4. Saneamiento o reconstrucción del endpoint comprometido si hubo ejecución de malware.
5. Actualización de firmas, listas de bloqueo y reglas de detección.
6. Revisión de configuración SPF, DKIM y DMARC cuando la campaña implique suplantación del dominio corporativo.
7. Cierre del vector que facilitó el incidente, por ejemplo falta de MFA, filtros débiles o ausencia de formación.

### 8.2 Validación previa a recuperación

Antes de devolver la cuenta o el equipo a operación normal, TIC y el responsable del incidente verificarán que:

1. Las sesiones antiguas estén cerradas.
2. La contraseña y, si procede, el MFA hayan sido renovados correctamente.
3. No existan reglas maliciosas ni accesos persistentes en el buzón.
4. El endpoint esté limpio o haya sido reconstruido si fue necesario.
5. Se haya evaluado el acceso real a sistemas de negocio o datos.

## 9. Recuperación

La recuperación deberá devolver al usuario y al área afectada a un estado seguro y funcional, no solo operativo en apariencia.

### 9.1 Acciones de recuperación

1. Habilitar de nuevo la cuenta una vez saneada y validada.
2. Restaurar accesos necesarios al usuario si se limitaron temporalmente.
3. Confirmar con el responsable del área que no persisten impactos funcionales.
4. Reincorporar el endpoint a la red solo tras validación técnica.
5. Mantener monitorización reforzada durante un periodo prudencial sobre la cuenta y el equipo afectados.

### 9.2 Criterios de éxito

Se considerará recuperado el incidente cuando:

1. Los mensajes relacionados estén purgados o bloqueados.
2. Las cuentas comprometidas estén bajo control y sin sesiones ajenas activas.
3. No existan reglas, tokens o accesos persistentes maliciosos.
4. El endpoint esté validado como limpio o reconstruido.
5. Se haya evaluado correctamente si hubo o no acceso a información sensible.

## 10. Comunicación

La comunicación debe ser clara, práctica y muy concreta. En phishing, los usuarios necesitan instrucciones accionables más que explicaciones largas.

### 10.1 Comunicación interna

El responsable del incidente informará a Dirección y a las áreas implicadas del estado del caso, el alcance de la campaña, las medidas de contención y cualquier riesgo de fraude o afectación a clientes.

Las comunicaciones técnicas y de negocio deberán mantenerse separadas para evitar ruido y contradicciones.

### 10.2 Comunicación a usuarios

Cuando proceda, el mensaje a usuarios deberá incluir como mínimo:

1. Identificación básica del correo o campaña detectada.
2. Qué usuarios están potencialmente afectados.
3. Qué deben hacer, por ejemplo reportar, cambiar contraseña, no abrir enlaces o esperar validación de TIC.
4. Qué no deben hacer, por ejemplo reenviar el correo, responder al remitente o ignorar avisos de MFA no reconocidos.
5. Canal único para reportar nuevos casos.

### 10.3 Comunicación externa

Si la campaña suplanta a la empresa frente a clientes o proveedores, Dirección, Comunicación y Legal decidirán si procede aviso externo.

Si hubo fraude económico o exposición de datos personales, se valorarán notificaciones adicionales y contacto con las entidades afectadas.

### 10.4 Evaluación regulatoria

Si el compromiso de correo o identidad ha permitido acceso a datos personales, Legal y el DPO evaluarán si existe brecha notificable y si deben adoptarse medidas adicionales de información a afectados o autoridad de control.

## 11. Recursos mínimos necesarios

Para aplicar este playbook se consideran necesarios como mínimo:

1. Acceso administrativo al sistema de correo y a sus logs.
2. Capacidad de purga o cuarentena de mensajes.
3. Gestión de identidades, contraseñas, MFA y sesiones.
4. Telemetría de endpoints y capacidad de aislamiento mediante EDR o equivalente.
5. Repositorio seguro para evidencias y cronología.
6. Contactos claros con Help Desk, TIC, CISO, Legal/DPO y Dirección.
7. Procedimientos de escalado a proveedores de correo, SaaS o ciberseguridad cuando proceda.

## 12. Cierre y lecciones aprendidas

El expediente no se cerrará hasta dejar documentados, como mínimo:

1. Tipo exacto de campaña o hipótesis más probable.
2. Número de usuarios afectados y número de interacciones reales.
3. Cuentas, sistemas y datos potencialmente comprometidos.
4. Acciones de contención, erradicación y recuperación ejecutadas.
5. Impacto real en negocio, fraude, reputación y protección de datos.
6. Evidencias preservadas y su ubicación.
7. Medidas correctivas obligatorias y responsables.

### 12.1 Mejoras esperables tras el incidente

Un incidente de phishing debería traducirse normalmente en mejoras sobre estos puntos:

1. Refuerzo de MFA en sistemas críticos.
2. Mejora de autenticidad de correo y endurecimiento de filtros.
3. Simulaciones y formación orientadas a usuarios con métricas.
4. Revisión de privilegios, reenvíos, delegaciones y exposición de cuentas.
5. Revisión de tiempos de purga, bloqueo y escalado.
6. Ajuste de reglas de detección en correo, EDR y SIEM.

## 13. Guía operativa rápida

Durante la primera hora, la secuencia práctica recomendada será:

1. Recibir el aviso y abrir expediente.
2. Confirmar si hubo interacción del usuario.
3. Identificar receptores y alcance de la campaña.
4. Purgar o bloquear mensajes relacionados.
5. Contener cuentas, sesiones y MFA si hay indicios de compromiso.
6. Revisar endpoint si hubo clic, descarga o ejecución.
7. Informar a responsables según impacto.
8. Verificar si hubo acceso real a sistemas o datos.

Este resumen rápido no sustituye al resto del playbook. Su función es ayudar a actuar con orden durante la fase inicial, cuando los minutos cuentan más.