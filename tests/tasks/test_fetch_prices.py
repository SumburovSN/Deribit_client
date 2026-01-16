import pytest
from unittest.mock import AsyncMock, MagicMock

from app.tasks.fetch_prices import _fetch_prices_async


@pytest.mark.asyncio
async def test_fetch_prices_task(monkeypatch):
    # --- mock deribit client ---
    mock_client = AsyncMock()
    mock_client.get_index_price.return_value = {
        "instrument_name": "ETH_USD",
        "last_price": 3333.33,
        "timestamp": 1700000000,
    }

    monkeypatch.setattr(
        "app.tasks.fetch_prices.DeribitClient",
        lambda: mock_client
    )

    # --- mock write service ---
    mock_service = AsyncMock()

    monkeypatch.setattr(
        "app.tasks.fetch_prices.PriceWriteService",
        lambda *_: mock_service
    )

    # --- run ---
    await _fetch_prices_async()

    # --- asserts ---
    mock_client.get_index_price.assert_called()
    mock_service.save_price.assert_called()
