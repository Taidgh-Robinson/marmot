from clients.quodb_client import QuoDBClient
from models.quote_context import QuoteContext
from clients.llm_client import LLMClient
from constants.queries import generate_crop_query
from utils.date_utils import get_perumtations_of_date
from typing import List
import httpx
import asyncio


async def print_oct_3rd_movie_quotes():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)
    llm = LLMClient()

    days = get_perumtations_of_date('10/03/2026')
    for day in days:
        data = await qdbc.get_all_full_movie_quotes_for_day(day)
        for quote in data:
            print(quote.quote_doc.title + ' - ' + quote.display_full_quote())
            resp = await llm.query_llm(generate_crop_query(quote.quote_doc.title, quote.display_full_quote()))
            print(quote.quote_doc.title + ' - ' + resp.choices[0].message.content)
            print()

async def print_july_4th_movie_quotes():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)

    days = get_perumtations_of_date('07/04/2026')
    for day in days:
        data = await qdbc.get_all_full_movie_quotes_for_day(day)
        for quote in data:
            print(quote.quote_doc.title + ' - ' + quote.display_full_quote())
            print()


async def main():
    print('--- october 3rd quotes ---')
    await print_oct_3rd_movie_quotes()
    print('--- july 4th quotes ---')
    await print_july_4th_movie_quotes()

if __name__ == "__main__":
    asyncio.run(main())
