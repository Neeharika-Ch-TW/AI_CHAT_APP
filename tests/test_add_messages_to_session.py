from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# Behavior:
# Validates if session exists
# Validates if role is user or assistant

def test_add_messages_to_session_happy_path():
    response = client.post(f'/sessions/{1}/messages', json={"role": "user", "content": "What is AI?"})
    assert response.status_code == 200
    assert response.json() == {'message': 'messages added to the session successfully!'}

def test_session_not_found():
    response = client.post(f'/sessions/{2}/messages', json={"role": "user", "content": "What is AI?"})
    assert response.status_code == 404
    assert response.json() == {'message': 'Session ID not Found!'}

def test_validate_role():
    response = client.post(f'/sessions/{1}/messages', json={"role": "admin", "content": "What is AI?"})
    assert response.status_code == 422
