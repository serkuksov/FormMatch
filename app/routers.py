from fastapi import APIRouter, Request, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from db import get_name_form_match
from validators import ValidateParameters

form_router = APIRouter()


@form_router.post("/get_form")
async def get_form(request: Request):
    query_params = dict(request.query_params)
    if not query_params:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Должен быть передан хотябы один параметр запроса",
        )
    type_parameters = ValidateParameters(query_params).get_type_parameters()
    db: AsyncIOMotorDatabase = request.app.mongodb
    name_form_match = await get_name_form_match(type_parameters, db)
    if name_form_match:
        return name_form_match
    else:
        return type_parameters
