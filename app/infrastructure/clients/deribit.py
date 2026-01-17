import aiohttp
from decimal import Decimal
from app.core.config import settings


class DeribitClient:
    BASE_URL = settings.deribit_base_url

    async def get_index_price(self, index_name: str) -> Decimal:
        url = f"{self.BASE_URL}/get_index_price"
        params = {"index_name": index_name}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                data = await response.json()
                return Decimal(str(data["result"]["index_price"]))

