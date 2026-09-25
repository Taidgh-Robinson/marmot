def quote_has_date(quote: str, dates) -> bool:
    for date in dates:
        if date.lower() in quote.lower():
            return True
    return False
