from pydantic import BaseModel
from datetime import datetime

class BitcoinPrices(BaseModel):
    id : int
    currency : str
    price : float
    created_at : datetime

    class Config:
        orm_mode = True
