# Política 01: Protección del Puesto de Trabajo

**Versión**: 1.0  
**Fecha de aprobación**: [Completar con fecha]  
**Fecha de última revisión**: [Completar con fecha]  
**Responsable**: [Completar con nombre del Responsable de Seguridad]  
**Alcance**: Todos los empleados de la organización con puesto de trabajo asignado

---
[Version extendida. Consulta los ejemplos de INCIBE para ver ejemplos de polÍticas]

## 1. Antecedentes

### 1.1. Contexto de la Organización

> **INSTRUCCIÓN**: Describir aquí el contexto específico de vuestra empresa del PDS. Incluir:
> - Tipo de empresa, sector, tamaño
> - Tipo de información que maneja
> - Características especiales (teletrabajo, movilidad, etc.)
> - Por qué es crítico proteger los puestos de trabajo

**EJEMPLO**:
> "Somos una empresa de desarrollo de software con 50 empleados que gestiona proyectos para clientes del sector financiero y sanitario, manejando código fuente propietario y datos sensibles sujetos a GDPR. El 70% de nuestro equipo trabaja en modalidad híbrida, accediendo a repositorios de código y servidores de desarrollo desde diferentes ubicaciones. Durante el análisis de riesgos del PDS identificamos que los puestos de trabajo constituyen el principal vector de ataque, con 15 intentos de phishing detectados en el último semestre y 2 incidentes de malware que comprometieron temporalmente estaciones de trabajo."

### 1.2. Elementos Clave del Puesto de Trabajo Afectados

| Elemento                      | Tipo                    | Criticidad  | Justificación                 |
|-------------------------------|-------------------------|-------------|-------------------------------|
| [Completar según vuestro PDS] | Hardware/Software/Info  | Alta/Media  | [Explicar por qué es crítico] |
|                               |                         |             |                               |

**EJEMPLO**:

| Elemento                         | Tipo        | Criticidad  | Justificación                                                                                         |
|----------------------------------|-------------|-------------|-------------------------------------------------------------------------------------------------------|
| Portátiles corporativos          | Hardware    | Muy Alta    | Contienen repositorios de código, credenciales de acceso a sistemas de producción y datos de clientes |
| Estaciones de trabajo            | Hardware    | Alta        | Utilizadas para desarrollo y pruebas, con acceso a entornos de pre-producción                         |
| Entorno de desarrollo (IDE, Git) | Software    | Muy Alta    | Herramientas críticas para la operación diaria, contienen propiedad intelectual                       |
| Credenciales de acceso           | Información | Crítica     | Permiten acceso a sistemas de control de versiones, servidores, bases de datos                        |
| VPN corporativa                  | Software    | Alta        | Única vía de acceso remoto seguro a la red interna                                                    |

### 1.3. Escenarios de Riesgo

> **INSTRUCCIÓN**: Identificar al menos 3-4 riesgos principales relacionados con el puesto de trabajo,
> basándose en el análisis de riesgos del PDS.

#### Riesgo 1: [Completar con nombre del riesgo]

**Descripción**: [Explicar el escenario]

**Ejemplo real o potencial en la organización**: [Dar contexto específico]

**Impacto potencial**:
- **Confidencialidad**: [Alto/Medio/Bajo] - [Explicar]
- **Integridad**: [Alto/Medio/Bajo] - [Explicar]
- **Disponibilidad**: [Alto/Medio/Bajo] - [Explicar]
- **Impacto económico**: [Estimación]
- **Impacto reputacional**: [Descripción]
- **Impacto legal**: [Posibles sanciones]

**Probabilidad**: [Alta/Media/Baja]

**Nivel de Riesgo**: [Crítico/Alto/Medio/Bajo]



**EJEMPLO COMPLETO**:

#### Riesgo 1: Compromiso de puesto de trabajo por malware

**Descripción**: Un empleado descarga y ejecuta involuntariamente un archivo adjunto malicioso recibido por correo electrónico, instalando malware en su equipo que podría propagarse por la red interna o exfiltrar información sensible.

**Ejemplo real en la organización**: En marzo de 2024, un desarrollador recibió un email aparentemente de un proveedor legítimo con un adjunto ".zip" que contenía un troyano. El antivirus lo bloqueó, pero evidenció la vulnerabilidad del personal ante ataques de ingeniería social.

**Impacto potencial**:
- **Confidencialidad**: Muy Alto - Acceso a código fuente, credenciales almacenadas, datos de clientes
- **Integridad**: Alto - Modificación no autorizada de código, inyección de backdoors
- **Disponibilidad**: Medio - Posible ransomware que bloquee el acceso a archivos locales
- **Impacto económico**: Entre 50.000€ y 200.000€ (recuperación, pérdida de productividad, posibles incumplimientos contractuales)
- **Impacto reputacional**: Alto - Pérdida de confianza de clientes del sector financiero y sanitario
- **Impacto legal**: Sanciones GDPR si se comprometen datos personales (hasta 20M€ o 4% facturación)

**Probabilidad**: Alta - 15 intentos detectados en 6 meses, sector en creciente foco de ataques

**Nivel de Riesgo**: **CRÍTICO**



#### Riesgo 2: [Completar]

[Repetir estructura]

#### Riesgo 3: [Completar]

[Repetir estructura]

### 1.4. Conexión con el Plan Director de Seguridad

> **INSTRUCCIÓN**: Referenciar explícitamente el PDS previo. Mostrar la trazabilidad.

**Referencias al PDS**:
- **Activos críticos identificados**: [Listar IDs o nombres de activos del PDS]
- **Puestos de trabajo analizados**: [Listar puestos del PDS]
- **Riesgos del PDS que mitiga**: [Listar códigos de riesgos: R-01, R-05, etc.]
- **Proyecto del PDS del que deriva**: "Proyecto 3: Implementación de políticas de seguridad del puesto de trabajo"

**EJEMPLO**:
> "Esta política responde directamente al Proyecto P-03 del PDS, identificado como prioritario con una puntuación de 92/100 en la matriz de priorización. Los activos críticos que protege incluyen AC-02 (Portátiles corporativos), AC-05 (Repositorios de código), AC-11 (Credenciales de acceso). Mitiga los riesgos R-01 (Compromiso por malware - Riesgo Crítico), R-03 (Acceso no autorizado - Riesgo Alto), R-07 (Pérdida de dispositivos - Riesgo Alto) y R-12 (Configuraciones inseguras - Riesgo Medio)."

### 1.5. Marco Normativo y Referencias

Esta política se fundamenta en:

- **ISO/IEC 27001:2022**: Controles A.5.15 (Control de acceso), A.8.1 (Dispositivos de usuario final), A.8.4 (Protección contra malware)
- **ENS**: Medidas mp.if.2 (Protección de la confidencialidad), mp.if.3 (Protección de la integridad), mp.eq.1 (Puesto de trabajo)
- **RGPD**: Artículos 5 (Principios), 25 (Protección de datos desde el diseño), 32 (Seguridad del tratamiento)
- **LOPDGDD**: Artículos 28-31 (Medidas de seguridad)
- **Guía INCIBE**: "Política de Protección del Puesto de Trabajo para Pymes"
- **CCN-STIC 417**: Seguridad en equipos informáticos



## 2. Objetivos

### 2.1. Objetivo General

> **INSTRUCCIÓN**: Redactar en 1-2 frases el propósito principal, adaptado a vuestra organización.

**EJEMPLO**:
> "Establecer las medidas de seguridad necesarias para proteger los puestos de trabajo de [Nombre Empresa] frente a amenazas internas y externas, garantizando la confidencialidad, integridad y disponibilidad de la información y los sistemas que soportan nuestra actividad de desarrollo de software para clientes críticos."

### 2.2. Objetivos Específicos

> **INSTRUCCIÓN**: Definir 3-5 objetivos concretos y medibles.

**EJEMPLO**:

1. **Prevenir accesos no autorizados**: Asegurar que solo personal autorizado acceda a información sensible mediante autenticación robusta y gestión adecuada de sesiones.

2. **Minimizar la superficie de ataque**: Reducir vulnerabilidades mediante configuraciones seguras, actualizaciones sistemáticas y desactivación de servicios innecesarios.

3. **Proteger contra código malicioso**: Implementar defensas en capas que detecten, prevengan y neutralicen malware antes de que comprometa la seguridad.

4. **Garantizar continuidad operativa**: Asegurar que los datos críticos pueden recuperarse y que los usuarios pueden continuar trabajando incluso tras un incidente.

5. **Fomentar una cultura de seguridad**: Concienciar y formar al personal para que actúe como primera línea de defensa frente a amenazas.



## 3. Puntos Clave

> **INSTRUCCIÓN**: Desarrollar las medidas principales de la política.
> Adaptarlas específicamente a vuestra organización.
> NO copiar literalmente de los PDFs de INCIBE, sino redactarlas con vuestras palabras
> y adaptadas al contexto específico.

### 3.1. Configuración Segura de Equipos

#### 3.1.1. Estándares de configuración

**Descripción**: [Adaptar a vuestra empresa]

**Aplicable a**: [Especificar]

**Responsable de implementación**: [Departamento IT / Administrador de Sistemas]

**Ejemplo de medida específica**:
> "Todos los equipos de desarrollo (portátiles y estaciones) se configurarán según la baseline de seguridad definida en el documento técnico BS-DEV-001, que incluye: desactivación de puertos USB por defecto (salvo autorización), configuración de firewall local con reglas específicas para entorno de desarrollo, instalación únicamente de software aprobado del catálogo corporativo, y configuración de salvapantallas con bloqueo automático a los 5 minutos en portátiles y 10 minutos en estaciones fijas."

#### 3.1.2. [Otras medidas de configuración]

[Continuar desarrollando]

### 3.2. Control de Acceso Físico y Lógico

[Desarrollar medidas relacionadas con accesos]

### 3.3. Protección contra Malware

[Desarrollar medidas relacionadas con malware]

### 3.4. Actualización y Gestión de Parches

[Desarrollar medidas relacionadas con actualizaciones]

### 3.5. Gestión de Datos en Puestos de Trabajo

[Desarrollar medidas relacionadas con almacenamiento, backups, etc.]

### 3.6. Uso y Gestión de Dispositivos

[Desarrollar medidas para periféricos, dispositivos extraíbles, etc.]

### 3.7. Formación y Concienciación

[Desarrollar programa de formación específico]



## 4. Alcance y Aplicabilidad

### 4.1. Ámbito de Aplicación

> **INSTRUCCIÓN**: Definir claramente qué incluye y qué excluye esta política.

| Elemento        | Incluye   | Excluye   |
|-----------------|-----------|-----------|
| **Personal**    | [Definir] | [Definir] |
| **Equipos**     | [Definir] | [Definir] |
| **Ubicaciones** | [Definir] | [Definir] |
| **Información** | [Definir] | [Definir] |

**EJEMPLO**:

| Elemento        | Incluye                                                                               | Excluye                                                                  |
|-----------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Personal**    | Todos los empleados, contratistas, becarios con asignación de puesto de trabajo       | Visitantes ocasionales, personal de mantenimiento externo                |
| **Equipos**     | Portátiles corporativos, estaciones de trabajo, tablets corporativos asignados        | Dispositivos personales (BYOD), equipos de sala de reuniones compartidos |
| **Ubicaciones** | Oficina central, teletrabajo, oficinas de clientes autorizadas                        | Espacios públicos (cafeterías, aeropuertos) - política específica        |
| **Información** | Toda información corporativa: código fuente, datos de clientes, información comercial | Información pública, datos anonimizados para análisis                    |

### 4.2. Roles y Responsabilidades

> **INSTRUCCIÓN**: Adaptar roles a vuestra organización específica.

| Rol                                | Responsabilidades  |
|------------------------------------|--------------------|
| **Dirección**                      | [Definir]          |
| **Responsable de Seguridad**       | [Definir]          |
| **Departamento IT**                | [Definir]          |
| **Jefes de Proyecto/Departamento** | [Definir]          |
| **Empleados**                      | [Definir]          |



## 5. Medidas de Seguridad Detalladas

> **INSTRUCCIÓN**: Desarrollar aquí las medidas concretas que luego se verificarán en el checklist.
> Deben ser medidas **específicas, claras y verificables**.
> Tener en cuenta que muchas de estas medidas se desarrollarán en otras politicas específicas,
> por lo que aquí deben centrarse en las relacionadas con la protección del puesto de trabajo. Por ejemplo,
> no incluir medidas de gestión de incidentes o auditoría que se desarrollarán en otras políticas.

### 5.1. Medidas de Nivel Básico (Obligatorias)

#### Medida B-01: Bloqueo automático de sesión

**Descripción completa**: [Desarrollar]

**Objetivo**: Prevenir accesos no autorizados cuando el usuario se ausenta

**Procedimiento de implementación**:
1. [Paso específico 1]
2. [Paso específico 2]
3. [...]

**Responsable**: [Rol]

**Verificación**: Checklist control #1.1


#### Medida B-02: [Siguiente medida]

[Continuar con todas las medidas básicas necesarias]


### 5.2. Medidas de Nivel Avanzado (Recomendadas)

[Desarrollar medidas avanzadas]


## 6-13. [Completar las demás secciones de la plantilla]

> **INSTRUCCIÓN**: Seguir la estructura de la PLANTILLA_POLITICA.md y completar todas las secciones:
> - Excepciones
> - Formación
> - Auditoría
> - Gestión de incidentes
> - Revisión
> - Sanciones
> - Glosario
> - Anexos
> - Firmas

---

## Notas para el Desarrollo

**Recordatorios importantes**:

1. ✅ **Trazabilidad**: Referenciar continuamente el PDS - activos, riesgos, puestos identificados
2. ✅ **Especificidad**: Usar nombres reales, números concretos, tecnologías específicas de vuestra empresa
3. ✅ **Coherencia**: Las medidas de esta política deben alinearse con los controles del checklist
4. ✅ **Realismo**: Las medidas deben ser factibles con los recursos de la empresa del caso
5. ✅ **Redacción propia**: NO copiar literalmente de INCIBE, redactar con vuestras palabras
6. ✅ **Justificación**: Cada medida debe justificarse con los riesgos que mitiga

**Estructura recomendada de trabajo**:

1. Revisar a fondo vuestro PDS
2. Identificar activos y riesgos relacionados con puestos de trabajo
3. Analizar los ejemplos de INCIBE para inspiración (NO copiar)
4. Redactar los antecedentes conectándolos con vuestro PDS
5. Definir objetivos alineados con los riesgos
6. Desarrollar puntos clave (medidas) específicas y realistas
7. Crear checklist coherente con las medidas definidas
8. Revisar coherencia entre política y checklist

---

**PRÓXIMO PASO**: Una vez completada esta política, desarrollar las otras 3 políticas siguiendo el mismo nivel de detalle y trazabilidad.