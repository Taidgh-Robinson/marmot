from pydantic import BaseModel
from typing import List

from models.quote_doc import QuoteDoc 
from models.quote_context import QuoteContext

class MovieQuote(BaseModel):
    quote_doc: QuoteDoc
    quote_contexts: List[QuoteContext]

    def display_full_quote(self):
        full_quote = ''
        for ctx in self.quote_contexts[:-1]:
            full_quote += ctx.phrase + ' '
        full_quote += self.quote_contexts[-1].phrase
        return full_quote

    