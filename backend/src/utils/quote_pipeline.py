from src.utils.date_utils import get_perumtations_of_date
from src.config.logging_config import logger
from src.utils.quote_utils import quote_has_date
from src.clients.quodb_client import QuoDBClient
from src.clients.llm_client import LLMClient
from src.constants.queries import generate_crop_query, generate_score_query
from src.clients.postgres_client import PostgresClient
from src.clients.omdbapi_client import OMDBAPIClient
from src.models.database_models.movie_record import MovieRecord
from src.models.database_models.date_to_quote_record import DateToQuoteRecord
import json 

def parse_score_response(response: str) -> dict:
    response = response.strip()

    if response.startswith("```"):
        response = response.removeprefix("```json")
        response = response.removeprefix("```")
        response = response.removesuffix("```")
        response = response.strip()

    return json.loads(response)

async def full_quote_pipeline(quoDBClient: QuoDBClient, day_to_fetch, llmClient: LLMClient, postgresClient: PostgresClient, omdbAPIClient: OMDBAPIClient):
    days = get_perumtations_of_date(day_to_fetch)
    all_quotes = []

    # Fetch all quotes
    for day in days:
        data = await quoDBClient.get_all_full_movie_quotes_for_day(day)
        all_quotes.extend(data)

    # Filter out quotes that don't actually contain the date
    # Ex. She had not completed a play in seven years. 17 October, third examination of Dudley Heinsbergen shows up for Oct 3rd.
    filtered_quotes = [
        quote
        for quote in all_quotes
        if quote_has_date(quote.display_full_quote(), days)
    ]

    logger.info(f"Size of filtered quotes: {len(filtered_quotes)}")

    seen = set()
    unique_filtered_quotes = []
    for q in filtered_quotes:
        quote_str = q.display_full_quote()
        if quote_str not in seen:
            seen.add(quote_str)
            unique_filtered_quotes.append(q)

    logger.info(f"Size of filtered quotes: {len(unique_filtered_quotes)}")

    # Crop  quotes using an LLM
    for quote in unique_filtered_quotes:
        logger.info(f"Going to crop full quote: {quote.display_full_quote()} from movie: {quote.quote_doc.title}.")
        llm_response = await llmClient.query_llm(generate_crop_query(quote.quote_doc.title, quote.display_full_quote()))
        crop = llm_response.choices[0].message.content
        logger.info(f"LLM returned: {crop}.")
        quote.llm_cropped_quote = crop

    # Filter out cropped quotes that dont have the date in them
    filtered_llm_cropped_quotes = [
        quote
        for quote in unique_filtered_quotes
        if quote_has_date(quote.llm_cropped_quote, days)
    ]

    if len(filtered_llm_cropped_quotes) == 0:
        logger.info("No filtered quotes for the day!")
        date_to_quote_record = DateToQuoteRecord(quote_date=day_to_fetch[:5], quote=None, movie=None)
        await postgresClient.insert_into_date_to_quote(date_to_quote_record)

    if len(filtered_llm_cropped_quotes) > 0:

        # Score 
        temp_quote = None
        temp_quote_score = 0

        for quote in filtered_llm_cropped_quotes:
            llm_response = await llmClient.query_llm(generate_score_query(quote.quote_doc.title, quote.display_full_quote()))
            score = parse_score_response(llm_response.choices[0].message.content)['total']
            logger.info(f"LLM returned a score of {score} for quote {quote.display_full_quote()} - {quote.quote_doc.title}")
            if int(score) > temp_quote_score:
                temp_quote = quote
                temp_quote_score = score 

        # Save
        movie_title = temp_quote.quote_doc.title
        try:
            movie_data = await omdbAPIClient.get_movie_info(movie_title)
        except Exception as e:
            logger.info(f"Failed to fetch movie from omdb! {e}")
        movie = None
        if movie_data:
            movie_record = MovieRecord(title=movie_data.Title, poster=movie_data.Poster, imdb_id=movie_data.imdbID)
            try:
                await postgresClient.insert_into_movie(movie_record)
            except Exception as e:
                logger.error(f"Failed to store movie with error {e}")

            movie = movie_record.title

        date_to_quote_record = DateToQuoteRecord(quote_date=day_to_fetch[:5], quote=temp_quote.llm_cropped_quote, movie=movie)
        try:
            await postgresClient.insert_into_date_to_quote(date_to_quote_record)
        except Exception as e:
            logger.error(f"Failed to store movie with error {e}")


    # Return all data
    return {"all": all_quotes, "filtered_quotes": filtered_quotes, "filtered_llm_cropped_quotes": filtered_llm_cropped_quotes}
