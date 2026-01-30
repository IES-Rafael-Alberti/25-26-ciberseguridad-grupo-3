<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class ValidateOAuthToken
{
    public function handle(Request $request, Closure $next): Response
    {
        // Get the Authorization header
        $authHeader = $request->header('Authorization');
        
        if (!$authHeader || !str_starts_with($authHeader, 'Bearer ')) {
            return response()->json([
                'error' => 'Unauthorized - No token provided'
            ], 401);
        }
        
        // Extract the token (remove "Bearer " prefix)
        $token = substr($authHeader, 7);
        
        // Compare with the token from your teacher
        // Store your teacher's token in .env file
        $validToken = env('OAUTH_VALID_TOKEN');
        
        if ($token !== $validToken) {
            return response()->json([
                'error' => 'Unauthorized - Invalid token'
            ], 401);
        }
        
        // Token is valid, continue
        return $next($request);
    }
}
