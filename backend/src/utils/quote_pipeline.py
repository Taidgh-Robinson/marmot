from src.utils.date_utils import get_perumtations_of_date
from src.config.logging_config import logger
from src.utils.quote_utils import quote_has_date
from src.clients.quodb_client import QuoDBClient
from src.clients.llm_client import LLMClient
from src.constants.queries import generate_crop_query

async def full_quote_pipeline(quoDBClient: QuoDBClient, day_to_fetch, llmClient: LLMClient):
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
        logger.info(f"LLM returned {crop}.")
        quote.llm_cropped_quote = crop

    filtered_llm_cropped_quotes = [
        quote
        for quote in all_quotes
        if quote_has_date(quote.llm_cropped_quote, days)
    ]

    # TODO: Score Quote Using LLM to find the quote of day


    return {"all": all_quotes, "filtered_quotes": filtered_quotes, "filtered_llm_cropped_quotes": filtered_llm_cropped_quotes}
