from src.config.postgres_config import PostgresConfig
import asyncio
import asyncpg

class PostgresClient:
    
    def __init__(self):
        self.config: PostgresConfig = PostgresConfig()
        self.connection_string = f'postgresql://{self.config.user}:{self.config.password}@{self.config.host}/{self.config.db}'

    async def fetch_all_function(self):
        conn = await asyncpg.connect(self.connection_string)
        return await conn.fetch('SELECT * FROM date_to_quote')