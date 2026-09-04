import httpx 
from models.quote_doc import QuoteDoc
from typing import List 

class QuoDBClient():
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get_all_quote_docs(self, query: str, titles_per_page: str) -> List[QuoteDoc]:
        docs = []
        page = 1
        resp = await self.client.get(f'https://api.quodb.com/search/{query}?titles_per_page={titles_per_page}&phrases_per_title=5&page={page}')
        docs_resp = resp.json()['docs']
        while docs_resp:
            docs.extend(docs_resp)
            page += 1 
            resp = await self.client.get(f'https://api.quodb.com/search/{query}?titles_per_page={titles_per_page}&phrases_per_title=5&page={page}')
            docs_resp = resp.json()['docs']

        return [QuoteDoc(**doc) for doc in docs] 