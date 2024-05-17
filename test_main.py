import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_podcasts():
    response = client.get("/podcasts")
    assert response.status_code == 200
    assert response.json() == []

def test_create_podcast():
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}

    response = client.post("/podcasts", json=new_podcast)
    assert response.status_code == 200
    assert response.json() == new_podcast

def test_get_podcast_by_id():
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}
    response = client.post("/podcasts", json=new_podcast)
    podcast_id = response.json()["id"]
    response = client.get(f"/podcasts/{podcast_id}")
    assert response.status_code == 200
    assert response.json() == new_podcast

def test_update_podcast():
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}
    response = client.post("/podcasts", json=new_podcast)
    podcast_id = response.json()["id"]
    updated_podcast = {"id": 1, "name": "My Updated Podcast", "speaker": "Jane Doe", "topic": "Science", "location": "London"}
    response = client.put(f"/podcasts/{podcast_id}", json=updated_podcast)
    assert response.status_code == 200
    assert response.json() == updated_podcast

def test_delete_podcast():
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}
    response = client.post("/podcasts", json=new_podcast)
    podcast_id = response.json()["id"]
    response = client.delete(f"/podcasts/{podcast_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Podcast deleted successfully"}
