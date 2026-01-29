require('dotenv').config();
const express = require('express');
const fs = require('fs');
const jwt = require('jsonwebtoken');
const OAuth2Server = require('@node-oauth/oauth2-server');
const { Request, Response } = OAuth2Server;
const crypto = require('crypto');


const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


const dataPath = './datos.json';
const oauthModel = require('./oauth-model');
const oauth = new OAuth2Server({
  model: oauthModel,
  accessTokenLifetime: 3600,
  allowBearerTokensInQueryString: true
});


const users = [
  { id: 1, username: 'user', password: 'password' },
  { id: 2, username: 'admin', password: 'admin123' }
];


// ========================================
// 🔥 OWASP ASVS V4.1 CONTROLES
// ========================================


// V4.1.1 - Content-Type JSON UTF-8
app.use((req, res, next) => {
  if (req.method !== 'OPTIONS') {
    res.set('Content-Type', 'application/json; charset=utf-8');
  }
  next();
});


// V4.1.2 - HTTPS Redirect (solo en producción)
app.use((req, res, next) => {
  if (process.env.NODE_ENV === 'production' && req.headers['x-forwarded-proto'] !== 'https') {
    return res.redirect(301, `https://${req.headers.host}${req.url}`);
  }
  next();
});


// V4.1.3 - Headers de seguridad no sobrescribibles
app.use((req, res, next) => {
  res.set({
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
    'X-XSS-Protection': '1; mode=block'
  });
  next();
});


// V4.1.4 - Solo métodos permitidos
app.use((req, res, next) => {
  const allowed = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'];
  
  if (req.method === 'OPTIONS') {
    res.set({
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': allowed.join(', '),
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Signature, X-Timestamp'
    });
    return res.status(204).end();
  }
  
  if (!allowed.includes(req.method)) {
    return res.status(405).json({ 
      error: 'V4.1.4 Method Not Allowed',
      allowed: allowed.join(', ')
    }).set('Allow', allowed.join(', '));
  }
  next();
});


// ========================================
// FUNCIONES
// ========================================
function readData() {
  if (!fs.existsSync(dataPath)) {
    fs.writeFileSync(dataPath, JSON.stringify([]));
  }
  const data = fs.readFileSync(dataPath, 'utf-8');
  return JSON.parse(data);
}


function writeData(data) {
  fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}


// JWT Auth
function authenticateJWT(req, res, next) {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: 'No se proporcionó token' });
  const token = authHeader.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Token inválido' });
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET || 'secret');
    next();
  } catch (err) {
    res.status(403).json({ error: 'Token expirado o inválido' });
  }
}


// OAuth Auth
async function authenticateOAuth(req, res, next) {
  const request = new Request(req);
  const response = new Response(res);
  try {
    await oauth.authenticate(request, response);
    next();
  } catch (err) {
    res.status(err.code || 500).json({ error: 'OAuth failed', message: err.message });
  }
}


// V4.1.5 - Verificación de firma digital
function verifySignature(req, res, next) {
  const signature = req.headers['x-signature'];
  const timestamp = req.headers['x-timestamp'];
  
  if (!signature) {
    return res.status(400).json({ error: 'V4.1.5 Falta firma digital (X-Signature)' });
  }
  
  if (!timestamp) {
    return res.status(400).json({ error: 'V4.1.5 Falta timestamp (X-Timestamp)' });
  }
  
  // Verificar que el timestamp no sea muy antiguo (5 minutos)
  const now = new Date();
  const reqTime = new Date(timestamp);
  const diffMinutes = (now - reqTime) / 1000 / 60;
  
  if (diffMinutes > 5 || diffMinutes < -1) {
    return res.status(401).json({ 
      error: 'V4.1.5 Firma expirada',
      detalle: `La firma tiene ${Math.round(diffMinutes)} minutos de antigüedad (máximo 5)` 
    });
  }
  
  // Construir mensaje para verificar
  const data = {
    id: parseInt(req.params.id) || null,
    method: req.method,
    path: req.path
  };
  
  const message = JSON.stringify(data, Object.keys(data).sort()) + timestamp;
  const secret = process.env.SIGNATURE_SECRET || 'clave_secreta_para_firmas_muy_larga_y_segura';
  
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(message)
    .digest('hex');
  
  // Comparación segura
  try {
    const sigBuf = Buffer.from(signature);
    const expectedBuf = Buffer.from(expectedSignature);
    
    if (sigBuf.length !== expectedBuf.length || !crypto.timingSafeEqual(sigBuf, expectedBuf)) {
      return res.status(401).json({ error: 'V4.1.5 Firma digital inválida' });
    }
  } catch (err) {
    return res.status(401).json({ error: 'V4.1.5 Firma digital inválida' });
  }
  
  console.log('✅ V4.1.5 Firma digital válida');
  next();
}


// ========================================
// RUTAS
// ========================================
app.get('/', (req, res) => {
  res.json({ mensaje: 'Node.js API - OWASP ASVS V4.1 Controles 4.1.1 - 4.1.5 ✅' });
});


app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ error: 'Username y password requeridos' });
  }
  const user = users.find(u => u.username === username && u.password === password);
  if (!user) return res.status(401).json({ error: 'Credenciales inválidas' });
  
  const payload = { id: user.id, username: user.username };
  const token = jwt.sign(payload, process.env.JWT_SECRET || 'secret', { expiresIn: '1h' });
  res.json({ 
    mensaje: 'Login exitoso', 
    token, 
    usuario: user.username 
  });
});


// Endpoint auxiliar para generar firmas (solo para testing)
app.post('/generar_firma', authenticateJWT, (req, res) => {
  const { id, method, path } = req.body;
  const timestamp = new Date().toISOString();
  
  const data = { id: id || null, method, path };
  const message = JSON.stringify(data, Object.keys(data).sort()) + timestamp;
  const secret = process.env.SIGNATURE_SECRET || 'clave_secreta_para_firmas_muy_larga_y_segura';
  
  const firma = crypto
    .createHmac('sha256', secret)
    .update(message)
    .digest('hex');
  
  res.json({ firma, timestamp });
});


// OAuth token endpoint
app.post('/oauth/token', async (req, res) => {
  const request = new Request(req);
  const response = new Response(res);
  try {
    const token = await oauth.token(request, response);
    res.json({
      access_token: token.accessToken,
      token_type: 'Bearer',
      expires_in: 3600,
      message: 'OAuth2 OK'
    });
  } catch (err) {
    res.status(err.code || 500).json({ error: err.message });
  }
});


// CRUD Endpoints
app.post('/nombres/:nombre', authenticateJWT, (req, res) => {
  const nombres = readData();
  const nuevo = { id: nombres.length + 1, nombre: req.params.nombre };
  nombres.push(nuevo);
  writeData(nombres);
  res.status(201).json({ mensaje: 'Creado', data: nuevo });
});


app.get('/nombres', authenticateJWT, (req, res) => {
  res.json(readData());
});


app.get('/nombres/:id', authenticateJWT, (req, res) => {
  const id = parseInt(req.params.id);
  const nombres = readData();
  const nombre = nombres.find(n => n.id === id);
  if (!nombre) {
    return res.status(404).json({ error: 'No encontrado' });
  }
  res.json(nombre);
});


// V4.1.5 - DELETE requiere firma digital
app.delete('/nombres/:id', authenticateJWT, verifySignature, (req, res) => {
  const id = parseInt(req.params.id);
  const nombres = readData();
  const index = nombres.findIndex(n => n.id === id);
  
  if (index === -1) {
    return res.status(404).json({ error: 'No encontrado' });
  }
  
  nombres.splice(index, 1);
  writeData(nombres);
  res.json({ mensaje: 'Eliminado correctamente', id });
});


// 404
app.use((req, res) => {
  res.status(404).json({ error: 'No encontrado' });
});


const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`🚀 Node.js API ASVS V4.1: http://localhost:${PORT}`);
  console.log('✅ Controles implementados: 4.1.1, 4.1.2, 4.1.3, 4.1.4, 4.1.5');
});
