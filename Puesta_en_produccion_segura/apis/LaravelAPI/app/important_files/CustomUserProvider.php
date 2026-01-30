<?php

namespace App\Auth;

use Illuminate\Contracts\Auth\UserProvider;
use Illuminate\Contracts\Auth\Authenticatable;
use App\Models\CustomUser;

class CustomUserProvider implements UserProvider
{
    public function retrieveById($identifier)
    {
        // Return user if ID matches
        if ($identifier === 1) {
            return new CustomUser(['id' => 1, 'email' => 'user@example.com', 'name' => 'Test User']);
        }
        return null;
    }

    public function retrieveByToken($identifier, $token)
    {
        return null;
    }

    public function updateRememberToken(Authenticatable $user, $token)
    {
        // Not needed for JWT
    }

    public function retrieveByCredentials(array $credentials)
    {
        // Check if email matches
        if (isset($credentials['email']) && $credentials['email'] === 'user@example.com') {
            return new CustomUser(['id' => 1, 'email' => 'user@example.com', 'name' => 'Test User']);
        }
        return null;
    }

    public function validateCredentials(Authenticatable $user, array $credentials)
    {
        // Validate hardcoded credentials
        return $credentials['email'] === 'user@example.com' && 
               $credentials['password'] === 'password';
    }

    public function rehashPasswordIfRequired(Authenticatable $user, array $credentials, bool $force = false)
    {
        // Not needed
    }
}
