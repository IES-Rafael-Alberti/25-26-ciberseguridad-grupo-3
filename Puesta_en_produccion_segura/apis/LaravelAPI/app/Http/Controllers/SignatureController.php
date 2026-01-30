<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;

class SignatureController extends Controller
{
    public function generate(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'id' => 'required|string',
            'method' => 'required|string|in:DELETE',
            'path' => 'required|string',
        ]);

        $timestamp = time(); // Ya es int

        // IMPORTANTE: timestamp debe ser int, no string
        $dataToSign = [
            'id' => $validated['id'],
            'method' => $validated['method'],
            'path' => $validated['path'],
            'timestamp' => $timestamp  // int, no string
        ];

        $secret = env('SIGNATURE_SECRET', 'default-secret-key-change-this');

        // JSON sin escape de barras
        $dataString = json_encode($dataToSign, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
        $signature = hash_hmac('sha256', $dataString, $secret);

        return response()->json([
            'success' => true,
            'signature' => $signature,
            'timestamp' => $timestamp,
            'data_signed' => $dataToSign,
            'data_string' => $dataString,  // Para debug
            'instructions' => [
                'Add these headers to your DELETE request:',
                'X-Signature: ' . $signature,
                'X-Timestamp: ' . $timestamp,
                'Note: Signature expires in 5 minutes'
            ]
        ], 200);
    }
}
