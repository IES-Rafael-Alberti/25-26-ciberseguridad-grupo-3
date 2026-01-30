<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class ValidateSignature
{
    public function handle(Request $request, Closure $next): Response
    {
        if ($request->method() !== 'DELETE') {
            return $next($request);
        }

        if (!$request->hasHeader('X-Signature') || !$request->hasHeader('X-Timestamp')) {
            return response()->json([
                'error' => 'Missing Signature',
                'message' => 'DELETE operations require X-Signature and X-Timestamp headers'
            ], 400);
        }

        $signature = $request->header('X-Signature');
        $timestamp = $request->header('X-Timestamp');

        $currentTime = time();
        $requestTime = intval($timestamp);

        if (abs($currentTime - $requestTime) > 300) {
            return response()->json([
                'error' => 'Signature Expired',
                'message' => 'The signature has expired. Maximum age is 5 minutes.'
            ], 401);
        }

        // IMPORTANTE: Los datos deben ser EXACTAMENTE iguales al controlador
        $dataToSign = [
            'id' => (string) $request->route('id'),
            'method' => 'DELETE',
            'path' => $request->path(),
            'timestamp' => (int) $timestamp  // ← CAMBIO: int en lugar de string
        ];

        $secret = env('SIGNATURE_SECRET', 'default-secret-key-change-this');

        // JSON sin escape de barras
        $dataString = json_encode($dataToSign, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
        $expectedSignature = hash_hmac('sha256', $dataString, $secret);

        if (!hash_equals($expectedSignature, $signature)) {
            // DEBUG temporal
            \Log::debug('Signature mismatch', [
                'expected_signature' => $expectedSignature,
                'received_signature' => $signature,
                'data_string' => $dataString,
                'data_to_sign' => $dataToSign,
                'request_path' => $request->path(),
            ]);

            return response()->json([
                'error' => 'Invalid Signature',
                'message' => 'The provided signature is invalid',
                'debug' => config('app.debug') ? [
                    'expected' => $expectedSignature,
                    'received' => $signature,
                    'data' => $dataToSign
                ] : null
            ], 401);
        }

        return $next($request);
    }
}
