<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\NameController;


Route::middleware(['oauth.validate'])->group(function () {
    Route::get('names', [NameController::class, 'index']);
    Route::get('names/{id}', [NameController::class, 'show']);
    Route::post('names', [NameController::class, 'store']);
    Route::put('names/{id}', [NameController::class, 'update']);
    Route::delete('names/{id}', [NameController::class, 'destroy']);
});

