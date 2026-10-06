from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DateToQuoteRecord(BaseModel):
    quote_date: str 
    quote: Optional[str] = None
    movie: Optional[str] = None
    quote_stored_time: datetime = Field(default_factory=datetime.now)