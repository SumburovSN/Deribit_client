from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Price
from app.infrastructure.db.models import PriceORM
from app.infrastructure.db.repositories.base import PriceReaderRepository


class PriceReaderRepositoryImpl(PriceReaderRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_by_ticker(self, ticker: str, limit: int = 100) -> list[Price]:
        stmt = select(PriceORM).where(PriceORM.ticker == ticker).limit(limit)
        result = await self._session.execute(stmt)
        return [self._to_domain(row[0]) for row in result.all()]

    async def get_last_by_ticker(self, ticker: str) -> Price | None:
        stmt = (
            select(PriceORM)
            .where(PriceORM.ticker == ticker)
            .order_by(desc(PriceORM.timestamp))
            .limit(1)
        )
        result = await self._session.execute(stmt)
        row = result.scalar_one_or_none()
        return self._to_domain(row) if row else None

    async def get_by_ticker_and_period(
        self,
        ticker: str,
        from_ts: int,
        to_ts: int,
        limit: int = 100,
    ) -> list[Price]:
        stmt = (
            select(PriceORM)
            .where(
                PriceORM.ticker == ticker,
                PriceORM.timestamp >= from_ts,
                PriceORM.timestamp <= to_ts,
            )
            .order_by(PriceORM.timestamp)
            .limit(limit)
        )
        result = await self._session.execute(stmt)
        return [self._to_domain(row[0]) for row in result.all()]

    @staticmethod
    def _to_domain(orm: PriceORM) -> Price:
        return Price(
            ticker=orm.ticker,
            price=orm.price,
            timestamp=orm.timestamp,
        )
