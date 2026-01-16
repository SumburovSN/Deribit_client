from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)


def create_session_maker(database_url: str) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        database_url,
        pool_pre_ping=True,
    )
    return async_sessionmaker(
        engine,
        expire_on_commit=False,
    )
