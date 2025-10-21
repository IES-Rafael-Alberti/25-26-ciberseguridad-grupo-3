**Test de Jose María Escalón Prada \- Bastionado de redes y sistemas**  
**Documentado por: Abel García Domínguez**

—-----------------------------------------------------------------------------------------------------------------------------

**Encabezado**:  
title “nginx test tests”

- **title**: define el nombre general del perfil. Indica que estos tests están orientados a verificar el estado y configuración de NGINX.  
- **uso:** simplemente da contexto,  no influye en la ejecución de los controles

**Control 1: nginx-01**  
control ‘nginx-01’ do  
    impact 1.0  
    title ‘NGINX debe estar instalado’  
    desc ‘Verificar que el paquete nginx este instalado’  
    describe package(‘nginx’) do  
        it { should be\_installed }  
    end  
end

- **¿Qué hace este control?** Comprueba que el paquete NGINX esté instalado en el sistema  
- **¿Cómo lo hace?** Usa el recurso *package(‘nginx’)* y verifica que *should be\_installed*  
- **Nivel de impacto *1.0* (crítico).** Si NGINX no está instalado, todo el servicio fallará

—-----------------------------------------------------------------------------------------------------------------------------

**Control 2: nginx-02**  
control ‘nginx-02’ do  
    impact 1.0  
    title ‘servicio nginx instalado, activo y habilitado’  
    desc ‘El servicio nginx debe estar corriendo y habilitado’  
    describe service(‘nginx’) do  
        it { should be\_installed }  
        it { should be\_enabled }  
        it { should be\_running }  
    end  
end

- **¿Qué hace?** Verifica tres cosas sobre el servicio NGINX:  
1. Que esté **instalado**  
2. Que esté **habilitado** para iniciarse automáticamente (enabled)  
3. Que esté actualmente **ejecutándose** (running)  
- **¿Por qué es importante?** Garantiza que el servicio esté operativo y disponible tras un reinicio.  
- **Nivel de impacto *1.0* (crítico).** Un servicio instalado pero parado no serviría a los usuarios

—-----------------------------------------------------------------------------------------------------------------------------

**Control 3: nginx-03**  
control ‘nginx-03’ do  
    impact 0.9  
    title ‘Puerto 80 escuchando’  
    describe port(80) do  
        it { should be\_listening }  
        its(‘protocols’) { should include ‘tcp’ }  
    end  
end

- **¿Qué hace?** Comprueba que el puerto 80 (HTTP) está abierto y escuchando conexiones  
- **¿Cómo lo hace?** Con el recurso port(80), verifica que el puerto escuche con protocolo TCP  
- **Importancia**: Asegura que el servidor web esté accesible para usuarios y clientes  
- **Nivel de impacto 0.9**. Es muy importante para el funcionamiento del servidor web

—-----------------------------------------------------------------------------------------------------------------------------

**Control 4: nginx-04**  
control ‘nginx-04’ do  
    impact 0.7  
    title ‘nginx.conf debe tener server\_tokens off’  
    desc ‘Para ocultar la version del servidor’  
    describe nginx\_conf do   
        its(‘server\_tokens’) { should cmp ‘off’ }  
    end  
end 

- **¿Qué hace?** Revisa el archivo de configuración principal (nginx.conf) para asegurarse de que *server\_tokens* está en *off*  
- **Motivo**. Aumenta la seguridad al evitar que los atacantes conozcan la versión exacta (podría facilitar exploits)  
- **Nivel de impacto *0.7***. Es una recomendación de seguridad media-alta porque afecta a la exposición de información sensible

—-----------------------------------------------------------------------------------------------------------------------------

**Control 5: nginx-05**  
control ‘nginx-05’ do  
    impact 0.8  
    title ‘Archivo index.html contiene texto esperado’  
    desc ‘Comprobar que la pagina de prueba contiene “Welcome” ‘  
    describe file(‘/usr/share/nginx/html/index.html’) do  
        it { should exist }  
        its(‘content’) { should match /Welcome/i }  
    end  
end 

- **¿Qué hace?** Comprueba que el archivo index.html existe y contiene la palabra “Welcome”  
- **Asegura** que la página principal está presente y muestra el contenido esperado.  
- **Nivel de impacto *0.8.*** Importante para validar el despliegue, aunque no tan crítico como la disponibilidad del servicio.  
  


—-----------------------------------------------------------------------------------------------------------------------------

**Este perfil de InSpec sirve para auditar la instalación y configuración básica de NGINX en un sistema.**

