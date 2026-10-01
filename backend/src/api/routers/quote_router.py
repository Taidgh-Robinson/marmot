from fastapi import APIRouter, Response, Query, Depends
from src.api.core.depdencies import get_quodb_client, get_postgres_client
from src.utils.quote_pipeline import full_quote_pipeline
from src.utils.date_utils import get_todays_date
from src.clients.postgres_client import PostgresClient
from src.clients.quodb_client import QuoDBClient

router = APIRouter()


# TODO
@router.get("/quote_of_the_day")
async def get_quote_of_the_day(quodb_client: QuoDBClient = Depends(get_quodb_client), postgres_client: PostgresClient = Depends(get_postgres_client)):
    date = get_todays_date()
    query = date[:5]

    cached_quote = await postgres_client.fetch_quote_by_date(query)
    if cached_quote:
        return {"quote": cached_quote.quote}
        

    quotes = await full_quote_pipeline(quodb_client, date)
    fake_data = quotes["filtered_quotes"][0]

    return {"quote": fake_data.display_full_quote()}


# TODO
@router.get("/get_quote")
async def get_quote(
    quodb_client: QuoDBClient = Depends(get_quodb_client),
    postgres_client: PostgresClient = Depends(get_postgres_client),
    date: str = Query(..., regex=r"^\d{2}/\d{2}/\d{4}$"),
):

    query = date[:5]
    cached_quote = await postgres_client.fetch_quote_by_date(query)
    if cached_quote:
        return {"quote": cached_quote.quote}

    quotes = await full_quote_pipeline(quodb_client, date)
    fake_data = quotes["filtered_quotes"][0]

    return {"quote": fake_data.display_full_quote()}
    