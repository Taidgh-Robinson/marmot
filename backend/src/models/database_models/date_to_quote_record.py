from pydantic import BaseModel, Field
from datetime import datetime

class DateToQuoteRecord(BaseModel):
    quote_date: str 
    quote: str
    movie: str
    quote_stored_time: datetime = Field(default_factory=datetime.now)