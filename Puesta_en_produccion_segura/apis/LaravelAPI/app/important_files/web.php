<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\NameController;

Route::middleware(['simple.auth'])->group(function () {
    Route::get('/', [NameController::class, 'saludo']);
    Route::get('names', [NameController::class, 'index']);       // List all names
    Route::get('names/{id}', [NameController::class, 'show']);   // Show specific Name by id
    Route::post('names', [NameController::class, 'store']);      // Create new Name
    Route::put('names/{id}', [NameController::class, 'update']); // Update Name by id
    Route::delete('names/{id}', [NameController::class, 'destroy']); // Delete Name by id
});
