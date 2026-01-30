<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class SimpleAuth
{
    public function handle(Request $request, Closure $next): Response
    {
        if (!$request->hasHeader('Authorization')) {
            return response()->json([
                'message' => 'Access denied'
            ], 401);
        }

        $authHeader = $request->header('Authorization');

        $credentials = base64_decode(substr($authHeader, 6));
        list($username, $password) = explode(':', $credentials);

        if ($username !== 'user' || $password !== 'password') {
            return response()->json([
                'message' => 'Access denied'
            ], 401);
        }

        return $next($request);
    }
}
