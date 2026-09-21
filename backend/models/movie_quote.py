from __future__ import annotations
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

    def has_overlapping_contexts(self, other_quote: MovieQuote):
        ctx_ids = [ctx.phrase_id for ctx in self.quote_contexts]
        other_ctx_ids = [ctx.phrase_id for ctx in other_quote.quote_contexts]
        for ctx in other_ctx_ids: 
            if ctx in ctx_ids:
                return True 

        return False
    
