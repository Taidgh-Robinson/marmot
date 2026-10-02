from src.clients.quodb_client import QuoDBClient
from src.models.quote_context import QuoteContext
from src.clients.llm_client import LLMClient
from src.constants.queries import generate_crop_query
from src.utils.quote_pipeline import full_quote_pipeline
from src.utils.date_utils import get_perumtations_of_date
from src.utils.quote_utils import quote_has_date
from typing import List
import httpx
import asyncio


async def get_oct_3rd_movie_quotes():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)
    llm = LLMClient()
    pipeline = await full_quote_pipeline(qdbc, '10/03/2026', llm)
    return pipeline

async def get_july_4th_movie_quotes():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)
    llm = LLMClient()
    pipeline = await full_quote_pipeline(qdbc, '07/04/2026', llm)

    return pipeline

async def main():
    print("--- july 4th quotes ---")
    oct_3rd = await get_july_4th_movie_quotes()
    for quote in oct_3rd['filtered_quotes']:
        print(f'{quote.display_full_quote()} - {quote.llm_cropped_quotec}')



if __name__ == "__main__":
    asyncio.run(main())
