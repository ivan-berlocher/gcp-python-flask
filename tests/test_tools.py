import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_tools_includes_registered_entries():
    response = client.get("/tools")
    assert response.status_code == 200
    tools = response.json()
    ids = {tool["id"] for tool in tools}
    assert {"summarize", "named-entities"} <= ids


@pytest.mark.parametrize("tool_id", ["summarize", "named-entities"])
def test_tool_schema_endpoint(tool_id):
    response = client.get(f"/tools/{tool_id}/schema")
    assert response.status_code == 200
    schema = response.json()
    assert schema["type"] == "object"

