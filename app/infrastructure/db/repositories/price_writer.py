from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Price
from app.infrastructure.db.models import PriceORM
from app.infrastructure.db.repositories.base import PriceWriterRepository


class PriceWriterRepositoryImpl(PriceWriterRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, price: Price) -> None:
        orm_obj = PriceORM(
            ticker=price.ticker,
            price=price.price,
            timestamp=price.timestamp,
        )
        self._session.add(orm_obj)
        await self._session.commit()
