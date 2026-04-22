# Investigación de captura de ram
### Grupo 3

## 1. Compromación de integridad

Usamos Hashrat para obtener los hashes de los archivos obtenidos, y comprobamos que coinciden con los hashes proporcionados.

![alt text](<img/2026-04-15 20_23_27-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Comprobamos que coinciden completamente.

## 2. Obtención del perfil de memoria

El primer paso es averiguar qué versión de kernel tiene el sistema del que se extrajo la memoria. Volatility 3 incluye el plugin `banners.Banners`, que escanea el dump buscando la cadena del banner del kernel.

```
python3 vol.py -f ../../forense/Proyecto\ 5.2/RAM.bin banners.Banners
```

![alt text](<img/2026-04-15 12_18_49-Kali (changed username kali to midex882) [Corriendo] - Oracle VirtualBox.png>)

Con esto, sabemos que tenemos el kernel **4.4.0-1061-aws**, y podemos descargarnos el paquete debug del kernel.

```
wget "http://ddebs.ubuntu.com/pool/main/l/linux-aws/linux-image-4.4.0-1061-aws-dbgsym_4.4.0-1061.70_amd64.ddeb"
```

![alt text](<img/2026-04-15 12_19_51-Kali (changed username kali to midex882) [Corriendo] - Oracle VirtualBox.png>)

Una vez descargado, creamos una carpeta para extraerlo y lo extraemos, y comprobamos que está en su sitio:

![alt text](<img/2026-04-15 12_37_43-Kali (changed username kali to midex882) [Corriendo] - Oracle VirtualBox.png>)

Ahora nos instalaremos dwarf2json, que es una herramienta de volatility foundation para convertir la información del debug del kernel (que tenemos en formato dwarf) al formato que necesita volatility, que es json.

```
sudo apt install golang-go

git clone https://github.com/volatilityfoundation/dwarf2json.git
cd dwarf2json
go build
cd ..

```

Cuando lo tengamos, lo usamos sobre el debug y lo imprimimos en un json:

```
./dwarf2json/dwarf2json linux \
  --elf ./kernel-debug/usr/lib/debug/boot/vmlinux-4.4.0-1061-aws \
  > Ubuntu_16.04-4.4.0-1061-aws.json
```

![alt text](<img/2026-04-15 12_39_09-Kali (changed username kali to midex882) [Corriendo] - Oracle VirtualBox.png>)

Con ello, ya tenemos lo que necesitamos, así que solo queda dárselo a volatility 3:

```
cp Ubuntu_16.04-4.4.0-1061-aws.json \ ~/Desktop/volatility3/volatility3/symbols/linux/
```

Y ya podríamos empezar con el análisis.

## 3. Análisis de la memoria

Podemos, ya que sabemos que se trata de un caso de web defacement, vamos mirar los procesos de apache:

![alt text](<img/2026-04-15 21_05_26-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

No parecen tener anidación extraña, pero vamos a analizarlos con malfind:

![alt text](<img/2026-04-15 21_01_59-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Malfind sí nos dice algo más interesante, y es que hay al menos un proceso con anonymous mapping, que quiere decir que es código que está corriendo sin un archivo que lo respalde, por lo que se trata de código inyectado. Si miramos un poco más, sacamos dos tres más:

![alt text](<img/2026-04-15 21_03_02-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

![alt text](<img/2026-04-15 21_03_23-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Entonces sabemos que sí tenemos código inyectado en el servidor de apache, y hemos confirmado en los access logs que efectivamente se subieron payloads con éxito, pero tenemos un poco limitada la información que podemos sacar.

Por eso, vamos a mirar las conexiones, a ver si hay algo más que podamos identificar.

Entre todo el registro, lo que nos llama la atención (en parte por ser el único registro de red que cuya ip ha sido registrada), son estas entradas de ssh:

![alt text](<img/2026-04-19 18_54_41-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

![alt text](<img/2026-04-19 18_53_42-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

En estos registros, vemos conexiones de (1) ssh con posterior ejecución de comandos con privilegios elevados (2), lo que puede ser muestra de la escalada de privilegios exitosa del atacante.

Sin muchas opciones, podemos buscar todo lo que haya en la memoria relacionado con la ip originaria de la conexión: 23.226.128.37 (3)

![alt text](<img/2026-04-19 18_49_48-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Vemos que hay una cantidad considerable de registros, pero hay múltiples conexiones de la ip objetivo relacionadas con "ganga.site" (la web hosteada en la máquina víctima). 

![alt text](<img/2026-04-19 19_15_53-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Si esto fue en algún momento una web pública, ya no lo es, pero podemos ver qué más hay en memoria sobre este sitio:

![alt text](<img/2026-04-19 19_21_28-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Y lo que encontramos son varios escaneos a la web usando wpscan, por parte de otra dirección ip 94.242.54.22.

Entre la infinidad de registros, también encontramos un registro de subida usando el plugin reflex gallery de wordpress

![alt text](<img/2026-04-19 19_30_55-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Esto es llamativo porque reflex gallery contiene una vulnerabilidad conocida, CVE-2015-4133 (Reflex Gallery Arbitrary File Upload), así que vamos a buscar por las ocurrencias de ese plugin:

![alt text](<img/2026-04-19 19_34_23-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Y vemos subidas tanto de la ip 94.242.54.22, identificada como potencial atacante, como de otra ip más, la 88.0.112.115.

Es probable que con esto tengamos un registro suficiente de cómo de llevó a cabo el web defacement.

## 4. Tabla de evidencias

> Los campos MAC time, tamaño y hash no son directamente recuperables para
> artefactos residentes en RAM. Se indica la región de memoria y el método
> de obtención de cada evidencia.

| ID | Artefacto | Región / Proceso | Timestamp inferido | Plugin / Método | Descripción |
|---|---|---|---|---|---|
| RAM-01 | Volcado `RAM.bin` — integridad verificada | Archivo entregado | 24/07/2018 ~05:26 UTC | Hashrat | Hash MD5/SHA1 verificado y coincidente con el proporcionado. Base de toda la investigación |
| RAM-02 | Banner del kernel `4.4.0-1061-aws` | Región del kernel | — | `banners.Banners` | Identifica el sistema como Ubuntu 16.04, kernel AWS. Necesario para construir el perfil de símbolos con dwarf2json |
| RAM-03 | Árbol de procesos Apache — PID 27428 + 9 workers | Tabla de procesos | — | `linux.psaux` | 10 procesos Apache activos. Estructura padre-hijo sin anidación anómala visible en el árbol de procesos |
| RAM-04 | Cadena de adquisición: `sshd` → `bash` → `sudo` → `insmod lime` | Tabla de procesos | 24/07/2018 05:24–05:26 UTC | `linux.psaux` | Evidencia directa del proceso de toma del volcado. El usuario `ubuntu` compiló e insertó LiME desde sesión SSH activa desde `23.226.128.37` |
| RAM-05 | Anonymous mappings (`rwx`) en workers Apache PIDs 6262, 6266, 6281, 6285 | Regiones de memoria de procesos Apache | — | `linux.malfind` | Código ejecutándose sin archivo de respaldo en disco. Indicador de código inyectado activo en el proceso Apache en el momento del volcado |
| RAM-06 | Registros de conexión SSH de `23.226.128.37` con ejecución de comandos privilegiados | Page cache de `auth.log` | 20/07/2018 y 24/07/2018 | `strings` + grep | Acceso SSH con clave RSA `SHA256:Q27pW6...`. El 24/07 ejecuta `apt install make`, `apt install gcc` e `insmod` con `sudo`. Descartado como actividad del atacante — corresponde al investigador |
| RAM-07 | Escaneo WPScan `v2.9.5-dev` desde `94.242.54.22` | Page cache del access log de Apache | 23/07/2018 11:08–11:19 UTC | `strings` + grep (búsqueda por `ganga.site`) | Enumeración activa de plugins, temas, rutas de configuración, posibles volcados SQL y credenciales. Confirma presencia del plugin Reflex Gallery v3.1.3 mediante descarga de `readme.txt` (8632 bytes) |
| RAM-08 | Subida de archivos PHP vía `FileUploader/php.php` — IPs `94.242.54.22` y `88.0.112.115` | Page cache del access log de Apache | 23/07/2018 11:20–11:54 UTC | `strings` + grep (búsqueda por `reflex-gallery`) | Subidas de `PSMOfbPom.php`, `yDdoSpsx.php`, `XLPYhlEtQOyiMKb.php` (desde `94.242.54.22`) y `vmGAbaiewrSSuMs.php`, `PLoeJFOEVoc.php` (desde `88.0.112.115`) mediante explotación de CVE-2015-4133 |
| RAM-11 | Traza de ejecución `eval()'d code` de `vmGAbaiewrSSuMs.php` | Heap PHP dentro de proceso Apache | — | `strings` + grep | `/var/www/html/wordpress/wp-content/uploads/2018/07/vmGAbaiewrSSuMs.php(1) : eval()'d code` — confirma ejecución activa del payload en el contexto de Apache |
| RAM-14 | Conexión SSH ESTABLISHED `172.31.47.60:22 ↔ 23.226.128.37:42760` | Tabla de sockets del kernel | 24/07/2018 05:24 UTC | `linux.sockstat` | Única conexión TCP activa con IP externa en el momento del volcado. Corresponde al investigador, no al atacante |


## 5. Pruebas con resultado negativo

| Prueba | Resultado | Observación |
|---|---|---|
| Proceso ssh con permisos altos | No concluyente | Se identificó, por medio de pstree, un proceso anidado con el último hijo como insmod, usado para cargar módulos de kernel (Figura 1). Se concluyó que se trataba de parte de la preparación del laboratorio.
| Identificación del LHOST del C2 en memoria | **No concluyente** | La IP del servidor de Metasploit no aparece de forma aislada en los strings analizados. Podría recuperarse con análisis binario de las regiones `rwx` volcadas por `malfind` |
| `linux.psaux`: procesos maliciosos independientes | **Negativo** | No se encontró ningún proceso de sistema anómalo fuera de los workers Apache. El payload operó enteramente dentro del contexto del proceso Apache |



![alt text](<img/2026-04-15 19_59_22-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

(Figura 1) Arbol del proceso anidado insmod

**Nota**: Algunas de estas pruebas han sido no concluyentes o negativas por falta de información. El análisis de disco más profundo puede permitir una correlación mejor.

## 6. Conclusión preliminar.


El 23 de julio de 2018, un atacante identificó el plugin vulnerable Reflex Gallery 3.1.3 en el WordPress de ganga.site mediante navegación manual y WPScan, y explotó CVE-2015-4133 para subir archivos PHP sin autenticación.

| Hora UTC | IP           | Evento                                                                                                                                                                                                    |
| -------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10:26:45 | 94.242.54.22 | Navegación manual con Chrome (Windows 7 x64). Carga la portada y descarga los assets de Reflex Gallery — identifica el plugin visualmente                                                                 |
| 10:51:52 | 94.242.54.22 | Segunda visita, ahora con Firefox 54 en Ubuntu Linux x64 — cambia de User-Agent, probable cambio de entorno o de herramienta                                                                              |
| 11:08:46 | 94.242.54.22 | Lanza WPScan v2.9.5-dev — enumera plugins, temas, archivos de configuración, volcados SQL, readme.html, credenciales expuestas. Descarga reflex-gallery/readme.txt (8632 bytes) confirmando versión 3.1.3 |
| 11:12:04 | 94.242.54.22 | Primer intento de subida fallido/incompleto vía FileUploader/php.php                                                                                                                                      |
| 11:25:35 | 88.0.112.115 | Nueva IP. Sube dos archivos                                                        |
| 11:53:31 | 88.0.112.115 | Descarga reflex-gallery/readme.txt — verificación o preparación para la siguiente subida                                                                                                                  |
                                                                                                                                                                