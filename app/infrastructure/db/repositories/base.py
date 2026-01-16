from abc import ABC, abstractmethod
from app.domain.models import Price


class PriceWriterRepository(ABC):

    @abstractmethod
    async def add(self, price: Price) -> None:
        pass


class PriceReaderRepository(ABC):

    @abstractmethod
    async def get_last_by_ticker(self, ticker: str) -> Price | None:
        pass

    @abstractmethod
    async def get_all_by_ticker(self, ticker: str, limit: int = 100) -> list[Price]:
        pass

    @abstractmethod
    async def get_by_ticker_and_period(
        self,
        ticker: str,
        from_ts: int,
        to_ts: int,
        limit: int = 100,
    ) -> list[Price]:
        pass


# from abc import ABC, abstractmethod
# from app.domain.models import Price
#
#
# class PriceRepository(ABC):
#
#     @abstractmethod
#     async def add(self, price: Price) -> None:
#         pass
#
#     @abstractmethod
#     async def get_all_by_ticker(self, ticker: str) -> list[Price]:
#         pass
#
#     @abstractmethod
#     async def get_last_by_ticker(self, ticker: str) -> Price | None:
#         pass
#
#     @abstractmethod
#     async def get_by_ticker_and_period(
#         self,
#         ticker: str,
#         from_ts: int,
#         to_ts: int,
#     ) -> list[Price]:
#         pass
