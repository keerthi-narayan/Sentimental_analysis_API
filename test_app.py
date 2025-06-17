import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "API is running"}

def test_single_text_analysis(client):
    response = client.post('/analyze', json={"text": "I love Python!"})
    assert response.status_code == 200
    assert "analysis" in response.json
    assert "text" in response.json
    assert "preprocessed_text" in response.json

def test_batch_text_analysis(client):
    response = client.post('/batch', json={
        "texts": ["I love Python!", "Debugging is frustrating sometimes."]
    })
    assert response.status_code == 200
    assert isinstance(response.json, list)
    for item in response.json:
        assert "analysis" in item
        assert "text" in item
        assert "preprocessed_text" in item

def test_invalid_input_analyze(client):
    response = client.post('/analyze', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid input"}

def test_invalid_input_batch(client):
    response = client.post('/batch', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid input"}

def test_character_limit_exceeded(client):
    response = client.post('/analyze', json={"text": "a" * 281})
    assert response.status_code == 400
    assert response.json == {"error": "Text exceeds character limit of 280"}

def test_multilingual_input(client):
    response = client.post('/analyze', json={"text": "J'aime Python!"})
    assert response.status_code == 200
    assert "analysis" in response.json

def test_history_endpoint(client):
    client.post('/analyze', json={"text": "I love Flask!"})
    response = client.get('/history')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

