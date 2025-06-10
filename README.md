# FastAPI on Google App Engine

This sample project is a minimal FastAPI application that can be deployed with Uvicorn.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

3. Run the app locally:
   ```bash
   uvicorn main:app --reload
   ```
   Then open <http://localhost:8080> in your browser.

The `/agent` endpoint relies on [LangChain](https://python.langchain.com/) and
requires an OpenAI API key just like the other endpoints.

## Deployment

The `Procfile` configures Uvicorn for production environments such as Google App Engine:

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Deploy using your preferred method (e.g., `gcloud app deploy`).

## F:Core Platform Documentation

Un aperçu de l'architecture et des objectifs du projet est disponible dans [docs/architecture.md](docs/architecture.md).

## API Endpoints

- `POST /summarize` – envoie un texte et reçoit un résumé en deux phrases généré par GPT‑4o-mini.
- `POST /named-entities` – renvoie les entités nommées détectées sous forme de tableau JSON `{text, label}`.
- `POST /agent` – exécute un agent LangChain qui combine raisonnement pas à pas et réponse finale.
  Les deux premières opérations sont également référencées via la route
  `GET /tools`.

## Orchestration API

Ces routes permettent de gérer les workflows low-code :

- `GET /tools` – liste des tools disponibles. Les entrées
  `summarize` et `named-entities` renvoient respectivement vers les
  routes `POST /summarize` et `POST /named-entities`.
- `GET /tools/{id}/schema` – renvoie le JSON Schema associé à un tool.
- `GET /workflows/{id}` – récupère la configuration d'un workflow.
- `POST /workflows` – crée un nouveau workflow.
- `POST /workflows/{id}/run` – lance l'exécution.
- WebSocket `ws://host/ws/workflows/{runId}/events` – flux en temps réel des logs de la run.

Un client WebSocket peut recevoir les logs ainsi :

```python
import websockets
import asyncio

async def watch(run_id):
    uri = f"ws://localhost:8080/ws/workflows/{run_id}/events"
    async with websockets.connect(uri) as ws:
        async for line in ws:
            print(line)

asyncio.run(watch("run-wf1"))
```

## Developer Studio UI

The repository includes a small Next.js app under `devstudio-next` that offers
an interface to the API. Start it locally with:

```bash
cd devstudio-next
npm install  # first time only
npm run dev
```

The UI lists the available tools, allows you to submit text to them and shows
the API response in the logs panel.
