#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-self-hosted-ai-starter-kit-normativa}"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$TARGET_DIR/.git" ]; then
  git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git "$TARGET_DIR"
fi

mkdir -p "$TARGET_DIR/n8n/demo-data/workflows" "$TARGET_DIR/shared"

cp "$SOURCE_DIR/docker-compose.yml" "$TARGET_DIR/docker-compose.yml"
cp "$SOURCE_DIR/Dockerfile.n8n" "$TARGET_DIR/Dockerfile.n8n"
cp "$SOURCE_DIR/.env.example" "$TARGET_DIR/.env.example"
cp "$SOURCE_DIR"/workflow_*.json "$TARGET_DIR/"
cp "$SOURCE_DIR"/workflow_*.json "$TARGET_DIR/n8n/demo-data/workflows/"

cd "$TARGET_DIR"

if [ ! -f .env ]; then
  cp .env.example .env
  if command -v openssl >/dev/null 2>&1; then
    POSTGRES_PASSWORD_VALUE="$(openssl rand -base64 24 | tr -d '\n')"
    N8N_ENCRYPTION_KEY_VALUE="$(openssl rand -hex 32 | tr -d '\n')"
    N8N_JWT_SECRET_VALUE="$(openssl rand -hex 32 | tr -d '\n')"
    sed -i.bak "s|POSTGRES_PASSWORD=.*|POSTGRES_PASSWORD=${POSTGRES_PASSWORD_VALUE}|" .env
    sed -i.bak "s|N8N_ENCRYPTION_KEY=.*|N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY_VALUE}|" .env
    sed -i.bak "s|N8N_USER_MANAGEMENT_JWT_SECRET=.*|N8N_USER_MANAGEMENT_JWT_SECRET=${N8N_JWT_SECRET_VALUE}|" .env
    rm -f .env.bak
  fi
fi

docker compose --profile gpu-nvidia up -d --build

echo "n8n: http://localhost:5678"
echo "Qdrant: http://localhost:6333/dashboard"
echo "Ollama: http://localhost:11434"
