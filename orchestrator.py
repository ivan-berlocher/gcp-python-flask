from fastapi import APIRouter, WebSocket
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

WORKFLOWS = {}

@router.get("/tools")
async def list_tools():
    """Return the registered tools."""
    return TOOLS

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
