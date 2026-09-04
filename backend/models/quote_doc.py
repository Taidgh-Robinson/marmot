from pydantic import BaseModel

class QuoteDoc(BaseModel):
    title_id: str
    title: str
    phrase_id: int
    year: int 
    image: str | None
    root_imdb: int 
    serie: str | None 
    num_found: int 
    phrase: str
    time: int 