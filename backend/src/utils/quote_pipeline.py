from src.utils.date_utils import get_perumtations_of_date
from src.config.logging_config import logger
from src.utils.quote_utils import quote_has_date
from src.clients.quodb_client import QuoDBClient
from src.clients.llm_client import LLMClient
from src.constants.queries import generate_crop_query
from src.clients.postgres_client import PostgresClient
from src.clients.omdbapi_client import OMDBAPIClient
from src.models.database_models.movie_record import MovieRecord
from src.models.database_models.date_to_quote_record import DateToQuoteRecord

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

    for quote in filtered_quotes:
        logger.info(f"Going to crop full quote: {quote.display_full_quote()} from movie: {quote.quote_doc.title}.")
        llm_response = await llmClient.query_llm(generate_crop_query(quote.quote_doc.title, quote.display_full_quote()))
        crop = llm_response.choices[0].message.content
        logger.info(f"LLM returned: {crop}.")
        quote.llm_cropped_quote = crop

    filtered_llm_cropped_quotes = [
        quote
        for quote in filtered_quotes
        if quote_has_date(quote.llm_cropped_quote, days)
    ]

    if len(filtered_llm_cropped_quotes) == 0:
        logger.info("No filtered quotes for the day!")

    if len(filtered_llm_cropped_quotes) > 0:
        temp_quote = filtered_llm_cropped_quotes[0]
        movie_title = temp_quote.quote_doc.title
        movie_data = await omdbAPIClient.get_movie_info(movie_title)
        movie = None
        if movie_data:
            movie_record = MovieRecord(movie_data.Title, movie_data.Poster, movie_data.imdbID)
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


    # TODO: Score Quote Using LLM to find the quote of day


    return {"all": all_quotes, "filtered_quotes": filtered_quotes, "filtered_llm_cropped_quotes": filtered_llm_cropped_quotes}
