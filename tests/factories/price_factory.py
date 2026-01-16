from decimal import Decimal
from app.domain.models import Price


def make_price(
    ticker: str = "btc_usd",
    price: Decimal = Decimal("50000.00"),
    timestamp: int = 1700000000,
) -> Price:
    return Price(
        ticker=ticker,
        price=price,
        timestamp=timestamp,
    )
