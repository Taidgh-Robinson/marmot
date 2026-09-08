from clients.quodb_client import QuoDBClient
from models.quote_context import QuoteContext
from utils.date_utils import get_perumtations_of_date
from typing import List
import httpx
import asyncio

def assemble_quote(contexts: List[QuoteContext]):
    ret = ''
    for context in contexts:
        ret += context.phrase + ' '
    return ret

async def print_oct_3rd_movie_quotes():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)

    days = get_perumtations_of_date('10/03/2026')
    for day in days:
        data = await qdbc.get_all_quote_docs(day, "10")
        for quote in data:
            #Filter out TV shows
            if not quote.serie:
                contexts = await qdbc.get_quote_contexts(quote)
                print(quote.title + ' - ' + assemble_quote(contexts))
                print()

async def print_july_4th_movie_quotes():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)

    days = get_perumtations_of_date('07/04/2026')
    for day in days:
        data = await qdbc.get_all_quote_docs(day, "10")
        for quote in data:
            #Filter out TV shows
            if not quote.serie:
                contexts = await qdbc.get_quote_contexts(quote)
                print(quote.title + ' - ' + assemble_quote(contexts))
                print()


async def main():
    print('--- october 3rd quotes ---')
    await print_oct_3rd_movie_quotes()
    print('--- july 4th quotes ---')
    await print_july_4th_movie_quotes()

if __name__ == "__main__":
    asyncio.run(main())
