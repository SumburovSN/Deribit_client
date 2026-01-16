from app.core.config import settings
from app.infrastructure.db.session import create_session_maker

SessionMaker = create_session_maker(settings.database_url)

async def get_session():
    async with SessionMaker() as session:
        yield session
