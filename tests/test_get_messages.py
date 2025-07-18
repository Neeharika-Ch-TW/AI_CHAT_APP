from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Behavior:
# Returns full chat history for the session
# Add filtering by role using query param (use List comprehension)
# Raises Exception  if session not found


def test_get_messages():
    response = client.get(f'/sessions/{1}/messages')
    assert response.status_code == 200
    assert response.json() == [{'role': 'user', 'content': 'What is AI?'}]

def test_get_messages_assistant_role():
    client.post(f'/sessions/{1}/messages', json={"role": "assistant", "content": "What is AI?"})
    response = client.get(f'/sessions/{1}/messages',params={"role":"assistant"})
    assert response.status_code == 200
    assert response.json() == [{'role': 'assistant', 'content': 'What is AI?'}]