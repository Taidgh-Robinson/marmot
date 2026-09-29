from src.config.postgres_config import PostgresConfig
from src.models.database_models.movie_record import MovieRecord
from src.models.database_models.date_to_quote_record import DateToQuoteRecord

import asyncio
import asyncpg


class PostgresClient:
    def __init__(self):
        self.config: PostgresConfig = PostgresConfig()
        self.connection_string = f"postgresql://{self.config.user}:{self.config.password}@{self.config.host}/{self.config.db}"

    async def fetch_all_function(self):
        conn = await asyncpg.connect(self.connection_string)
        data = await conn.fetch("SELECT * FROM date_to_quote")
        await conn.close()
        
        return data 

    async def insert_into_movie(self, movie_record: MovieRecord):
        conn = await asyncpg.connect(self.connection_string)
        await conn.execute(
        '''
        INSERT INTO MOVIE (title, poster, imdb_id)
        VALUES ($1, $2, $3)
        ''', movie_record.title, movie_record.poster, movie_record.imdb_id)
        await conn.close()

    async def fetch_movie(self, movie_title: str) -> MovieRecord | None:
        conn = await asyncpg.connect(self.connection_string)
        row = await conn.fetchrow('SELECT * FROM MOVIE WHERE title = $1', movie_title)
        await conn.close()

        if row:
            return MovieRecord(**row)
        return None 

    async def insert_into_date_to_quote(self, date_to_quote_record: DateToQuoteRecord):
        conn = await asyncpg.connect(self.connection_string)
        await conn.execute(
        '''
        INSERT INTO DATE_TO_QUOTE (quote_date, quote, movie)
        VALUES ($1, $2, $3)
        ''', date_to_quote_record.quote_date, date_to_quote_record.quote, date_to_quote_record.movie)
        await conn.close()

    async def fetch_quote_by_date(self, date: str) -> DateToQuoteRecord | None:
        conn = await asyncpg.connect(self.connection_string)
        row = await conn.fetchrow('SELECT * FROM DATE_TO_QUOTE WHERE quote_date = $1', date)
        await conn.close()
        if row:
            return DateToQuoteRecord(**row)
        
        return None 
