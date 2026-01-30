const crypto = require('crypto');


const clients = [
  {
    clientId: 'test-client',
    clientSecret: process.env.OAUTH_SECRET || 'change-this-secret',
    grants: ['client_credentials']
  }
];


const tokens = [];


function getClient(clientId, clientSecret) {
  const client = clients.find(c => c.clientId === clientId);
  if (!client) return false;
  if (clientSecret) {
    const a = Buffer.from(client.clientSecret);
    const b = Buffer.from(clientSecret);
    if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) {
      return false;
    }
  }
  return {
    id: client.clientId,
    clientId: client.clientId,
    clientSecret: client.clientSecret,
    grants: client.grants
  };
}


function saveToken(token, client, user) {
  const savedToken = {
    accessToken: token.accessToken,
    accessTokenExpiresAt: token.accessTokenExpiresAt,
    client: { id: client.id || client.clientId },
    user: user
  };
  tokens.push(savedToken);
  return savedToken;
}


function getAccessToken(accessToken) {
  const token = tokens.find(t => t.accessToken === accessToken);
  
  if (!token) return false;
  
  return {
    accessToken: token.accessToken,
    accessTokenExpiresAt: token.accessTokenExpiresAt,
    client: token.client,
    user: token.user
  };
}


function getUserFromClient(client) {
  return { id: 'system' };
}


module.exports = {
  getClient,
  saveToken,
  getAccessToken,
  getUserFromClient
};
