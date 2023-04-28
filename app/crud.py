from .schemas import BitcoinPrices
from sqlalchemy.orm import Session
from .models import BitcoinPrice

def get_prices(db: Session, skip:int=0, limit:int=10):
    return db.query(BitcoinPrice).offset(skip).limit(limit).all()

def add_price(db:Session, price:float):
    reading = BitcoinPrice(currency="USD",price=price)
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading