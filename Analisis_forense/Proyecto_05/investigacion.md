# Investigación del incidente
### Grupo 3

## Compromación de integridad

Usamos powershell para obtener los hashes de los archivos obtenidos, y comprobamos que coinciden con los hashes del archivo [hashes_256.txt]("evidence/hashes_sha256.txt")

![alt text](<img/2026-04-13 19_48_18-Windows PowerShell.png>)

## 1. Identificar la vulnerabilidad en la aplicación web que fue explotada por el atacante.

Revisamos el archivo access.log de apache, y vimos varias interacciones con el archivo ping.php:

![alt text](<img/2026-04-13 19_12_08-access.log_ Bloc de notas.png>)

Así que miramos qué es:

![alt text](<img/2026-04-13 19_13_44-Exterro FTK Imager 8.2.0.26.png>)

Y vemos que contiene código sencillo:

![alt text](<img/2026-04-13 19_15_01-ping.php - Proyecto 5 - Incident on Linux Server I - Visual Studio Code.png>)

Buscando un poco en internet, vemos que se trata de una vulnerabilidad web conocida. El archivo presenta una vulnerabilidad de OS Command Injection (CWE-78), una de las más críticas en aplicaciones web. Miramos la línea 19:

```
echo(system('ping -c 1 ' . $_POST['ping']));
```

El valor de ```$_POST['ping']``` se concatena directamente en un comando del sistema operativo sin ningún tipo de sanitización ni validación. La función system() de PHP ejecuta ese string directamente en la shell del servidor.

Para explotar esto, un atacante puede inyectar operadores de encadenamiento de comandos en el campo IP del formulario, como por ejemplo:

```
127.0.0.1; whoami
127.0.0.1 && cat /etc/passwd
127.0.0.1 | ls -la /var/www
127.0.0.1 `id`
```

En lugar de ejecutar solo ping -c 1 127.0.0.1, el servidor ejecutaría el comando extra con los mismos privilegios del proceso web. Esto puede llevar a exfiltración de datos, lectura de archivos sensibles o incluso una reverse shell completa. Esto puede tratarse del CWE-78, pero es dificil de asociar con un CVE concreto, aunque lo más probable es que se trate del CVE-2012-1823.

En este caso, se sospecha que se usó para ejecutar código que permitió hacer un dump de contraseñas.

## 2. Determinar la IP, el cliente y el sistema operativo utilizado por el atacante durante el ataque.

Al revisar el access.log, vemos claramente las conexiones realizadas al servidor:

![alt text](<img/2026-04-13 19_18_13-access.log_ Bloc de notas.png>)

Por lo que podemos concluir los siguientes datos:

| Campo             | Valor                                   |
| ----------------- | --------------------------------------- |
| IP atacante       | 192.168.1.6                             |
| Navegador         | Firefox 78.0 ESR                        |
| Sistema operativo | Linux x86_64 (probablemente Kali Linux) |

## 3. Descubrir qué datos fueron exfiltrados del servidor comprometido.

Sospechamos que la vulnerabilidad se usó para ejecutar código que permitió hacer un dump de contraseñas, dado que hay un archivo con un muy evidente dump de contraseñas llamado *passwd.txt* al lado de ping.php:

![alt text](<img/2026-04-13 19_16_21-Exterro FTK Imager 8.2.0.26.png>)

El contenido es el siguiente:

![alt text](<img/2026-04-13 19_16_58-passwd.txt_ Bloc de notas.png>)

Al revisar la fehca de modificación del archivo, vemos que cuadra con los eventos registrados en el log de apache:

![alt text](<img/2026-04-13 19_38_25-Propiedades_ passwd.txt.png>)

Si hacemos un strings a la memoria, obtenemos lo que probablemente son los parámetros que usó el atacante para crear el archivo en primer lugar y para posteriormente traerlo:

![alt text](<img/2026-04-14 09_19_12-Kali (changed username kali to midex882) [Corriendo] - Oracle VirtualBox.png>)

Además, se sospecha la conexión (o el intento de) al servicio de samba del servidor, ya que existe un log de samba con la ip del atacante:

![alt text](<img/2026-04-13 19_35_45-Exterro FTK Imager 8.2.0.26.png>)

Aunque este está vacío

## 4. Analizar por qué el archivo original no muestra actividad durante el incidente.

El archivo original no tiene actividad porque no se alteró ni borró de ninguna manera. El comando cat solo muestra su contenido, y ello no deja registro. Solo tenemos constancia de la modificiación del *passwd.txt*

## 5. Proponer soluciones para reparar la vulnerabilidad explotada.


### 1. Eliminar el backdoor inmediatamente

El primer paso es borrar el webshell del servidor, es decir, eliminar ping.
php.

### 2. Actualización de xampp

La solución definitiva es actualizar PHP a una versión >= 5.3.12 o >= 5.4.2. Si XAMPP está desactualizado, actualizar el stack completo

### 3. Desactivar php cgi

Si no es posible actualizar inmediatamente, como mitigación temporal se puede deshabilitar PHP-CGI en Apache y usar mod_php en su lugar, ya que CVE-2012-1823 solo afecta al modo CGI, que es el Common Gateway Interface, una interfaz estándar que permite a un servidor web como Apache comunicarse con programas o scripts externos para generar contenido dinámico

### 4. Implementar WAF

Desplegar un waf para bloquear cierto tipo de tráfico malicioso, como este, que pretende ejecutar código remoto no autorizado.


