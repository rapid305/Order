
from fastapi import APIRouter
from src.routs.orderRoute import router


api_router = APIRouter(
    prefix = ("/api")
)

api_router.include_router(router)