from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Price:
    ticker: str
    price: Decimal
    timestamp: int
