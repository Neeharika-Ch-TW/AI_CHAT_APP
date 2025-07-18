from main import app
from fastapi.testclient import TestClient
from helpers.custom_helpers import utc_time_calculator

client = TestClient(app)


# Behavior:
# Add validation: Reject empty usernames.
# Assign session_id = len(session_store) + 1
# Set created_at to current UTC timestamp
# Add new entry to session_store


def test_store_new_session():
    # provided input in uppercase with leading and trailing spaces, code is stripping the spaces and storing values in
    # lower case as expected
    response = client.post('/sessions', json={"session_user": " NEEHARIKA  "})
    assert response.status_code == 201
    assert response.json() == {'session_id': '1', 'created_at': utc_time_calculator(), 'session_user': 'neeharika'}


def test_empty_username():
    # no username provided is a validation error
    response = client.post('/sessions', json={"session_user": ""})
    assert response.status_code == 422


def test_space_as_username():
    # a space provided as username is not valid
    response = client.post('/sessions', json={"session_user": " "})
    assert response.status_code == 422
