# Temp file so I can still use main to test logic, will be moved up to main later
import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers.quote_router import router as quote_router
from contextlib import asynccontextmanager
from pyliquibase import Pyliquibase
from src.config.logging_config import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = httpx.AsyncClient()

    logger.info("Running database migrations.")
    try:
        liquibase = Pyliquibase(defaultsFile="changelogs/liquibase.properties")
        liquibase.update()
        logger.info("Migrations applied")
    except Exception as e:
        logger.error(f"Failed to apply migrations: {e}")
        raise e 

    yield

    await app.state.http_client.aclose()


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quote_router)
