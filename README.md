# FastAPI on Google App Engine

This sample project is a minimal FastAPI application that can be deployed with Uvicorn.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
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

## F:Core Platform Documentation

Un aperçu de l'architecture et des objectifs du projet est disponible dans [docs/architecture.md](docs/architecture.md).
