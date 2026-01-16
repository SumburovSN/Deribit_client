import pytest
from unittest.mock import AsyncMock

from app.services.price_read_service import PriceReadService
from app.domain.models import Price
from tests.factories.price_factory import make_price


@pytest.mark.asyncio
async def test_get_last_price():
    repo = AsyncMock()
    repo.get_last_by_ticker.return_value = make_price()

    service = PriceReadService(repo)

    price = await service.get_last_price("btc_usd")

    assert price.ticker == "btc_usd"
    repo.get_last_by_ticker.assert_called_once_with("btc_usd")
