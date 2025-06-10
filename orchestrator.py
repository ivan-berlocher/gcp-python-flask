from fastapi import APIRouter, WebSocket, HTTPException
import asyncio

router = APIRouter()

# Dummy in-memory stores for example purposes
# Each tool advertises the POST endpoint that executes it.
TOOLS = [
    {"id": "summarize", "name": "Summarize text", "endpoint": "/summarize"},
    {
        "id": "named-entities",
        "name": "Extract named entities",
        "endpoint": "/named-entities",
    },
]

# Basic JSON Schemas describing the configuration for each tool.
# These would normally be defined alongside the tool implementation.
TOOL_SCHEMAS = {
    "summarize": {
        "title": "Summarize text",
        "type": "object",
        "properties": {
            "text": {"title": "Text", "type": "string"},
        },
        "required": ["text"],
    },
    "named-entities": {
        "title": "Extract named entities",
        "type": "object",
        "properties": {
            "text": {"title": "Text", "type": "string"},
        },
        "required": ["text"],
    },
}

WORKFLOWS = {}

@router.get("/tools")
async def list_tools():
    """Return the registered tools."""
    return TOOLS


@router.get("/tools/{tool_id}/schema")
async def get_tool_schema(tool_id: str):
    """Return the JSON Schema for a tool."""
    schema = TOOL_SCHEMAS.get(tool_id)
    if not schema:
        raise HTTPException(status_code=404, detail="Tool not found")
    return schema

@router.get("/workflows/{workflow_id}")
async def get_workflow(workflow_id: str):
    """Return a workflow configuration."""
    return WORKFLOWS.get(workflow_id, {"id": workflow_id, "steps": []})

@router.post("/workflows")
async def create_workflow(config: dict):
    """Create a workflow."""
    workflow_id = f"wf{len(WORKFLOWS)+1}"
    WORKFLOWS[workflow_id] = config
    return {"id": workflow_id}

@router.post("/workflows/{workflow_id}/run")
async def run_workflow(workflow_id: str):
    """Start a workflow run and return its run identifier."""
    run_id = f"run-{workflow_id}"
    return {"runId": run_id}

@router.websocket("/ws/workflows/{run_id}/events")
async def workflow_events(websocket: WebSocket, run_id: str):
    """Yield log lines for a running workflow."""
    await websocket.accept()
    for i in range(5):
        await websocket.send_text(f"{run_id}: log {i+1}")
        await asyncio.sleep(0.5)
    await websocket.close()
