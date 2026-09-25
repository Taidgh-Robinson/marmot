from src.utils.date_utils import get_perumtations_of_date
from src.config.logging_config import logger
from src.utils.quote_utils import quote_has_date


async def full_quote_pipeline(quoDBClient, day_to_fetch):
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

    # TODO: Crop quotes using LLM
    # TODO: Filter cropped quotes to those that still contain the date
    # TODO: Score Quote Using LLM to find the quote of day

    return {"all": all_quotes, "filtered_quotes": filtered_quotes}
