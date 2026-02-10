package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.type.TypeReference;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import io.github.cdimascio.dotenv.Dotenv;

import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicLong;
import jakarta.validation.Valid;
import jakarta.validation.constraints.*;
import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.stereotype.Component;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;

@SpringBootApplication
@RestController
@RequestMapping("/nombres")
public class Main {

    // V4.1 Security Headers
    @Component
    public static class SecurityHeadersFilter implements Filter {
        @Override
        public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
                throws IOException, ServletException {
            HttpServletResponse httpResponse = (HttpServletResponse) response;
            httpResponse.setHeader("X-Content-Type-Options", "nosniff");
            httpResponse.setHeader("X-Frame-Options", "DENY");
            httpResponse.setHeader("Strict-Transport-Security", "max-age=31536000; includeSubDomains");
            httpResponse.setHeader("Cache-Control", "no-store");
            chain.doFilter(request, response);
        }
    }

	private final Map<Long, Persona> personas = new HashMap<>();
	private final AtomicLong contador = new AtomicLong();
	private final ObjectMapper objectMapper = new ObjectMapper();
	private final String ARCHIVO_JSON = "personas.json";

	// === CARGAR VARIABLES DESDE .env ===
	private final Dotenv dotenv = Dotenv.configure().ignoreIfMissing().load();

	// Ahora las claves vienen del archivo .env
	private final String SECRET_KEY = dotenv.get("JWT_SECRET") != null ? dotenv.get("JWT_SECRET") : "default_secret_key_for_dev_12345678901234567890";
	private final String GITHUB_CLIENT_ID = dotenv.get("GITHUB_CLIENT_ID");
	private final String GITHUB_CLIENT_SECRET = dotenv.get("GITHUB_CLIENT_SECRET");

	public static void main(String[] args) {
		SpringApplication.run(Main.class, args);
	}

	public Main() {
		cargarDesdeJSON();
	}

	// ===============================
	//      JWT: generar y validar
	// ===============================
	private String generarToken(String usuario) {
		return Jwts.builder()
				.setSubject(usuario)
				.signWith(Keys.hmacShaKeyFor(SECRET_KEY.getBytes()))
				.compact();
	}

	private boolean validarToken(String token) {
		try {
			Jwts.parserBuilder()
					.setSigningKey(SECRET_KEY.getBytes())
					.build()
					.parseClaimsJws(token);
			return true;
		} catch (Exception e) {
			return false;
		}
	}

	private boolean authValida(String header) {
		if (header == null || !header.startsWith("Bearer ")) return false;
		String token = header.substring(7);
		return validarToken(token);
	}

	// ===============================
	//            LOGIN
	// ===============================
	@PostMapping("/login")
	public Map<String, String> login(@RequestBody Map<String, String> credenciales) {

		if ("username".equals(credenciales.get("usuario")) &&
				"password".equals(credenciales.get("contrasena"))) {

			String token = generarToken(credenciales.get("usuario"));

			return Map.of(
					"mensaje", "Login correcto",
					"token", token
			);
		}

		return Map.of("error", "Credenciales incorrectas");
	}

	// ===============================
	//     LOGIN CON GITHUB OAuth
	// ===============================
	@PostMapping("/github_oauth")
	public Map<String, String> loginConGithub(@RequestBody Map<String, String> body) throws Exception {

		String code = body.get("code");

		if (code == null) {
			return Map.of("error", "Falta code");
		}

		// 1. Enviar code a GitHub para obtener access_token
		String url = "https://github.com/login/oauth/access_token";

		var params = new HashMap<String, String>();
		params.put("client_id", GITHUB_CLIENT_ID);
		params.put("client_secret", GITHUB_CLIENT_SECRET);
		params.put("code", code);

		String json = objectMapper.writeValueAsString(params);

		var client = org.apache.hc.client5.http.impl.classic.HttpClients.createDefault();
		var post = new org.apache.hc.client5.http.classic.methods.HttpPost(url);
		post.addHeader("Accept", "application/json");
		post.setEntity(new org.apache.hc.core5.http.io.entity.StringEntity(json));

		var response = client.execute(post);
		String respuesta = new String(response.getEntity().getContent().readAllBytes());

		Map<?, ?> tokenRespuesta = objectMapper.readValue(respuesta, Map.class);

		if (!tokenRespuesta.containsKey("access_token")) {
			return Map.of("error", "No se pudo obtener token de GitHub");
		}

		String githubToken = tokenRespuesta.get("access_token").toString();

		// 2. Pedir datos del usuario
		var get = new org.apache.hc.client5.http.classic.methods.HttpGet("https://api.github.com/user");
		get.addHeader("Authorization", "Bearer " + githubToken);

		var userResp = client.execute(get);
		String userJson = new String(userResp.getEntity().getContent().readAllBytes());

		Map<?, ?> userInfo = objectMapper.readValue(userJson, Map.class);

		String usuarioGitHub = userInfo.get("login").toString();

		// 3. Crear tu propio JWT para ese usuario
		String jwt = generarToken(usuarioGitHub);

		return Map.of(
				"jwt", jwt,
				"githubUser", usuarioGitHub
		);
	}

	// ===============================
	//      V6.2 PASSWORD SECURITY
	// ===============================
	public static class RegistroRequest {
		public String usuario;
		public String password;
	}

	@PostMapping("/register")
	public ResponseEntity<?> registrar(@RequestBody RegistroRequest request) {
		if (!validarPassword(request.password)) {
			return ResponseEntity.badRequest().body(Map.of(
					"error", "La contraseña no cumple los requisitos de seguridad (min 8 chars, mayus, minus, numero, especial)"
			));
		}
		// Simular registro
		return ResponseEntity.ok(Map.of("mensaje", "Usuario registrado (simulado)"));
	}

	private boolean validarPassword(String password) {
		if (password == null || password.length() < 8) return false;
		boolean hasUpper = !password.equals(password.toLowerCase());
		boolean hasLower = !password.equals(password.toUpperCase());
		boolean hasDigit = password.chars().anyMatch(Character::isDigit);
		boolean hasSpecial = password.matches(".*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>/?].*");
		return hasUpper && hasLower && hasDigit && hasSpecial;
	}

	// ===============================
	//            CRUD
	// ===============================
	@PostMapping("/{nombre}")
	public Object crear(@RequestHeader(value = "Authorization", required = false) String auth,
						@PathVariable String nombre) {

		if (!authValida(auth)) return Map.of("error", "Token inválido o faltante");

		long id = contador.incrementAndGet();
		Persona persona = new Persona(id, nombre);
		personas.put(id, persona);
		guardarEnJSON();
		return persona;
	}

	@GetMapping
	public Object obtenerTodos(@RequestHeader(value = "Authorization", required = false) String auth) {
		if (!authValida(auth)) return Map.of("error", "Token inválido o faltante");
		return new ArrayList<>(personas.values());
	}

	@GetMapping("/{id}")
	public Object obtenerPorId(@RequestHeader(value = "Authorization", required = false) String auth,
							   @PathVariable Long id) {

		if (!authValida(auth)) return Map.of("error", "Token inválido o faltante");

		Persona persona = personas.get(id);
		if (persona == null) return Map.of("error", "Persona no encontrada");
		return persona;
	}

	@PutMapping("/{id}")
	public Object actualizar(@RequestHeader(value = "Authorization", required = false) String auth,
							 @PathVariable Long id,
							 @Valid @RequestBody Persona personaActualizada) {

		if (!authValida(auth)) return Map.of("error", "Token inválido o faltante");

		if (!personas.containsKey(id)) return Map.of("error", "Persona no encontrada");

		personaActualizada.setId(id);
		personas.put(id, personaActualizada);
		guardarEnJSON();

		return personaActualizada;
	}

	@DeleteMapping("/{id}")
	public Object eliminar(@RequestHeader(value = "Authorization", required = false) String auth,
						   @PathVariable Long id) {

		if (!authValida(auth)) return Map.of("error", "Token inválido o faltante");

		if (!personas.containsKey(id)) return Map.of("error", "Persona no encontrada");

		personas.remove(id);
		guardarEnJSON();
		return Map.of("mensaje", "Persona eliminada con id: " + id);
	}

	// ===============================
	//       JSON (guardar/cargar)
	// ===============================
	private void guardarEnJSON() {
		try {
			objectMapper.writerWithDefaultPrettyPrinter()
					.writeValue(new File(ARCHIVO_JSON), personas);
		} catch (IOException e) {
			System.err.println("Error al guardar en JSON: " + e.getMessage());
		}
	}

	private void cargarDesdeJSON() {
		try {
			File archivo = new File(ARCHIVO_JSON);
			if (archivo.exists()) {
				Map<Long, Persona> datos = objectMapper.readValue(
						archivo,
						new TypeReference<Map<Long, Persona>>() {}
				);
				personas.putAll(datos);

				if (!personas.isEmpty()) {
					long maxId = personas.keySet().stream().max(Long::compare).orElse(0L);
					contador.set(maxId);
				}
			}
		} catch (IOException e) {
			System.out.println("No se encontró archivo JSON previo");
		}
	}

	@ExceptionHandler(MethodArgumentNotValidException.class)
	public ResponseEntity<Map<String, String>> handleValidationExceptions(MethodArgumentNotValidException ex) {
		Map<String, String> errors = new HashMap<>();
		ex.getBindingResult().getAllErrors().forEach((error) -> {
			String fieldName = ((FieldError) error).getField();
			String errorMessage = error.getDefaultMessage();
			errors.put(fieldName, errorMessage);
		});
		return ResponseEntity.badRequest().body(errors);
	}

	// ===============================
	//           CLASE PERSONA
	// ===============================
	public static class Persona {
		private Long id;
		
		@NotBlank(message = "El nombre no puede estar vacío")
		@Size(min = 2, max = 50, message = "El nombre debe tener entre 2 y 50 caracteres")
		private String nombre;

		public Persona() {}
		public Persona(Long id, String nombre) {
			this.id = id;
			this.nombre = nombre;
		}

		public Long getId() { return id; }
		public void setId(Long id) { this.id = id; }

		public String getNombre() { return nombre; }
		public void setNombre(String nombre) { this.nombre = nombre; }
	}
}
