from pydantic import BaseModel

class MovieRecord(BaseModel):
    title: str 
    poster: str
    imdb_id: str