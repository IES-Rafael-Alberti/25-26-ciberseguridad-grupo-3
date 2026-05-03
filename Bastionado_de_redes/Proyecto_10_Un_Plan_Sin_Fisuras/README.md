# 🛡️ Proyecto 10 — Análisis de Riesgos con PILAR
### Grupo 3 · Bastionado de Redes y Sistemas

> **Archivos principales del proyecto:**
> - 📁 [`PILAR/Proyecto_10_G3.mgr`](PILAR/Proyecto_10_G3.mgr) — Proyecto PILAR con el análisis completo
> - 📄 [`PILAR/Analisis_Riesgos.docx`](PILAR/Analisis_Riesgos.docx) — Informe de análisis de riesgos exportado
> - 📘 [`pdf/470I1 PILAR Guía CCN-STIC.pdf`](pdf/470I1%20PILAR%20Guía%20CCN-STIC.pdf) — Manual oficial CCN-STIC seguido durante el proyecto

---

## 👥 Equipo

| Nombre |
|---|
| Abel García Domínguez |
| José María Escalón Prada |
| David Jiménez Ruiz |

---

## 📋 Fundamentación Teórica

A lo largo del curso hemos visto muchas medidas que podemos aplicar en el bastionado de redes y sistemas. Pero lo difícil no es conocerlas — lo realmente complicado es saber **cuándo tenemos que parar**, cuándo tenemos una seguridad suficiente en el contexto de nuestra empresa u organización.

La herramienta correcta para responder a esa pregunta es el **análisis de riesgos**. A través del mismo conoceremos las amenazas a las que estamos sometidos y evaluaremos el riesgo. Si lo hacemos correctamente, conoceremos cuál es el **punto mínimo suficiente** para asegurar nuestras redes y sistemas, sin olvidar que el proceso siempre será continuo.

### Metodología MAGERIT

**MAGERIT** fue elaborada por el Consejo Superior de Administración Electrónica del Gobierno de España para minimizar los riesgos de la implantación y uso de las Tecnologías de la Información, enfocada a las Administraciones Públicas.

### Herramienta PILAR

Para aplicar MAGERIT de forma práctica, el **Centro Criptológico Nacional (CCN)** desarrolló la herramienta [PILAR](https://www.ccn-cert.cni.es/es/soluciones-seguridad.html). Esta herramienta guía al analista paso a paso a través de la metodología, permitiendo:

- Inventariar y valorar activos
- Identificar amenazas y calcular su impacto y riesgo
- Comparar la situación actual (*current*) con el objetivo (*target*)
- Exportar informes detallados en múltiples formatos

---

## 🎯 Objetivos del Proyecto

1. **Evaluar** el nivel actual de ciberseguridad en la organización e identificar las áreas de mejora más relevantes en relación con los principios de la **Economía Circular**.
2. **Identificar y priorizar** las medidas técnicas de seguridad a implementar.
3. **Diseñar un plan de acción** de ciberseguridad que aborde las áreas de mejora identificadas.

---

## 🏢 Descripción del Supuesto Empresarial

El análisis parte del contexto de una **PYME** con los siguientes activos principales:

| ID | Activo | Categoría |
|---|---|---|
| ID-0001 | Datos Personales | Información |
| ID-0002 | Información de Clientes y Proveedores | Información |
| ID-0003 | Servidor de Archivos | Servidores y Hardware |
| ID-0004 | Servidor de Correos | Servidores y Hardware |
| ID-0005 | Equipos de Usuario | Servidores y Hardware |
| ID-0006 | Red Corporativa | Red e Infraestructura |
| ID-0007 | Sistema de Backups | Software y Aplicaciones |
| ID-0008 | Aplicaciones CRM/ERP | Software y Aplicaciones |
| ID-0009 | Página Web | Servicios |
| ID-0010 | Servicios en la Nube | Servicios |

---

## 📊 Estructura del Análisis

El análisis se ha realizado en las siguientes fases:

```
Potencial  →  Current (situación actual)  →  Target (objetivo)
```

- **Potencial**: riesgo máximo sin ninguna salvaguarda aplicada
- **Current**: riesgo real considerando los controles actualmente implantados
- **Target**: riesgo objetivo tras implementar las mejoras propuestas

El marco normativo de referencia utilizado es el **ENS (Esquema Nacional de Seguridad)** en categoría **Media (M)**, acorde al perfil de la empresa.

---

## ⚠️ Principales Riesgos Identificados

Los tres riesgos más críticos (riesgo > 6,0) identificados en la fase *current*:

| Amenaza | Activo | Dimensión | Riesgo |
|---|---|:---:|:---:|
| E.21 Errores de mantenimiento SW | CRM/ERP | C | `{6,9}` |
| A.22 Manipulación de programas | CRM/ERP | I, C | `{6,5}` |
| A.8 Difusión de software dañino | CRM/ERP | D, I, C | `{6,3}` |

> El **CRM/ERP** y el **Sistema de Backups** son los activos más críticos del análisis.

---

## 🗂️ Estructura del Repositorio

```
📦 Proyecto_10_G3/
├── 📁 PILAR/
│   ├── Proyecto_10_G3.mgr        ← Archivo de proyecto PILAR
│   └── Analisis_Riesgos.docx     ← Informe exportado (R.tpl → Análisis de riesgos)
├── 📁 pdf/
│   └── 470I1 PILAR Guía CCN-STIC.pdf  ← Manual CCN-STIC consultado
├── 📁 defensa/
│   ├── abel_garcia.md            ← Registro de tareas de Abel
│   ├── josemaria_escalon.md      ← Registro de tareas de José María
│   └── david_jimenez.md          ← Registro de tareas de David
└── README.md
```

---

## 📅 Registro de Trabajo

El reparto de tareas y el registro diario de cada miembro se encuentra en la carpeta [`defensa/`](defensa/), con un archivo `.md` por integrante del grupo donde se indica la fecha y las tareas realizadas cada día.

---

## 📚 Referencias

- [MAGERIT v3 — Metodología de Análisis y Gestión de Riesgos](https://administracionelectronica.gob.es/pae_Home/pae_Metodologia/pae_Magerit.html)
- [CCN-CERT — Soluciones de Seguridad](https://www.ccn-cert.cni.es/es/soluciones-seguridad.html)
- [Manual PILAR — CCN-STIC 470I1](https://www.ccn-cert.cni.es/pdf/guias/series-ccn-stic/guias-de-acceso-publico-ccn-stic/2841-ccn-stic-470i1-pilar-manual-de-usuario-v7-1/file.html)
- [Real Decreto 311/2022 — Esquema Nacional de Seguridad](https://www.boe.es/eli/es/rd/2022/05/03/311)

---

<p align="center">
  <sub>Proyecto realizado con fines educativos · Licencia temporal CCN · No distribuir</sub>
</p>
