from src.clients.quodb_client import QuoDBClient
from src.clients.postgres_client import PostgresClient
from src.clients.omdbapi_client import OMDBAPIClient
from src.clients.llm_client import LLMClient
from fastapi import Request


def get_quodb_client(request: Request) -> QuoDBClient:
    return QuoDBClient(request.app.state.http_client)

def get_postgres_client() -> PostgresClient: 
    return PostgresClient() 

def get_omdb_api_client(request: Request) -> OMDBAPIClient:
    return OMDBAPIClient(request.app.state.http_client)

def get_llm_client() -> LLMClient:
    return LLMClient()