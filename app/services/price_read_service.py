from app.domain.models import Price
from app.infrastructure.db.repositories.base import PriceReaderRepository


class PriceReadService:

    def __init__(self, repository: PriceReaderRepository):
        self._repository = repository

    async def get_last_price(self, ticker: str) -> Price | None:
        return await self._repository.get_last_by_ticker(ticker)

    async def get_prices(self, ticker: str, limit) -> list[Price]:
        return await self._repository.get_all_by_ticker(ticker, limit)

    async def get_prices_by_period(
        self,
        ticker: str,
        from_ts: int,
        to_ts: int,
        limit: int = 100,
    ) -> list[Price]:
        if from_ts > to_ts:
            raise ValueError("from_ts must be <= to_ts")

        return await self._repository.get_by_ticker_and_period(
            ticker=ticker,
            from_ts=from_ts,
            to_ts=to_ts,
            limit=limit,
        )
