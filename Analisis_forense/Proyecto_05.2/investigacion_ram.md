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

Para empezar, vamos a hacer un pstree para observar procesos anidados sospechosos, y sacamos una serie de procesos inusualmente anidados:

![alt text](<img/2026-04-15 19_59_22-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Vamos a sacar algo más de información con pslist:

![alt text](<img/2026-04-15 20_03_59-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Confirmamos la anidación y tenemos una secuencia extraña de escalada:

sshd (1340) -> sshd (9055) -> sshd (9118) -> bash (9126) -> sudo (14088) -> insmod (14089)

Ahora, esto no tiene por qué ser especialmente sospechoso hasta el último paso, que se trata de un proceso de carga de un kernel con privilegio de root completo.

me cago en la leche

_______________________________

Podemos, ya que sabemos que se trata de un caso de web defacement, mirar los procesos de apache:

![alt text](<img/2026-04-15 21_05_26-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

No parecen tener anidación extraña, pero vamos a analizarlos con malfind:

![alt text](<img/2026-04-15 21_01_59-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

Malfind sí nos dice algo más interesante, y es que hay al menos un proceso con anonymous mapping, que quiere decir que es código que está corriendo sin un archivo que lo respalde, por lo que se trata de código inyectado. Si miramos un poco más, sacamos dos tres más:

![alt text](<img/2026-04-15 21_03_02-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)

![alt text](<img/2026-04-15 21_03_23-kali-linux-2025.4-virtualbox-amd64 (after upgrade 2) [Corriendo] - Oracle Virtua.png>)
