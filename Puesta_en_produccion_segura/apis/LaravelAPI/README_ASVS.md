# ASVS V4.1 Controls - Laravel API

Implementación de los controles OWASP ASVS V4.1 (Access Control) en Laravel 12.

## 🔐 Controles Implementados

### V4.1.1 - Content-Type con charset UTF-8
**Middleware:** `SetContentTypeUtf8`
**Ubicación:** `app/Http/Middleware/SetContentTypeUtf8.php`
**Descripción:** Establece `Content-Type: application/json; charset=utf-8` en todas las respuestas.

### V4.1.2 - Redirección HTTP → HTTPS
**Middleware:** `ForceHttpsRedirect`
**Ubicación:** `app/Http/Middleware/ForceHttpsRedirect.php`
**Descripción:** Redirige automáticamente HTTP a HTTPS cuando `APP_ENV=production`.

### V4.1.3 - Cabeceras de Seguridad Inmutables
**Middleware:** `SecurityHeaders`
**Ubicación:** `app/Http/Middleware/SecurityHeaders.php`
**Cabeceras aplicadas:**
- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Strict-Transport-Security: max-age=31536000; includeSubDomains`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: geolocation=(), microphone=(), camera=()`

### V4.1.4 - Validación de Métodos HTTP
**Middleware:** `ValidateHttpMethods`
**Ubicación:** `app/Http/Middleware/ValidateHttpMethods.php`
**Métodos permitidos:** GET, POST, PUT, DELETE, PATCH, OPTIONS
**Métodos bloqueados:** TRACE, TRACK, CONNECT, etc.

### V4.1.5 - Firmas Digitales HMAC-SHA256
**Middleware:** `ValidateSignature`
**Ubicación:** `app/Http/Middleware/ValidateSignature.php`
**Descripción:** Las operaciones DELETE requieren firma HMAC-SHA256 válida.
**Expiración:** 5 minutos

## 🚀 Instalación

### 1. Copiar archivos
Copia todos los archivos middleware a sus ubicaciones correspondientes.

### 2. Configurar variables de entorno
```bash
cp .env.example .env
php artisan key:generate
