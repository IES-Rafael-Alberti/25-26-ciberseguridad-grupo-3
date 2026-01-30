<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class ValidateHttpMethods
{
    /**
     * Handle an incoming request.
     *
     * ASVS V4.1.4: Verify that the application restricts HTTP methods
     * to only those that are necessary and blocks dangerous methods
     * like TRACE and TRACK.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        // Lista blanca de métodos HTTP permitidos
        $allowedMethods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'];

        $method = strtoupper($request->method());

        // Bloquear métodos peligrosos (TRACE, TRACK, CONNECT, etc.)
        if (!in_array($method, $allowedMethods)) {
            return response()->json([
                'error' => 'Method Not Allowed',
                'message' => "The {$method} method is not allowed for this resource.",
                'allowed_methods' => $allowedMethods
            ], 405)
            ->header('Allow', implode(', ', $allowedMethods));
        }

        return $next($request);
    }
}
