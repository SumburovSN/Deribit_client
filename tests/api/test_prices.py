import pytest
from decimal import Decimal

from app.domain.models import Price


@pytest.mark.asyncio
async def test_get_latest_price(client, monkeypatch):
    fake_price = Price(
        ticker="btc_usd",
        price=Decimal("50000.00"),
        timestamp=1700000000,
    )

    async def fake_get_last_price(self, ticker):
        return fake_price

    monkeypatch.setattr(
        "app.services.price_read_service.PriceReadService.get_last_price",
        fake_get_last_price,
    )

    response = await client.get(
        "/prices/latest",
        params={"ticker": "btc_usd"},
    )

    assert response.status_code == 200

    data = response.json()
    assert data["ticker"] == "btc_usd"
    assert data["price"] == "50000.00"
    assert "datetime" in data


@pytest.mark.asyncio
async def test_get_price_history(client, monkeypatch):
    prices = [
        Price("eth_usd", Decimal("3000.00"), 1700000000),
        Price("eth_usd", Decimal("3100.00"), 1700000600),
    ]

    async def fake_get_prices(self, ticker, limit):
        return prices

    monkeypatch.setattr(
        "app.services.price_read_service.PriceReadService.get_prices",
        fake_get_prices,
    )

    response = await client.get(
        "/prices/history",
        params={"ticker": "eth_usd", "limit": 2},
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 2
    assert data[0]["ticker"] == "eth_usd"
