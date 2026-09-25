from src.clients.quodb_client import QuoDBClient
from fastapi import Request

def get_quodb_client(request: Request):
    return QuoDBClient(request.app.state.http_client)
