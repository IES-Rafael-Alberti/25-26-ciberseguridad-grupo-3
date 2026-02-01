package com.example.demo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
class SecurityTests {

    @Autowired
    private MockMvc mockMvc;

    // V4.1 Security Headers
    @Test
    void securityHeadersIdentify() throws Exception {
        mockMvc.perform(get("/nombres"))
                .andExpect(header().string("X-Content-Type-Options", "nosniff"))
                .andExpect(header().string("X-Frame-Options", "DENY"))
                .andExpect(header().string("Strict-Transport-Security", "max-age=31536000; includeSubDomains"))
                .andExpect(header().string("Cache-Control", "no-store"));
    }

    // V4.2 Input Validation
    @Test
    void validationPreventsBadInput() throws Exception {
        // Authenticate first (mocking logic or just skipping auth for this specific endpoint if it was open, 
        // but 'actualizar' requires auth header check manually implemented in Main.
        // The Main.java 'actualizar' method manually checks 'Authorization' header.
        
        // Let's create a valid token first using valid credentials? 
        // No, the simplistic auth in Main.java just checks "Bearer " + validToken.
        // Main.java: validarToken checks signature.
        // We can just use a dummy token if we mock the key or just rely on 'authValida' logic?
        // Wait, 'authValida' verifies the signature against the key in .env. 
        // Since we are in @SpringBootTest, it loads .env if configured, or might fail if not present.
        // Ideally we should mock the behavior or set a test property.
        
        // However, for validation check, the @Valid kicks in BEFORE the manual auth check inside the method body?
        // No, Spring validation on @RequestBody happens before method entry usually?
        // Actually, 'authValida' is called manually inside the method:
        /*
          public Object actualizar(...) {
              if (!authValida(auth)) ...
              ...
          }
        */
        // So validation happens BEFORE existing manual auth check?
        // Yes, @Valid on @RequestBody is processed by ArgumentResolver before the method body is entered.
        // So we should see 400 Bad Request even without auth header if the body is invalid.
        // Let's test that.
        
        String invalidJson = "{\"nombre\": \"\"}"; // Empty name, violates @NotBlank
        
        mockMvc.perform(put("/nombres/1")
                .header("Authorization", "Bearer ignored") 
                .contentType("application/json")
                .content(invalidJson))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.nombre").value("El nombre no puede estar vacío"));
    }

    // V6.2 Password Security
    @Test
    void passwordPolicyEnforcement() throws Exception {
        // Weak password
        String weakBody = "{\"usuario\": \"test\", \"password\": \"123\"}";
        mockMvc.perform(post("/register")
                .contentType("application/json")
                .content(weakBody))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.error").exists());

        // Strong password
        String strongBody = "{\"usuario\": \"test\", \"password\": \"StronG$Pa55word\"}";
        mockMvc.perform(post("/register")
                .contentType("application/json")
                .content(strongBody))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.mensaje").value("Usuario registrado (simulado)"));
    }
}
