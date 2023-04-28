from .database import Base
from sqlalchemy import Integer, Float, String, DateTime, Column
from datetime import datetime

class BitcoinPrice(Base):
    __tablename__="bitcoin_prices"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String(50))
    price = Column(Float)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return f"Entry {id}"


