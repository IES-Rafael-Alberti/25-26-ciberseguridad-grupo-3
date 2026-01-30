<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\NameController;
use App\Http\Controllers\SignatureController;

// Endpoint para generar firmas (sin autenticación)
Route::post('generate-signature', [SignatureController::class, 'generate']);

// Rutas CRUD con OAuth
Route::middleware('oauth.validate')->group(function () {
    Route::get('names', [NameController::class, 'index']);
    Route::get('names/{id}', [NameController::class, 'show']);
    Route::post('names', [NameController::class, 'store']);
    Route::put('names/{id}', [NameController::class, 'update']);

    // DELETE con firma (dentro del grupo OAuth)
    Route::delete('names/{id}', [NameController::class, 'destroy'])
        ->middleware('signature');
});

// ============================================================
// RUTA DE TESTING - Solo para verificar control V4.1.5
// Esta ruta SOLO valida la firma, sin OAuth ni base de datos
// Si llegas aquí, significa que la firma fue validada correctamente
// ============================================================
Route::delete('test-signature/{id}', function($id) {
    return response()->json([
        'success' => true,
        'message' => 'Signature validation passed successfully',
        'id' => $id,
        'note' => 'This is a test endpoint to verify V4.1.5 signature validation'
    ], 200);
})->middleware('signature');
