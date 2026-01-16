from app.domain.models import Price
from app.infrastructure.db.repositories.base import PriceWriterRepository


class PriceWriteService:

    def __init__(self, repository: PriceWriterRepository):
        self._repository = repository

    async def save_price(self, price: Price) -> None:
        await self._repository.add(price)
