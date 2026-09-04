from clients.quodb_client import QuoDBClient
from models.quote_context import QuoteContext
from typing import List
import httpx
import asyncio

def assemble_quote(contexts: List[QuoteContext]):
    ret = ''
    for context in contexts:
        ret += context.phrase + ' '
    return ret


async def main():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)
    data = await qdbc.get_all_quote_docs("October 3rd", "10")
    for quote in data:
        contexts = await qdbc.get_quote_contexts(quote)
        print(assemble_quote(contexts))
        print()


if __name__ == "__main__":
    asyncio.run(main())
