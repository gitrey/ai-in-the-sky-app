import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_podcasts():
    """
    This test checks that the `GET /podcasts` endpoint returns a list of all podcasts stored in the application.
    """
    response = client.get("/podcasts")
    assert response.status_code == 200
    assert response.json() == []

def test_create_podcast():
    """
    This test checks that the `POST /podcasts` endpoint creates a new podcast and returns the newly created podcast object.
    """
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}

    response = client.post("/podcasts", json=new_podcast)
    assert response.status_code == 200
    assert response.json() == new_podcast

def test_get_podcast_by_id():
    """
    This test checks that the `GET /podcasts/{podcast_id}` endpoint returns the podcast with the specified ID.
    """
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}
    response = client.post("/podcasts", json=new_podcast)
    podcast_id = response.json()["id"]
    response = client.get(f"/podcasts/{podcast_id}")
    assert response.status_code == 200
    assert response.json() == new_podcast

def test_update_podcast():
    """
    This test checks that the `PUT /podcasts/{podcast_id}` endpoint updates an existing podcast and returns the updated podcast object.
    """
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}
    response = client.post("/podcasts", json=new_podcast)
    podcast_id = response.json()["id"]
    updated_podcast = {"id": 1, "name": "My Updated Podcast", "speaker": "Jane Doe", "topic": "Science", "location": "London"}
    response = client.put(f"/podcasts/{podcast_id}", json=updated_podcast)
    assert response.status_code == 200
    assert response.json() == updated_podcast

def test_delete_podcast():
    """
    This test checks that the `DELETE /podcasts/{podcast_id}` endpoint deletes the podcast with the specified ID and returns a message indicating whether the deletion was successful.
    """
    new_podcast = {"id": 1, "name": "My Podcast", "speaker": "John Doe", "topic": "Technology", "location": "New York"}
    response = client.post("/podcasts", json=new_podcast)
    podcast_id = response.json()["id"]
    response = client.delete(f"/podcasts/{podcast_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Podcast deleted successfully"}

