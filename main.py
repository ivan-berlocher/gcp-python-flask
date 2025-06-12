from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
import re

nlp = None
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # spaCy model is missing; inform user
    nlp = None

class TextPayload(BaseModel):
    text: str

class ContextPayload(BaseModel):
    userId: str
    data: dict

app = FastAPI()

_contexts = {}
@app.get("/")
async def index():
    return {"message": "hello, world"}


@app.get("/context")
async def get_context(userId: str):
    return _contexts.get(userId, {})


@app.post("/context")
async def set_context(payload: ContextPayload):
    _contexts[payload.userId] = payload.data
    return {"status": "ok"}


@app.post("/summary")
async def summarize(payload: TextPayload):
    sentences = re.split(r"(?<=[.!?]) +", payload.text.strip())
    summary = " ".join(sentences[:2])
    return {"summary": summary}


@app.post("/ner")
async def named_entities(payload: TextPayload):
    if nlp is None:
        raise HTTPException(status_code=500, detail="spaCy model 'en_core_web_sm' not installed")
    doc = nlp(payload.text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}

if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)

