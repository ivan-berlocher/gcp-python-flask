# FastAPI on Google App Engine

This sample project is a minimal FastAPI application that can be deployed with Uvicorn.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # Required for NER
   python -m spacy download en_core_web_sm
   ```

2. Run the app locally:
   ```bash
   uvicorn main:app --reload
   ```
   Then open <http://localhost:8080> in your browser.

## Deployment

The `Procfile` configures Uvicorn for production environments such as Google App Engine:

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Deploy using your preferred method (e.g., `gcloud app deploy`).

## API Endpoints

- `GET /context` : récupère le contexte stocké en mémoire.
- `POST /context` : met à jour le contexte pour un `userId` donné.
- `POST /summary` : renvoie un résumé court du texte fourni (premières phrases).
- `POST /ner` : extrait les entités nommées du texte via spaCy.

Ces endpoints illustrent la mise en place d'un **MCP server** et de quelques
tools du module **F:Insight** (résumé et NER).

## F:Core Platform Documentation

Un aperçu de l'architecture et des objectifs du projet est disponible dans [docs/architecture.md](docs/architecture.md).
