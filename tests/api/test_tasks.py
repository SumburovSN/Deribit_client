import pytest
from httpx import AsyncClient
from unittest.mock import MagicMock

from app.core.celery_app import celery_app


@pytest.mark.asyncio
async def test_fetch_prices_task(client, monkeypatch):
    mock_result = MagicMock()
    mock_result.id = "test-task-id"

    def mock_send_task(name):
        assert name == "app.tasks.fetch_prices.fetch_prices"
        return mock_result

    monkeypatch.setattr(celery_app, "send_task", mock_send_task)

    response = await client.post("/tasks/fetch-prices")

    assert response.status_code == 200
    data = response.json()

    assert data["task_id"] == "test-task-id"
    assert data["status"] == "queued"
