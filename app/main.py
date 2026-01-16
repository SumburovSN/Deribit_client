from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.database import engine
from app.infrastructure.db.models import Base
from app.api.routers import prices, tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Deribit Client API",
    lifespan=lifespan,
)

app.include_router(prices.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return RedirectResponse("/docs")