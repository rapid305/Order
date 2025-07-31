from fastapi import APIRouter
from src.schemas.orderSchema import OrderSchema, UpdateOrderSchema

router = APIRouter(
    prefix = "/orderInfo",
    tags =["OrderInfo"]
)



@router.post("/")
async def create_order_handler(orderPostSchema: OrderSchema):
        return await orderPostSchema


@router.get("/")
async def get_order_handler():
        return await None


@router.put("/")
async def put_order_handler():
        return await None