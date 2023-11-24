from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase, AsyncIOMotorClient


async def get_collection(name_collection: str, db: AsyncIOMotorDatabase) -> AsyncIOMotorCollection:
    collection = db.get_collection(name_collection)
    return collection


async def get_name_form_match(filter_form: dict[str, str], db: AsyncIOMotorDatabase) -> str | None:
    collection = await get_collection(name_collection="form_match", db=db)
    form_match = await collection.find_one(filter_form)
    if form_match:
        return form_match.get("name")
    return None
