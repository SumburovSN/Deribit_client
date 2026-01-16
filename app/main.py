from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.database import engine
from app.infrastructure.db.models import Base
from app.api.router import router as prices_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Deribit Client API",
    lifespan=lifespan,
)

app.include_router(prices_router)

@app.get("/")
def root():
    return RedirectResponse("/docs")