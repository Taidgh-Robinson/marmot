#Temp file so I can still use main to test logic, will be moved up to main later
from fastapi import FastAPI
from src.api.routers.quote_router import router as quote_router 


app = FastAPI()

app.include_router(quote_router)