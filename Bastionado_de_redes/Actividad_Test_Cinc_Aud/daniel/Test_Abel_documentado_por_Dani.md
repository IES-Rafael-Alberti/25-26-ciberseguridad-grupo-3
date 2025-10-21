# Test InSpec para Nginx de Abel documentado por Dani

## ¿Qué hace este test?

Este test verifica que el servidor web nginx esté correctamente instalado, funcionando y configurado en el sistema.

---

## Verificaciones que Realiza el test

### Verificación 1: Servicio Nginx
```ruby
describe service('nginx') do
  it { should be_installed }
  it { should be_running }
end
```

**Comprueba:**
- Que nginx está instalado
- Que nginx está ejecutándose

---

### Verificación 2: Versión de Nginx
```ruby
describe command('nginx -v') do
  its('stderr') { should match /nginx\/\d+\.\d+\.\d+/ }
end
```

**Comprueba:**
- Ejecuta el comando `nginx -v`
- Verifica que la salida tenga un formato de versión válido
- Ejemplo: `nginx/1.18.0`

---

### ✅ Verificación 3: Puerto de Escucha
```ruby
describe port(8081) do
  it { should be_listening }
end
```

**Comprueba:**
- Que nginx está escuchando en el puerto 8081
- **Nota**: El puerto 8081 es personalizado (el estándar es 80)

---

## Resumen

Este test verifica **4 cosas**:

1. ✅ Nginx instalado
2. ✅ Nginx corriendo
3. ✅ Versión válida de nginx
4. ✅ Escuchando en puerto 8081

---

## Resultados Posibles

- **✅ PASA**: Todo funciona correctamente
- **❌ FRACASA**: Algo no funciona (nginx no está instalado, no corre, o no escucha en el puerto)