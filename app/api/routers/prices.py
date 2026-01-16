from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from app.api.schemas.price import PriceOut
from app.api.schemas.ticker import TickerEnum
from app.infrastructure.db.session_fastapi import get_session
from app.infrastructure.db.repositories.price_reader import PriceReaderRepositoryImpl
from app.services.price_read_service import PriceReadService

router = APIRouter(prefix="/prices", tags=["prices"])


@router.get("/latest", response_model=PriceOut)
async def get_latest_price(
    ticker: TickerEnum,
    session: AsyncSession = Depends(get_session),
):
    service = PriceReadService(PriceReaderRepositoryImpl(session))
    price = await service.get_last_price(ticker.value)

    if not price:
        raise HTTPException(status_code=404, detail="Price not found")

    return {
        "ticker": price.ticker,
        "price": price.price,
        "timestamp": price.timestamp,
        "datetime": datetime.fromtimestamp(
            price.timestamp,
            tz=timezone.utc
        ),
    }


@router.get("/history", response_model=list[PriceOut])
async def get_price_history(
    ticker: TickerEnum,
    limit: int = 100,
    session: AsyncSession = Depends(get_session),
):
    service = PriceReadService(PriceReaderRepositoryImpl(session))
    return await service.get_prices(ticker.value, limit)


@router.get("/period", response_model=list[PriceOut])
async def get_prices_by_period(
    ticker: TickerEnum,
    from_dt: datetime = Query(
        ...,
        description="Начало периода (ISO 8601)",
        examples=["2026-01-15T10:00:00Z"],
    ),
    to_dt: datetime = Query(
        ...,
        description="Конец периода (ISO 8601)",
        examples=["2026-01-15T12:00:00Z"],
    ),
    limit: int = Query(100, ge=1, le=1000),
    session: AsyncSession = Depends(get_session),
):
    if from_dt > to_dt:
        raise HTTPException(
            status_code=400,
            detail="from_dt must be less than or equal to to_dt",
        )

    # гарантируем UTC
    from_ts = int(from_dt.replace(tzinfo=timezone.utc).timestamp())
    to_ts = int(to_dt.replace(tzinfo=timezone.utc).timestamp())

    service = PriceReadService(
        PriceReaderRepositoryImpl(session)
    )

    return await service.get_prices_by_period(
        ticker=ticker.value,
        from_ts=from_ts,
        to_ts=to_ts,
        limit=limit,
    )
