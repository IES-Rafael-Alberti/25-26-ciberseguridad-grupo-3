<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class SetContentTypeUtf8
{
    /**
     * Handle an incoming request.
     *
     * ASVS V4.1.1: Verify that the application uses a single, pre-defined
     * character encoding such as UTF-8, and the Content-Type header is
     * correctly set in all responses.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        $response = $next($request);

        // Solo aplica a respuestas JSON (API)
        if ($response instanceof Response) {
            $response->headers->set('Content-Type', 'application/json; charset=utf-8');
        }

        return $response;
    }
}
