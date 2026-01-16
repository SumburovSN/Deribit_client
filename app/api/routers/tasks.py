from fastapi import APIRouter
from app.core.celery_app import celery_app

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/fetch-prices")
async def fetch_prices_task():
    task = celery_app.send_task(
        "app.tasks.fetch_prices.fetch_prices"
    )

    return {
        "task_id": task.id,
        "status": "queued",
    }
