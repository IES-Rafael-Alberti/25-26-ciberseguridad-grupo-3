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
cp Ubuntu_16.04-4.4.0-1061-aws.json \
   ~/Desktop/volatility3/volatility3/symbols/linux/
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

## 4. Conclusión preliminar.

Entonces, de momento, sabemos qué:

El 23 de julio de 2018, un atacante subió tres webshells PHP (PSMOfbPom.php, yDdoSpsx.php, XLPYhlEtQOyiMKb.php) mediante el endpoint FileUploader/php.php explotando una vulnerabilidad de subida de archivos sin autenticación. Posteriormente, se ejecutó vmGAbaiewrSSuMs.php, cuya ejecución activa quedó confirmada en el volcado de memoria RAM mediante la presencia del agente PHP Meterpreter cargado, incluyendo todas las funciones stdapi_* del módulo de control remoto de Metasploit.