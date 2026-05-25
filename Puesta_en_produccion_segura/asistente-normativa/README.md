Asistente local multi agente para normativa de ciberseguridad
=============================================================

Este proyecto despliega un asistente local para consultar normativas de ciberseguridad con n8n, Ollama, Qdrant y PostgreSQL.

El sistema responde preguntas sobre normas como ISO 27001, ENS, RGPD y NIS2. También permite añadir nuevas normas, por ejemplo ISO 27041, si ingestas su PDF y creas un agente especializado.

Todo corre en local. No usa APIs externas de pago.


1. Qué problema resuelve
========================

El proyecto permite hacer preguntas en lenguaje natural sobre documentos normativos. El asistente busca fragmentos relevantes en los PDFs indexados y usa un modelo local para redactar la respuesta.

El flujo básico es este:

1. Subes o envías un PDF de una normativa.
2. n8n extrae el texto del PDF.
3. El texto se divide en fragmentos pequeños.
4. Ollama crea embeddings para esos fragmentos.
5. Qdrant guarda los fragmentos y sus vectores.
6. El usuario pregunta desde el chat de n8n.
7. El orquestador clasifica la pregunta.
8. El orquestador llama al agente especializado.
9. El agente busca contexto en Qdrant y responde.

Este patrón se llama RAG. Significa que el modelo no responde solo con su memoria interna. Primero recupera información de documentos locales y luego redacta la respuesta con ese contexto.


2. Componentes del sistema
==========================

2.1. n8n

n8n coordina todo el sistema.

En este proyecto, n8n ejecuta tres tipos de workflows:

1. Un workflow de ingesta.
2. Un workflow orquestador.
3. Un workflow agente por cada normativa.

n8n también ofrece el chat integrado que usa el usuario final.

2.2. Ollama

Ollama sirve los modelos locales.

Este proyecto usa estos modelos:

```text
qwen3:8b
nomic-embed-text:latest
```

`qwen3:8b` genera respuestas y clasifica preguntas. `nomic-embed-text:latest` crea los embeddings que Qdrant usa para buscar fragmentos similares.

El sistema usa el mismo modelo de chat para todos los agentes. Esto reduce problemas de memoria de vídeo porque Ollama mantiene un solo modelo principal cargado.

2.3. Qdrant

Qdrant guarda los fragmentos vectorizados de los PDFs.

Cada fragmento incluye metadata. La metadata más importante es `normativa`.

Ejemplos:

```json
{
  "normativa": "ISO27001",
  "fuente": "ISO27001.pdf"
}
```

El agente usa esa metadata para buscar solo dentro de la normativa correcta.

2.4. PostgreSQL

PostgreSQL guarda datos internos de n8n y también puede guardar memoria conversacional.

El orquestador incluye memoria PostgreSQL en la rama general. Esto permite mantener contexto entre mensajes.

2.5. Docker Compose

Docker Compose levanta todos los servicios.

Servicios principales:

```text
postgres
qdrant
n8n-import
n8n
ollama-gpu
ollama-pull-models-gpu
```

El perfil principal es `gpu-nvidia`.


3. Archivos del proyecto
========================

```text
docker-compose.yml
.env.example
setup.sh
workflow_ingest.json
workflow_orquestador.json
workflow_agente_iso27001.json
README.md
shared/
```

`docker-compose.yml` define los contenedores.

`.env.example` contiene las variables necesarias.

`setup.sh` prepara una copia basada en el starter kit oficial de n8n. En Windows puedes usar Docker Compose directamente sin este script.

`workflow_ingest.json` importa el workflow de ingesta de PDFs.

`workflow_orquestador.json` importa el workflow principal de chat.

`workflow_agente_iso27001.json` importa el agente ISO 27001. También sirve como plantilla para otras normativas.

`shared/` queda disponible como carpeta compartida con el contenedor n8n.


4. Requisitos
=============

Necesitas:

1. Windows.
2. Docker Desktop instalado.
3. Docker Desktop arrancado.
4. Contenedores Linux activados.
5. GPU NVIDIA compatible.
6. Drivers NVIDIA instalados.
7. Soporte de GPU en Docker Desktop.
8. Al menos 8 GB de VRAM para `qwen3:8b` cuantizado.
9. Al menos 16 GB de RAM. El proyecto recomienda 32 GB.

Para comprobar que Docker responde:

```powershell
docker version
```

Para comprobar que Docker Compose lee la configuración:

```powershell
docker compose config
```


5. Configuración inicial
========================

5.1. Crear el archivo `.env`

Copia el ejemplo:

```powershell
Copy-Item .env.example .env
```

Abre `.env` y cambia estos valores:

```env
POSTGRES_PASSWORD=pon_una_clave_larga
N8N_ENCRYPTION_KEY=pon_una_clave_larga
N8N_USER_MANAGEMENT_JWT_SECRET=pon_otra_clave_larga
```

No cambies `N8N_ENCRYPTION_KEY` después de crear credenciales en n8n. n8n usa esa clave para cifrar y descifrar credenciales.

5.2. Generar secretos en PowerShell

Ejecuta este comando dos veces:

```powershell
[Convert]::ToHexString((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

Usa el primer valor en:

```env
N8N_ENCRYPTION_KEY=
```

Usa el segundo valor en:

```env
N8N_USER_MANAGEMENT_JWT_SECRET=
```

Para `POSTGRES_PASSWORD`, usa otra contraseña larga.


6. Arranque del sistema
======================

Arranca los servicios con GPU NVIDIA:

```powershell
docker compose --profile gpu-nvidia up -d --build
```

La primera ejecución tarda más. Docker descarga imágenes y Ollama descarga los modelos.

Comprueba el estado:

```powershell
docker compose ps
```

Abre las URLs:

```text
n8n: http://localhost:5678
Qdrant: http://localhost:6333/dashboard
Ollama: http://localhost:11434
```

Ollama responde con un mensaje simple en el navegador. Para ver modelos:

```powershell
curl.exe http://localhost:11434/api/tags
```

Para parar el sistema:

```powershell
docker compose down
```

Para pararlo y eliminar volúmenes de datos:

```powershell
docker compose down -v
```

Usa `down -v` solo si quieres borrar datos de n8n, PostgreSQL, Qdrant y Ollama.


7. Credenciales en n8n
======================

Entra en n8n:

```text
http://localhost:5678
```

Crea el usuario inicial.

Después crea o revisa estas credenciales.

7.1. Ollama

Tipo de credencial: Ollama.

Valores:

```text
Base URL: http://ollama:11434
API key: vacío
```

Si n8n no conecta, prueba:

```text
Base URL: http://ollama-gpu:11434
API key: vacío
```

Usa `localhost:11434` solo desde Windows o desde el navegador. Dentro de n8n, `localhost` apunta al contenedor de n8n, no a Ollama.

7.2. Qdrant

Tipo de credencial: Qdrant.

Valores:

```text
Base URL: http://qdrant:6333
API key: vacío
```

Si activas una API key en Qdrant, debes ponerla aquí. Este proyecto no la activa por defecto.

7.3. PostgreSQL

Tipo de credencial: Postgres.

Valores:

```text
Host: postgres
Port: 5432
Database: valor de POSTGRES_DB
User: valor de POSTGRES_USER
Password: valor de POSTGRES_PASSWORD
```


8. Workflows incluidos
======================

8.1. Ingest Normativa

Este workflow recibe un PDF y lo guarda en Qdrant.

Nodos principales:

```text
Webhook PDF
Preparar metadata
Qdrant upsert normativa
Embeddings Ollama
Document Loader PDF
Text Splitter 800 100
Respuesta ingesta
```

El webhook espera un archivo en el campo binario `data`.

También espera un campo `normativa`, por ejemplo:

```text
ISO27001
ENS
RGPD
NIS2
ISO27041
```

El nodo `Text Splitter 800 100` usa:

```text
chunk_size: 800
chunk_overlap: 100
```

8.2. Orquestador Normativa

Este workflow recibe preguntas desde el chat.

Nodos principales:

```text
On Chat Message
Text Classifier Normativa
Call Agente ISO27001
Call Agente ENS
Call Agente RGPD
Call Agente NIS2
GENERAL Agent
Postgres Chat Memory
```

El clasificador asigna una categoría:

```text
ISO27001
ENS
RGPD
NIS2
GENERAL
```

Después llama al sub workflow correspondiente.

8.3. Agente ISO27001

Este workflow responde preguntas sobre ISO 27001.

Nodos principales:

```text
When Executed by Another Workflow
AI Agent ISO27001
Ollama qwen3
Qdrant ISO27001 Retriever
Embeddings Ollama
ejecutar_codigo
Devolver respuesta
```

El agente busca en Qdrant con este filtro:

```json
{
  "must": [
    {
      "key": "metadata.normativa",
      "match": {
        "value": "ISO27001"
      }
    }
  ]
}
```

La herramienta `ejecutar_codigo` ejecuta JavaScript pequeño con Node. Sirve para cálculos o transformaciones simples.


9. Importar workflows
=====================

El contenedor `n8n-import` intenta importar los workflows al arrancar si no existen workflows en la base de datos.

Si no aparecen en n8n, impórtalos manualmente:

1. Entra en n8n.
2. Ve a Workflows.
3. Importa desde archivo.
4. Importa estos archivos:

```text
workflow_ingest.json
workflow_orquestador.json
workflow_agente_iso27001.json
```

Después abre cada workflow y revisa credenciales. n8n no siempre asigna credenciales importadas de forma automática.


10. Ingestar un PDF
===================

10.1. Usar la URL de test

Este método sirve mientras editas el workflow.

1. Abre el workflow `Ingest Normativa`.
2. Abre el nodo `Webhook PDF`.
3. Pulsa `Listen for test event`.
4. Ejecuta el comando con `/webhook-test/`.

Ejemplo:

```powershell
curl.exe -X POST http://localhost:5678/webhook-test/ingest-normativa `
  -F "data=@C:\Users\jefft\Desktop\BS_ISO_IEC_27041.pdf" `
  -F "normativa=ISO27041"
```

10.2. Usar la URL de producción

Este método sirve cuando el workflow ya está activo.

1. Abre `Ingest Normativa`.
2. Guarda el workflow.
3. Activa el workflow con el interruptor superior.
4. Ejecuta el comando con `/webhook/`.

Ejemplo:

```powershell
curl.exe -X POST http://localhost:5678/webhook/ingest-normativa `
  -F "data=@C:\Users\jefft\Desktop\BS_ISO_IEC_27041.pdf" `
  -F "normativa=ISO27041"
```

10.3. Comprobar que el PDF llegó

Abre la ejecución en n8n.

El nodo `Webhook PDF` debe mostrar un campo binario llamado:

```text
data
```

El nodo `Preparar metadata` también debe conservar ese binario. Si no lo conserva, Qdrant mostrará este error:

```text
This operation expects the node's input data to contain a binary file 'data', but none was found
```

Solución:

1. Abre `Preparar metadata`.
2. En `Include in Output`, selecciona `All Input Fields`.
3. Activa `Include Binary Data`, si tu versión de n8n muestra esa opción.
4. Si aparece `Strip Binary Data`, déjalo desactivado.


11. Usar el chat
================

Abre el workflow `Orquestador Normativa`.

Usa el chat integrado de n8n.

Ejemplos de preguntas:

```text
Qué controles de ISO 27001 tratan la gestión de accesos
```

```text
Qué exige NIS2 sobre notificación de incidentes
```

```text
Compara ENS e ISO 27001 en gestión de riesgos
```

El orquestador clasifica la pregunta. Si detecta una normativa concreta, llama al agente especializado. Si la pregunta es general o comparativa, responde desde la rama general.


12. Añadir una normativa nueva
==============================

Supongamos que quieres añadir ISO 27041.

12.1. Ingesta el PDF

Ejecuta:

```powershell
curl.exe -X POST http://localhost:5678/webhook/ingest-normativa `
  -F "data=@C:\Users\jefft\Desktop\BS_ISO_IEC_27041.pdf" `
  -F "normativa=ISO27041"
```

Ese valor `ISO27041` queda guardado en Qdrant como metadata.

12.2. Duplica el agente

Duplica `workflow_agente_iso27001.json` o duplica el workflow desde n8n.

Cambia:

```text
id
name
system prompt
toolName
toolDescription
filtro metadata.normativa
```

El filtro debe usar el mismo valor que usaste en la ingesta:

```json
{
  "must": [
    {
      "key": "metadata.normativa",
      "match": {
        "value": "ISO27041"
      }
    }
  ]
}
```

12.3. Conecta el agente al orquestador

Tienes dos opciones.

Opción 1. Añadir una nueva categoría al clasificador.

Añade `ISO27041` al nodo `Text Classifier Normativa`. Después añade una rama que llame al nuevo workflow.

Opción 2. Reusar una categoría existente.

Esto sirve para pruebas rápidas, pero no es limpio. Por ejemplo, puedes cambiar temporalmente el agente ISO27001 para que filtre `ISO27041`.

La opción 1 es la correcta si quieres mantener el sistema extensible.


13. Gestión de modelos y VRAM
=============================

El proyecto usa un único modelo de chat:

```text
qwen3:8b
```

Todos los agentes usan ese modelo. Solo cambia el prompt de sistema.

Ollama mantiene el modelo cargado durante:

```text
OLLAMA_KEEP_ALIVE=5m
```

Esto evita recargas constantes. También reduce conflictos de VRAM porque el sistema no intenta cargar varios modelos de chat a la vez.

El modelo de embeddings es distinto:

```text
nomic-embed-text:latest
```

Este modelo se usa durante ingesta y recuperación vectorial.


14. Resolución de problemas
===========================

14.1. Docker no conecta

Error típico:

```text
open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified
```

Causa:

Docker Desktop no está arrancado o no está usando contenedores Linux.

Solución:

1. Abre Docker Desktop.
2. Espera a que termine de arrancar.
3. Verifica que usa Linux containers.
4. Ejecuta:

```powershell
docker version
```

14.2. Conflicto con PostgreSQL

Error típico:

```text
The container name "/postgres" is already in use
```

Causa:

Otro contenedor ya usa ese nombre.

Estado actual:

El `docker-compose.yml` ya no define nombres fijos de contenedor. Si ves este error, estás usando una versión antigua del archivo o tienes un contenedor huérfano.

Solución:

```powershell
docker compose down --remove-orphans
docker compose --profile gpu-nvidia up -d
```

14.3. n8n no conecta con Ollama

Causa habitual:

La credencial usa `localhost:11434`.

Dentro de n8n, `localhost` apunta al propio contenedor de n8n.

Solución:

```text
Base URL: http://ollama:11434
```

Alternativa:

```text
Base URL: http://ollama-gpu:11434
```

14.4. El webhook devuelve 404

Error típico:

```json
{
  "code": 404,
  "message": "The requested webhook is not registered"
}
```

Causa:

Usas la URL de producción con un workflow inactivo, o usas la URL de test sin poner el nodo en escucha.

Solución para test:

```text
Usa /webhook-test/ingest-normativa y pulsa Listen for test event.
```

Solución para producción:

```text
Activa el workflow y usa /webhook/ingest-normativa.
```

14.5. Qdrant dice que no hay archivo binario

Error típico:

```text
This operation expects the node's input data to contain a binary file 'data', but none was found
```

Causa:

El nodo anterior eliminó el binario.

Solución:

1. Revisa que el `curl` usa `-F "data=@ruta.pdf"`.
2. Revisa que `Webhook PDF` muestra `binary.data`.
3. Revisa que `Preparar metadata` conserva campos de entrada y datos binarios.

14.6. Qdrant no devuelve resultados

Causas comunes:

1. El PDF no se ingestó bien.
2. La metadata `normativa` no coincide.
3. El agente filtra por otro valor.
4. La colección de Qdrant no es la misma.

Comprueba que estos valores coinciden:

```text
QDRANT_COLLECTION
metadata.normativa en la ingesta
metadata.normativa en el filtro del agente
```

14.7. El agente ISO no responde sobre ISO 27041

Causa:

ISO 27041 no forma parte de las categorías del orquestador original.

Solución:

Añade una categoría `ISO27041`, crea un agente `Agente ISO27041` y filtra Qdrant con `metadata.normativa = ISO27041`.


15. Seguridad
=============

Este proyecto está pensado para uso local.

No expongas n8n directamente a Internet sin autenticación fuerte, HTTPS y controles adicionales.

La herramienta `ejecutar_codigo` ejecuta JavaScript dentro del contenedor n8n. Esto resulta útil para cálculos pequeños, pero aumenta el riesgo si usuarios no confiables pueden hablar con el agente.

Recomendaciones:

1. Usa el sistema en una red local controlada.
2. No compartas el puerto de n8n públicamente.
3. No subas documentos sensibles si otras personas tienen acceso a la instancia.
4. Mantén copias de seguridad del volumen de PostgreSQL.
5. Mantén estable `N8N_ENCRYPTION_KEY`.


16. Mantenimiento
=================

16.1. Ver logs

```powershell
docker compose logs --tail 200 n8n
```

```powershell
docker compose logs --tail 200 ollama-gpu
```

```powershell
docker compose logs --tail 200 qdrant
```

16.2. Reiniciar servicios

```powershell
docker compose restart n8n
```

```powershell
docker compose restart ollama-gpu
```

16.3. Actualizar imágenes

```powershell
docker compose pull
docker compose --profile gpu-nvidia up -d
```

Haz una copia de seguridad antes de actualizar si ya tienes datos importantes.


17. Decisiones de diseño
========================

17.1. Un modelo de chat

El sistema usa `qwen3:8b` para todos los agentes.

Motivo:

La RTX 3070 tiene 8 GB de VRAM. Cargar varios modelos a la vez aumenta el riesgo de falta de memoria. Un solo modelo con prompts distintos resulta más estable.

17.2. Un agente por normativa

Cada agente tiene un prompt propio y un filtro propio en Qdrant.

Motivo:

La separación reduce respuestas mezcladas. También facilita añadir nuevas normas sin rehacer todo el sistema.

17.3. Qdrant con metadata

Los fragmentos guardan `normativa` y `fuente`.

Motivo:

El agente puede buscar solo en la norma correcta y puede citar el documento de origen.

17.4. n8n como orquestador

n8n permite ver y modificar el sistema de forma visual.

Motivo:

Esto facilita depurar nodos, revisar entradas y salidas, y extender el sistema sin escribir una aplicación completa desde cero.


18. Estado actual del proyecto
==============================

El proyecto incluye:

1. Infraestructura local con Docker Compose.
2. Perfil NVIDIA para Ollama.
3. Qdrant local.
4. PostgreSQL local.
5. n8n local.
6. Workflow de ingesta.
7. Workflow orquestador.
8. Agente ISO27001 como plantilla funcional.

Falta crear agentes específicos para ENS, RGPD, NIS2 y cualquier otra normativa nueva que quieras consultar de forma separada.

El flujo ya permite ingestar PDFs con cualquier valor de `normativa`. Para preguntar sobre esa normativa, el orquestador debe conocer esa categoría y debe existir un agente con el filtro correcto.
