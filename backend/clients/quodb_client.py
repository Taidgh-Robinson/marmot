import httpx
from models.quote_doc import QuoteDoc
from models.quote_context import QuoteContext
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
