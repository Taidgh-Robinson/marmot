from clients.quodb_client import QuoDBClient
import httpx 
import asyncio

async def main():
    client = httpx.AsyncClient()
    qdbc = QuoDBClient(client)
    data = await qdbc.get_all_quote_docs("October 3rd", "10")
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
