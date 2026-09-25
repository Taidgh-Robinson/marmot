from fastapi import APIRouter, Response, Query, Depends
from src.api.core.depdencies import get_quodb_client
from src.utils.quote_pipeline import full_quote_pipeline
from src.utils.date_utils import get_todays_date
router = APIRouter()

#TODO
@router.get('/quote_of_the_day')
async def get_quote_of_the_day(quodb_client=Depends(get_quodb_client)):
    quotes = await full_quote_pipeline(quodb_client, get_todays_date())
    fake_data = quotes['filtered_quotes'][0]

    return Response(content=f"{fake_data.display_full_quote()}", media_type="application/json")

#TODO
@router.get('/get_quote')
async def get_quote(quodb_client=Depends(get_quodb_client), date: str = Query(..., regex=r"^\d{2}/\d{2}/\d{4}$")):
    quotes = await full_quote_pipeline(quodb_client, date)
    fake_data = quotes['filtered_quotes'][0]

    return Response(content=f"{fake_data.display_full_quote()}", media_type="application/json")