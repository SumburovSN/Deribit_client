from celery import Celery
from celery.schedules import crontab

from app.core.config import settings


celery_app = Celery(
    "deribit_client",
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=[
        "app.tasks.fetch_prices",
    ],
)


celery_app.conf.update(
    timezone="UTC",
    enable_utc=True,
)


celery_app.conf.beat_schedule = {
    "fetch-btc-eth-prices-every-minute": {
        "task": "app.tasks.fetch_prices.fetch_prices",
        "schedule": crontab(minute="*"),
    },
}
