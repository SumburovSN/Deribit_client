from pydantic import BaseModel, ConfigDict, computed_field
from decimal import Decimal
from datetime import datetime, timezone


class PriceOut(BaseModel):
    ticker: str
    price: Decimal
    timestamp: int

    @computed_field
    @property
    def datetime(self) -> datetime:
        return datetime.fromtimestamp(self.timestamp, tz=timezone.utc)

    model_config = ConfigDict(from_attributes=True)
