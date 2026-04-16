# Proyecto 5b AF: Análisis de disco

# Memoria de Trabajo — Análisis Forense de Imagen de Disco

## 1. Información del Caso

| Campo              | Valor                          |
|--------------------|-------------------------------|
| Analista           | Abel García Domínguez          |
| Fecha de inicio    | 15/04/2026                     |
| Hora de inicio     | [12:10] CEST                  |
| Nombre del caso    | Análisis de Imagen de Disco    |
| Identificador      | Disc.E01                       |
| Herramientas usadas| [Completar según avance]       |

---

## 2. Adquisición y Verificación de la Evidencia

### 2.1 Descarga del archivo

- **Archivo recibido:** `Disc.E01.zip`
- **Fuente:** Moodle 
- **Fecha y hora de descarga:** 15/04/2026 — [12:12] CEST

### 2.2 Descompresión

Descomprimimos el archivo `Disc.E01.zip`.

- **Archivo resultante:** `Disc.E01`
- **Tamaño de la imagen (Size):**      983.1 MiB (1,030,873,131 bytes)
- **Tamaño en disco (Size on Disk):**  983.1 MiB (1,030,881,280 bytes)

### 2.3 Verificación de integridad mediante hashes

Se procedió al cálculo de los valores hash de la imagen forense con el objetivo de verificar
su integridad respecto a los valores proporcionados por el docente/proveedor.

#### Hashes calculados

```bash
md5sum Disc.E01
sha1sum Disc.E01
```

| Algoritmo | Hash calculado                          | Hash proporcionado                      | 
|-----------|-----------------------------------------|-----------------------------------------|
| MD5       | bac5561328b477f0508fab7c5d9ee0a6  | bac5561328b477f0508fab7c5d9ee0a6  | 
| SHA1      | 5b0a9cc8ff4ebd5aa3e1e36d8713e3b24b072e79 | 5b0a9cc8ff4ebd5aa3e1e36d8713e3b24b072e79  | 

![img](img/hashes.png)

> **Conclusión:** La integridad de la imagen ha sido verificada.


---

## 3. Análisis

### 3.1 Herramientas utilizadas

El análisis de la imagen forense `Disc.E01` se ha llevado a cabo utilizando **dos herramientas de forma paralela e independiente**, con el objetivo de maximizar la cobertura de artefactos y validar los hallazgos mediante contraste entre fuentes:

| Herramienta    | Versión       | Plataforma  | Función principal |
|----------------|---------------|-------------|-------------------|
| **Autopsy**    | 4.22.1  | Windows | Análisis completo: módulos de ingest, timeline, artefactos del sistema, archivos eliminados |
| **FTK Imager** | 4.7.3.81   | Windows     | Exploración directa del sistema de archivos, extracción de artefactos, verificación de hashes, extracción de MFT |

### **Hallazgo 1: Registros de Acceso del Servidor Web Apache**

Al examinar el archivo `/var/log/apache2/access.log` se detectaron
peticiones al plugin `reflex-gallery`. La respuesta `200 OK` al fichero
`readme.txt` del plugin expuso la versión instalada (**ReFlex Gallery 3.1.3**),
que tras consultar NVD y Exploit-DB resultó estar afectada por **CVE-2015-4133**
(*Unrestricted File Upload*, sin autenticación requerida).

![img](img/log1.png)

En el log se identificó un escaneo previo con **WPScan v2.9.5-dev** desde
`94.242.54.22` a las `11:08`, seguido de la explotación a las `11:20` mediante
POST al endpoint vulnerable `php.php`. Las peticiones GET inmediatas a los
archivos subidos devolvieron `HTTP 200`, confirmando la ejecución de las
webshells. A las `11:54`, una segunda IP (`88.0.112.115`) repitió el mismo ataque.

![img](img/log2.png)

![img](img/reflex-gallery.png)



