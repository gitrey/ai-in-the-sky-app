from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Podcast(BaseModel):
    id: int
    name: str
    speaker: str
    topic: str
    location: str

podcasts = []

@app.get("/podcasts")
async def get_all_podcasts():
    return podcasts

@app.get("/podcasts/{podcast_id}")
async def get_podcast_by_id(podcast_id: int = Path(..., title="Podcast ID", ge=1)):
    for podcast in podcasts:
        if podcast.id == podcast_id:
            return podcast
    return None

@app.post("/podcasts")
async def create_podcast(podcast: Podcast):
    podcasts.append(podcast)
    return podcast

@app.put("/podcasts/{podcast_id}")
async def update_podcast(podcast_id: int, updated_podcast: Podcast):
    for i, podcast in enumerate(podcasts):
        if podcast.id == podcast_id:
            podcasts[i] = updated_podcast
            return updated_podcast
    return None

@app.delete("/podcasts/{podcast_id}")
async def delete_podcast(podcast_id: int):
    for i, podcast in enumerate(podcasts):
        if podcast.id == podcast_id:
            del podcasts[i]
            return {"message": "Podcast deleted successfully"}
    return {"message": "Podcast not found"}
