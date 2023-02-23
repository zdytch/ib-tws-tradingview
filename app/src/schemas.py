from pydantic import BaseModel, Field
from decimal import Decimal
from enum import Enum


class Exchange(Enum):
    NYSE = 'NYSE'
    NASDAQ = 'NASDAQ'


class Side(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class OrderType(Enum):
    LIMIT = 'LMT'
    STOP = 'STP'
    MARKET = 'MKT'


class TVWebhookData(BaseModel):
    token: str = Field(repr=False)
    symbol: str
    exchange: Exchange
    side: Side
    close: Decimal


class StockData(BaseModel):
    symbol: str
    exchange: Exchange


class OrderData(BaseModel):
    stock: StockData
    side: Side
    type: OrderType
    size: int
    price: Decimal = Decimal('0.0')
