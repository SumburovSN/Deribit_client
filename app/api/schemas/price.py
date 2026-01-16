from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal
from datetime import datetime


class PriceOut(BaseModel):
    ticker: str
    price: Decimal
    timestamp: int
    datetime: datetime

    model_config = ConfigDict(from_attributes=True)

#
# class PriceLatestRequest(BaseModel):
#     ticker: str = Field(..., examples=["btc_usd", "eth_usd"], description="Код валюты")
#
#
# class PriceHistoryRequest(BaseModel):
#     ticker: str = Field(..., examples=["btc_usd", "eth_usd"], description="Код валюты")
#     limit: int = Field(100, ge=1, le=1000)
