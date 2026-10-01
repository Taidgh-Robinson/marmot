from src.clients.quodb_client import QuoDBClient
from src.clients.postgres_client import PostgresClient
from fastapi import Request


def get_quodb_client(request: Request) -> QuoDBClient:
    return QuoDBClient(request.app.state.http_client)

def get_postgres_client() -> PostgresClient: 
    return PostgresClient() 