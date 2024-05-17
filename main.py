from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Podcast(BaseModel):
    """
    Represents a podcast with the following attributes:
    - id: Unique identifier of the podcast (integer)
    - name: Name of the podcast (string)
    - speaker: Name of the speaker(s) (string)
    - topic: Topic of the podcast (string)
    - location: Location where the podcast was recorded (string)
    """
    id: int
    name: str
    speaker: str
    topic: str
    location: str

podcasts = []

@app.get("/podcasts")
async def get_all_podcasts():
    """
    Returns a list of all podcasts stored in the application.
    """
    return podcasts

@app.get("/podcasts/{podcast_id}")
async def get_podcast_by_id(podcast_id: int = Path(..., title="Podcast ID", ge=1)):
    """
    Returns the podcast with the specified ID.
    Raises an error if the podcast is not found.
    """
    for podcast in podcasts:
        if podcast.id == podcast_id:
            return podcast
    return None

@app.post("/podcasts")
async def create_podcast(podcast: Podcast):
    """
    Creates a new podcast and adds it to the list of podcasts.
    Returns the newly created podcast object.
    """
    podcasts.append(podcast)
    return podcast

@app.put("/podcasts/{podcast_id}")
async def update_podcast(podcast_id: int, updated_podcast: Podcast):
    """
    Updates an existing podcast with the specified ID.
    Returns the updated podcast object.
    Raises an error if the podcast is not found.
    """
    for i, podcast in enumerate(podcasts):
        if podcast.id == podcast_id:
            podcasts[i] = updated_podcast
            return updated_podcast
    return None

@app.delete("/podcasts/{podcast_id}")
async def delete_podcast(podcast_id: int):
    """
    Deletes the podcast with the specified ID.
    Returns a message indicating whether the deletion was successful.
    """
    for i, podcast in enumerate(podcasts):
        if podcast.id == podcast_id:
            del podcasts[i]
            return {"message": "Podcast deleted successfully"}
    return {"message": "Podcast not found"}
