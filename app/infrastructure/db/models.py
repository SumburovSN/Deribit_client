from datetime import datetime
from sqlalchemy import String, Integer, DateTime, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, declarative_base


Base = declarative_base()


class PriceORM(Base):
    __tablename__ = "prices"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str] = mapped_column(String(10), index=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(18, 8), nullable=False)
    timestamp: Mapped[int] = mapped_column(Integer, index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
