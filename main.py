from fastapi import FastAPI
from pydantic import BaseModel
import json

from gpt_utils import chat
from agents.langchain_agent import run_agent

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "hello, world"}


class TextRequest(BaseModel):
    text: str


@app.post("/agent")
async def agent(req: TextRequest):
    """Invoke the LangChain sequential agent."""
    result = run_agent(req.text)
    return result


@app.post("/summarize")
async def summarize(req: TextRequest):
    messages = [
        {"role": "system", "content": "Vous êtes un assistant."},
        {
            "role": "user",
            "content": f"Résume le texte en 2 phrases : {req.text}",
        },
    ]
    summary = chat(messages)
    return {"summary": summary}


@app.post("/named-entities")
async def named_entities(req: TextRequest):
    instruction = (
        "Extract the named entities from the text as JSON array of objects with"
        " 'text' and 'label'."
    )
    messages = [
        {"role": "system", "content": instruction},
        {"role": "user", "content": req.text},
    ]
    data = chat(messages)
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {"raw": data}


if __name__ == "__main__":
    # Dev only: run "python main.py" and open http://localhost:8080
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
