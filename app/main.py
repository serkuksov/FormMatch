from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from routers import form_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL)
    app.mongodb = app.mongodb_client.get_database(settings.MONGODB_DB)
    yield
    app.mongodb_client.close()


app = FastAPI(title="FormMatch", lifespan=lifespan)
app.include_router(form_router)


if __name__ == '__main__':
    uvicorn.run(app)
