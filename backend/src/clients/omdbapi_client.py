import httpx
from src.config.omdbapi_config import OMDBAPIConfig
from src.models.omdbapi_model import OMDBAPIModel

class OMDBAPIClient:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client
        self.config: OMDBAPIConfig = OMDBAPIConfig()

    async def get_movie_info(self, movie_title: str) -> OMDBAPIModel | None:
        params = {
            "apikey": self.config.api_key,
            "t": movie_title,
            "plot": "short"
        }

        resp = await self.client.get("http://www.omdbapi.com/", params=params)
        if resp.status_code != 200:
            return None
        
        return OMDBAPIModel(**resp.json())