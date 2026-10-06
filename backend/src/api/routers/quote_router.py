from fastapi import APIRouter, Query, Depends
from src.api.core.depdencies import get_quodb_client, get_postgres_client, get_omdb_api_client, get_llm_client
from src.utils.quote_pipeline import full_quote_pipeline
from src.utils.date_utils import get_todays_date
from src.clients.postgres_client import PostgresClient
from src.clients.quodb_client import QuoDBClient
from src.clients.omdbapi_client import OMDBAPIClient
from src.clients.llm_client import LLMClient
from src.models.database_models.date_to_quote_record import DateToQuoteRecord

router = APIRouter()


# TODO
@router.get("/quote_of_the_day")
async def get_quote_of_the_day(    quodb_client: QuoDBClient = Depends(get_quodb_client),
    postgres_client: PostgresClient = Depends(get_postgres_client),
    llm_client: LLMClient = Depends(get_llm_client),
    omdb_api_client: OMDBAPIClient = Depends(get_omdb_api_client),
):
    date = get_todays_date()
    query = date[:5]

    cached_quote: DateToQuoteRecord = await postgres_client.fetch_quote_by_date(query)
    if cached_quote:
        poster_url = None
        if cached_quote.movie:
            movie = await postgres_client.fetch_movie(cached_quote.movie)
            if movie:
                poster_url = movie.poster

        return {"quote": cached_quote.quote, "movie": cached_quote.movie, "poster_url": poster_url}
        

    quotes = await full_quote_pipeline(quodb_client, date, llm_client, postgres_client, omdb_api_client)
    
    saved_quote = await postgres_client.fetch_quote_by_date(query)
    
    if saved_quote:
        poster_url = None
        if saved_quote.movie:
            movie = await postgres_client.fetch_movie(saved_quote.movie)
            if movie:
                poster_url = movie.poster
                
        return {"quote": saved_quote.quote, "movie": saved_quote.movie, "poster_url": poster_url}

    return {"quote": None, "movie": None, "poster_url": None}    

# TODO
@router.get("/get_quote")
async def get_quote(
    quodb_client: QuoDBClient = Depends(get_quodb_client),
    postgres_client: PostgresClient = Depends(get_postgres_client),
    llm_client: LLMClient = Depends(get_llm_client),
    omdb_api_client: OMDBAPIClient = Depends(get_omdb_api_client),
    date: str = Query(..., regex=r"^\d{2}/\d{2}/\d{4}$"),
):

    query = date[:5]
    cached_quote = await postgres_client.fetch_quote_by_date(query)
    if cached_quote:
        poster_url = None
        if cached_quote.movie:
            movie = await postgres_client.fetch_movie(cached_quote.movie)
            if movie:
                poster_url = movie.poster
                
        return {"quote": cached_quote.quote, "movie": cached_quote.movie, "poster_url": poster_url}

    quotes = await full_quote_pipeline(quodb_client, date, llm_client, postgres_client, omdb_api_client)

    saved_quote = await postgres_client.fetch_quote_by_date(query)
    if saved_quote:
        poster_url = None
        if saved_quote.movie:
            movie = await postgres_client.fetch_movie(saved_quote.movie)
            if movie:
                poster_url = movie.poster
                
        return {"quote": saved_quote.quote, "movie": saved_quote.movie, "poster_url": poster_url}

    return {"quote": None, "movie": None, "poster_url": None}    