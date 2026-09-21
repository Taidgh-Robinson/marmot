from fastapi import APIRouter, Response, Query

router = APIRouter()

#TODO
@router.get('/quote_of_the_day')
def get_quote_of_the_day():
    return Response(content="", media_type="application/json")

#TODO
@router.get('/get_quote')
def get_quote(date: str = Query(..., regex=r"^\d{4}/\d{2}/\d{2}$")):
    return Response(content=f"{date}", media_type="application/json")