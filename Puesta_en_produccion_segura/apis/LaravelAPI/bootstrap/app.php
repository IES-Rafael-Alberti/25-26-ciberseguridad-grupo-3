<?php

use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        api: __DIR__.'/../routes/api.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware) {
        // ============================================================
        // ASVS V4.1 - Middleware GLOBALES (se aplican a TODAS las peticiones)
        // ============================================================
        $middleware->append([
            \App\Http\Middleware\SetContentTypeUtf8::class,       // V4.1.1 - Content-Type UTF-8
            \App\Http\Middleware\ForceHttpsRedirect::class,       // V4.1.2 - HTTPS Redirect
            \App\Http\Middleware\SecurityHeaders::class,          // V4.1.3 - Security Headers
            \App\Http\Middleware\ValidateHttpMethods::class,      // V4.1.4 - HTTP Method Validation
        ]);

        // ============================================================
        // MIDDLEWARE CON ALIAS (para aplicar selectivamente en rutas)
        // ============================================================
        $middleware->alias([
            // Middleware existentes de tu aplicación
            'simple.auth' => \App\Http\Middleware\SimpleAuth::class,
            'oauth.validate' => \App\Http\Middleware\ValidateOAuthToken::class,

            // ASVS V4.1.5 - Validación de firmas digitales para operaciones sensibles
            'signature' => \App\Http\Middleware\ValidateSignature::class,
        ]);
    })
    ->withExceptions(function (Exceptions $exceptions): void {
        //
    })
    ->create();
