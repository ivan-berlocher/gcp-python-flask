import os
import openai

MODEL_NAME = "gpt-4o-mini"
_api_key = os.getenv("OPENAI_API_KEY")

if not _api_key:
    raise EnvironmentError("OPENAI_API_KEY environment variable is not set")

_client = openai.OpenAI(api_key=_api_key)

def chat(messages, model: str = MODEL_NAME) -> str:
    """Send a list of messages to the OpenAI chat completion API."""
    response = _client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content.strip()
