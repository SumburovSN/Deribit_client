import aiohttp
from decimal import Decimal
from app.core.config import settings


class DeribitClient:
    # BASE_URL = "https://test.deribit.com/api/v2/public"
    BASE_URL = settings.deribit_base_url

    async def get_index_price(self, index_name: str) -> Decimal:
        url = f"{self.BASE_URL}/get_index_price"
        params = {"index_name": index_name}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                return Decimal(str(data["result"]["index_price"]))


# import aiohttp
# from decimal import Decimal
# from typing import Final
#
#
# class DeribitClientError(Exception):
#     """Base exception for Deribit client."""
#
#
# class DeribitClient:
#
#     # BASE_URL: Final[str] = "https://www.deribit.com/api/v2"
#     BASE_URL: Final[str] = "https://test.deribit.com/api/v2"
# # curl - X GET "https://test.deribit.com/api/v2/public/get_instruments?currency=BTC&kind=future"
#
#     def __init__(self, session: aiohttp.ClientSession | None = None):
#         self._session = session
#
#     async def get_index_price(self, ticker: str) -> Decimal:
#         index_name = ticker.lower()
#
#         url = f"{self.BASE_URL}/public/get_index_price"
#         params = {"index_name": index_name}
#
#         close_session = False
#         if self._session is None:
#             self._session = aiohttp.ClientSession()
#             close_session = True
#
#         try:
#             async with self._session.get(url, params=params) as response:
#                 if response.status != 200:
#                     raise DeribitClientError(
#                         f"Deribit API error: {response.status}"
#                     )
#
#                 data = await response.json()
#                 return Decimal(str(data["result"]["index_price"]))
#         finally:
#             if close_session:
#                 await self._session.close()
