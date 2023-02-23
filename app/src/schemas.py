from pydantic import BaseModel, Field
from decimal import Decimal
from enum import Enum


class Exchange(Enum):
    NYSE = 'NYSE'
    NASDAQ = 'NASDAQ'


class Side(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class TVWebhookData(BaseModel):
    token: str = Field(repr=False)
    symbol: str
    exchange: Exchange
    side: Side
    last_price: Decimal
