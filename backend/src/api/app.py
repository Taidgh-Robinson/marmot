#Temp file so I can still use main to test logic, will be moved up to main later
import httpx
from fastapi import FastAPI
from src.api.routers.quote_router import router as quote_router 
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = httpx.AsyncClient()

    yield

    await app.state.http_client.aclose()

app = FastAPI(lifespan=lifespan)

app.include_router(quote_router)