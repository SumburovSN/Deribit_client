# from app.domain.models import Price
# from app.infrastructure.db.repositories.base import PriceRepository
#
#
# class PriceService:
#
#     def __init__(self, repository: PriceRepository):
#         self._repository = repository
#
#     async def save_price(self, price: Price) -> None:
#         await self._repository.add(price)
#
#     async def get_prices(self, ticker: str) -> list[Price]:
#         return await self._repository.get_all_by_ticker(ticker)
#
#     async def get_last_price(self, ticker: str) -> Price | None:
#         return await self._repository.get_last_by_ticker(ticker)
#
#     async def get_prices_by_period(
#         self,
#         ticker: str,
#         from_ts: int,
#         to_ts: int,
#     ) -> list[Price]:
#         if from_ts > to_ts:
#             raise ValueError("from_ts must be less than or equal to to_ts")
#
#         return await self._repository.get_by_ticker_and_period(
#             ticker=ticker,
#             from_ts=from_ts,
#             to_ts=to_ts,
#         )
