# OAuth2 Implementation Guide (client_credentials)

Follow these steps to configure and test OAuth2 client credentials flow in this project.

## 1) Install dependencies

- Run:

  npm install

## 2) Configure environment

- Copy `.env.example` to `.env` and set secure random secrets:

  OAUTH_SECRET, JWT_SECRET, API_HMAC_SECRET

- Example values (use a random generator in production):

  OAUTH_SECRET=super-secret-client-secret
  JWT_SECRET=super-secret-jwt-key
  API_HMAC_SECRET=super-secret-hmac-key

## 3) Start the server

- Run:

  npm start

- Server will listen on `http://localhost:3000` by default

## 4) Obtain an access token (client_credentials)

- Use HTTP Basic auth with client id `test-client` and secret from `OAUTH_SECRET`.

- Example cURL:

  curl -u test-client:${OAUTH_SECRET} -d "grant_type=client_credentials" \
    http://localhost:3000/oauth/token

- Successful response example:

  {
    "access_token": "<token>",
    "token_type": "Bearer",
    "expires_in": 3600,
    "message": "OAuth2 OK [V4.1]"
  }

## 5) Call protected resource

- Use the `Authorization: Bearer <token>` header:

  curl -H "Authorization: Bearer <token>" http://localhost:3000/nombres

## 6) POST/PUT require HMAC header

- For `POST /nombres` and `PUT /nombres/:id` you must include a header `X-Message-Signature: sha256=<hex>` where `<hex>` is the HMAC-SHA256 of the JSON body using `API_HMAC_SECRET`.

- Example with `openssl`:

  body='{"nombre":"Nuevo"}'
  sig=$(printf "%s" "$body" | openssl dgst -sha256 -hmac "$API_HMAC_SECRET" -binary | xxd -p -c 256)
  curl -H "Authorization: Bearer <token>" -H "X-Message-Signature: sha256=$sig" -H "Content-Type: application/json" -d "$body" http://localhost:3000/nombres

## Notes and security tips

- The current model stores tokens and clients in memory (for demo only). Use a persistent DB in production.
- Store secrets in a secure store and rotate regularly.
- Use TLS in production.
- Consider support for additional grants (password, refresh_token, auth_code) if needed.
