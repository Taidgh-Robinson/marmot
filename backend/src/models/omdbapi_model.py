from pydantic import BaseModel
from typing import List

class Rating(BaseModel):
    Source: str
    Value: str

class OMDBAPIModel(BaseModel):
    Title: str
    Year: str
    Rated: str
    Released: str
    Runtime: str
    Genre: str
    Director: str
    Writer: str
    Actors: str
    Plot: str
    Language: str
    Country: str
    Awards: str
    Poster: str
    Metascore: str
    imdbRating: str
    imdbVotes: str
    imdbID: str
    Type: str
    DVD: str
    BoxOffice: str
    Production: str
    Website: str
    Response: bool
    Ratings: List[Rating]
