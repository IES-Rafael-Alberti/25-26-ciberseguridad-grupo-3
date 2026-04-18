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

Podemos, ya que sabemos que se trata de un caso de web defacement, y ya que sabemos por el [analisis de disco](./investigacion_disco.md) y el access.log, que ha habido llamadas al servidor de apache, vamos mirar los procesos de apache:

![alt text](<img/2026-04-15 21_05_26-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

No parecen tener anidación extraña, pero vamos a analizarlos con malfind:

![alt text](<img/2026-04-15 21_01_59-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Malfind sí nos dice algo más interesante, y es que hay al menos un proceso con anonymous mapping, que quiere decir que es código que está corriendo sin un archivo que lo respalde, por lo que se trata de código inyectado. Si miramos un poco más, sacamos dos tres más:

![alt text](<img/2026-04-15 21_03_02-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

![alt text](<img/2026-04-15 21_03_23-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Entonces sabemos que sí tenemos código inyectado en el servidor de apache, y hemos confirmado en los access logs que efectivamente se subieron payloads con éxito, pero tenemos un poco limitada la información que podemos sacar.

Por esos mismos access logs, conocemos los nombres de los archivos subidos: 

| Archivo             | IP atacante  | Timestamp (UTC)     | POST (subida)                                          | GET (ejecución)                                              | Estado             |
| ------------------- | ------------ | ------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | ------------------ |
| PSMOfbPom.php       | 94.242.54.22 | 23/07/2018 11:20:26 | POST FileUploader/php.php?Year=2018&Month=07 → HTTP 55 | GET /wp-content/uploads/2018/07/PSMOfbPom.php → HTTP 2       | Subido y ejecutado |
| yDdoSpsx.php        | 94.242.54.22 | 23/07/2018 11:23:04 | POST FileUploader/php.php?Year=2018&Month=07 → HTTP 54 | GET /wp-content/uploads/2018/07/yDdoSpsx.php → HTTP 2        | Subido y ejecutado |
| XLPYhlEtQOyiMKb.php | 94.242.54.22 | 23/07/2018 11:23:56 | POST FileUploader/php.php?Year=2018&Month=07 → HTTP 61 | GET /wp-content/uploads/2018/07/XLPYhlEtQOyiMKb.php → HTTP 2 | Subido y ejecutado |
| vmGAbaiewrSSuMs.php | 88.0.112.115 | 23/07/2018 11:25:35 | POST FileUploader/php.php?Year=2018&Month=07 → HTTP 61 | GET /wp-content/uploads/2018/07/vmGAbaiewrSSuMs.php → HTTP 2 | Meterpreter activo |
| PLoeJFOEVoc.php     | 88.0.112.115 | 23/07/2018 11:54:34 | POST FileUploader/php.php?Year=2018&Month=07 → HTTP 57 | GET /wp-content/uploads/2018/07/PLoeJFOEVoc.php → HTTP 2     | Subido y ejecutado |

Vamos a hacer una búsqueda en strings de estos archivos:

![alt text](<img/2026-04-16 13_36_16-access.log_ Bloc de notas.png>)

Y aquí tenemos varios puntos de los que hablar:

- Puntos 1 y 2 Tenemos aquí el rastro de la subida de algunos de los archivos.
- Punto 3 vemos rastros de ejecución.

Vamos a analizar mejor.

Primero, tenemos las líneas que incluyen el "Content-Disposition" nos cuentan la subida de cada archivo:

![alt text](<img/2026-04-16 13_40_57-Kali (Volatility 3 installed) [Corriendo] - Oracle VirtualBox.png>)

Después, tenemos el path traversal:

![alt text](<img/2026-04-16 13_41_48-Kali (Volatility 3 installed) [Corriendo] - Oracle VirtualBox.png>)

Los cinco `../` navegan desde la carpeta del plugin hasta la raíz de WordPress para calcular la ruta de destino del archivo subido.

Respuesta JSON del servidor confirmando la subida:
```
{"success":true,"fileName":"\\/2018\\/07\\/vmGAbaiewrSSuMs.php"}
```

![alt text](<img/2026-04-16 13_42_32-Kali (Volatility 3 installed) [Corriendo] - Oracle VirtualBox.png>)

Por último, tenemos trazas de meterpreter en las líneas que contienen **stdapi**.

![alt text](<img/2026-04-16 13_44_19-Kali (Volatility 3 installed) [Corriendo] - Oracle VirtualBox.png>)

Las stdapi_* son los comandos del módulo stdapi de Meterpreter. 

Vamos teniendo una idea de cual fue la línea de eventos. Vamos a hacer un analisis de conexiones para confirmar la ip del atacante.

![alt text](<img/2026-04-16 14_18_52-Kali (Volatility 3 installed) [Corriendo] - Oracle VirtualBox.png>)

Pero por desgracia, no parece haber constancia de cuales fueron las ips que realizaron las conexiones, al menos en memoria. El análsis de disco nos podrá decir más.

## 4. Tabla de evidencias

> Los campos MAC time, tamaño y hash no son recuperables directamente desde un
> volcado de memoria para artefactos de RAM (no son archivos en disco).
> Se indica la fuente de cada evidencia y el método de obtención.

| ID | Nombre / Artefacto | Localización en RAM | MAC time | Tamaño | Hash | Fuente / Método | Descripción |
|---|---|---|---|---|---|---|---|
| RAM-01 | `RAM.bin` | Archivo de volcado entregado | — | — | MD5/SHA1 verificados con Hashrat ✓ | Comprobación de integridad | Volcado de memoria del servidor. Hash coincide con el proporcionado por el perito |
| RAM-02 | Kernel banner `4.4.0-1061-aws` | Región de memoria del kernel | — | — | — | `banners.Banners` | Identifica el sistema operativo como Ubuntu 16.04 con kernel AWS. Necesario para construir el perfil de símbolos |
| RAM-03 | Árbol de procesos Apache (PID 27428 + workers) | Tabla de procesos en memoria | — | — | — | `linux.psaux` | 9 workers de Apache activos (PIDs 5573, 5763, 6196, 6262, 6266, 6281, 6285, 6286, 6287, 9054). Estructura de procesos padre-hijo normal. Sin anidación anómala |
| RAM-04 | Proceso `sshd` → `bash` → `sudo` → `insmod lime` | Tabla de procesos en memoria | — | — | — | `linux.psaux` | Cadena PID 1340→9055→9118→9126→14088→14089. Evidencia de que el volcado fue realizado por el usuario `ubuntu` mediante LiME desde sesión SSH |
| RAM-05 | Anonymous mappings en workers Apache | Regiones de memoria de PIDs 6262, 6266, 6281, 6285 | — | — | — | `linux.malfind` | Código ejecutándose sin archivo de respaldo en disco (anonymous mapping). Indicador de código inyectado. Permisos `rwx` |
| RAM-06 | Petición multipart de subida — `XLPYhlEtQOyiMKb.php` | Buffer HTTP de worker Apache en RAM | 23/07/2018 ~11:23 | — | — | `strings` + grep | Fragmento del POST capturado en caché: `Content-Disposition: form-data; name="qqfile"; filename="XLPYhlEtQOyiMKb.php"`. Confirma subida via `multipart/form-data` |
| RAM-07 | Petición multipart de subida — `vmGAbaiewrSSuMs.php` | Buffer HTTP de worker Apache en RAM | 23/07/2018 ~11:25 | — | — | `strings` + grep | `Content-Disposition: form-data; name="qqfile"; filename="vmGAbaiewrSSuMs.php"` |
| RAM-08 | Petición multipart de subida — `PLoeJFOEVoc.php` | Buffer HTTP de worker Apache en RAM | 23/07/2018 ~11:54 | — | — | `strings` + grep | `Content-Disposition: form-data; name="qqfile"; filename="PLoeJFOEVoc.php"` |
| RAM-09 | Path traversal del exploit | Buffer HTTP en RAM | — | — | — | `strings` + grep | Cadena `../../../../../uploads/2018/07/[archivo].php` presente para los 5 archivos. Huella del módulo `wp_reflexgallery_file_upload` de Metasploit |
| RAM-10 | Respuesta JSON de subida exitosa | Buffer HTTP de worker Apache en RAM | — | — | — | `strings` + grep | `{"success":true,"fileName":"\\/2018\\/07\\/vmGAbaiewrSSuMs.php"}` presente 3 veces. Confirmación del servidor de que la subida fue aceptada |
| RAM-11 | Ruta completa de `vmGAbaiewrSSuMs.php` con `eval()'d code` | Región de memoria PHP (proceso Apache) | — | — | — | `strings` + grep | `/var/www/html/wordpress/wp-content/uploads/2018/07/vmGAbaiewrSSuMs.php(1) : eval()'d code`. Confirma ejecución activa del payload en el momento del volcado |
| RAM-12 | Cadena de `eval()` anidados — capa 2 en línea 434 | Región de memoria PHP (proceso Apache) | — | — | — | `strings` + grep | `vmGAbaiewrSSuMs.php(1) : eval()'d code(434) : eval()'d code`. Estructura de doble desofuscación del PHP Meterpreter de Metasploit |
| RAM-13 | Funciones `stdapi_*` del módulo Meterpreter | Región de memoria PHP en offset `0x7f065b6a....` | — | — | — | `strings` + grep | 30+ funciones identificadas: `stdapi_fs_*`, `stdapi_sys_*`, `stdapi_net_*`, `channel_create_*`. El agente Meterpreter estaba completamente cargado en memoria |
| RAM-14 | Funciones del loader inicial — `file_get_contents` y `socket_set_option` | Offset `0x7f065b696721` y `0x7f065b6967bc` | — | — | — | `strings` + grep | Pertenecen a la capa 1 del payload. Usadas para establecer la conexión reversa al C2 antes de cargar el Meterpreter completo |
| RAM-15 | Conexión SSH activa `172.31.47.60:22 ↔ 23.226.128.37:42760` | Tabla de sockets del kernel | — | — | — | `linux.sockstat` | Única conexión TCP ESTABLISHED con IP externa en el momento del volcado. Corresponde a la sesión SSH del investigador, no al atacante |
| RAM-16 | Rutas de los 5 archivos PHP en `/uploads/2018/07/` | Múltiples regiones del heap de Apache | — | — | — | `strings` + grep | Todas las rutas absolutas `/var/www/html/wordpress/wp-content/uploads/2018/07/[archivo].php` presentes en memoria para los 5 archivos subidos |

## 5. Pruebas con resultado negativo

| Prueba | Resultado | Observación |
|---|---|---|
| Proceso ssh con permisos altos | No concluyente | Se identificó, por medio de pstree, un proceso anidado con el último hijo como insmod, usado para cargar módulos de kernel (Figura 10). Se concluyó que se trataba de parte de la preparación del laboratorio.
| `linux.sockstat`: búsqueda de conexión TCP activa del Meterpreter | **Negativo** | No hay ninguna conexión ESTABLISHED hacia IP externa sospechosa. La sesión Meterpreter ya había concluido antes del volcado |
| Identificación del LHOST del C2 en memoria | **No concluyente** | La IP del servidor de Metasploit no aparece de forma aislada en los strings analizados. Podría recuperarse con análisis binario de las regiones `rwx` volcadas por `malfind` |
| `linux.psaux`: procesos maliciosos independientes | **Negativo** | No se encontró ningún proceso de sistema anómalo fuera de los workers Apache. El payload operó enteramente dentro del contexto del proceso Apache |



![alt text](<img/2026-04-15 19_59_22-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

(Figura 10) Arbol del proceso anidado insmod

**Nota**: Algunas de estas pruebas han sido no concluyentes o negativas por falta de información. El análisis de disco más profundo puede permitir una correlación mejor.

## 6. Conclusión preliminar.

Entonces, de momento, sabemos qué:

El 23 de julio de 2018, un atacante subió tres webshells PHP (PSMOfbPom.php, yDdoSpsx.php, XLPYhlEtQOyiMKb.php) mediante el endpoint FileUploader/php.php explotando una vulnerabilidad de subida de archivos sin autenticación. Posteriormente, se ejecutó vmGAbaiewrSSuMs.php, cuya ejecución activa quedó confirmada en el volcado de memoria RAM mediante la presencia del agente PHP Meterpreter cargado, incluyendo todas las funciones stdapi_* del módulo de control remoto de Metasploit.