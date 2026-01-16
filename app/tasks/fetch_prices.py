import asyncio
import time
from decimal import Decimal
from app.core.celery_app import celery_app
from app.core.config import settings
from app.domain.models import Price
from app.infrastructure.clients.deribit import DeribitClient
from app.infrastructure.db.repositories.price_writer import PriceWriterRepositoryImpl
from app.services.price_write_service import PriceWriteService
from app.infrastructure.db.session import create_session_maker


@celery_app.task(name="app.tasks.fetch_prices.fetch_prices")
def fetch_prices() -> None:
    """
    Periodic task that fetches BTC and ETH index prices
    from Deribit and saves them to the database.
    """
    print("Fetching prices...")
    asyncio.run(_fetch_prices_async())


async def _fetch_prices_async():
    session_maker = create_session_maker(settings.database_url)

    async with session_maker() as session:
        repository = PriceWriterRepositoryImpl(session)
        service = PriceWriteService(repository)
        client = DeribitClient()

        timestamp = int(time.time())

        for ticker in ("btc_usd", "eth_usd"):
            price: Decimal = await client.get_index_price(ticker)

            await service.save_price(
                Price(
                    ticker=ticker,
                    price=price,
                    timestamp=timestamp,
                )
            )
