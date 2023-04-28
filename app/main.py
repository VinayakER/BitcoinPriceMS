from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from .models import BitcoinPrice
from .schemas import BitcoinPrices
from .crud import get_prices, add_price
from .database import SessionLocal, engine

from sqlalchemy.orm import Session
from fastapi_utils.tasks import repeat_every
from .externalAPIs import fetchLatestBitcoinPrice


app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/bitcoin/prices",response_model=List[BitcoinPrices])
def bitcoin_prices(skip:int=0, limit: int=10,db:Session = Depends(get_db)):
    return get_prices(db,skip,limit)


@app.on_event("startup")
@repeat_every(seconds=300)
def fetch_data():
    response = fetchLatestBitcoinPrice()
    print(response.status_code==200)
    if(response.status_code==200):
        data = response.json()
        price = data['bpi']["USD"]["rate_float"]
        
        db=SessionLocal()
        reading=add_price(db,price)
        db.close()
