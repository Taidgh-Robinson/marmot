import httpx
from src.models.quote_doc import QuoteDoc
from src.models.quote_context import QuoteContext
from src.models.movie_quote import MovieQuote
from typing import List


class QuoDBClient:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get_all_quote_docs(
        self, query: str, titles_per_page: str
    ) -> List[QuoteDoc]:
        docs = []
        page = 1
        resp = await self.client.get(
            f"https://api.quodb.com/search/{query}?titles_per_page={titles_per_page}&phrases_per_title=5&page={page}"
        )
        resp_docs = resp.json()["docs"]
        while resp_docs:
            docs.extend(resp_docs)
            page += 1
            resp = await self.client.get(
                f"https://api.quodb.com/search/{query}?titles_per_page={titles_per_page}&phrases_per_title=5&page={page}"
            )
            resp_docs = resp.json()["docs"]

        return [QuoteDoc(**doc) for doc in docs]

    async def get_quote_contexts(self, quote_doc: QuoteDoc) -> List[QuoteContext]:
        resp = await self.client.get(
            f"https://api.quodb.com/quotes/{quote_doc.title_id}/{quote_doc.phrase_id}"
        )
        resp_docs = resp.json()["docs"]
        return [QuoteContext(**doc) for doc in resp_docs]

    async def get_all_full_movie_quotes_for_day(
        self, day: str, titles_per_page: str = "10"
    ) -> List[MovieQuote]:
        quotes = []
        data = await self.get_all_quote_docs(day, titles_per_page)
        for quote in data:
            # Filter out TV shows
            if not quote.serie:
                contexts = await self.get_quote_contexts(quote)
                full_quote = MovieQuote(quote_doc=quote, quote_contexts=contexts)
                quotes.append(full_quote)

        return quotes
