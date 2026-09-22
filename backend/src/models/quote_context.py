from pydantic import BaseModel
from typing import List


class QuoteContext(BaseModel):
    rating_imdb: float
    image: str | None = None
    year: int
    title_id: int
    phrase_profanity: bool
    title: str
    uuid: str
    duration: int
    title_profanity: bool
    imdb: int
    phrase: str
    user_id: int
    votes_imdb: int
    phrase_id: int
    time: int
    genres: List[str] | None = None
    episode: int
    root_imdb: int
    season: int
    score: int
