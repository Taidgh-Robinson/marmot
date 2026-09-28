import httpx
from src.config.omdbapi_config import OMDBAPIConfig

class OMDBAPIClient:

    def __init__(self, client: httpx.AsyncClient):
        self.client = client
        self.config: OMDBAPIConfig = OMDBAPIConfig()

    async def get_movie_info(self, movie_title: str):
        params = {
            "apikey": self.config.api_key,
            "t": movie_title,
            "plot": "short"
        }

        resp = await self.client.get("http://www.omdbapi.com/", params=params)
        return resp