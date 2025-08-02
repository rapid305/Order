from fastapi import APIRouter ,Depends
from src.schemas.orderSchema import OrderResponseSchema, OrderCreateSchema
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.orderModel import OrderModel

router = APIRouter(
    prefix = "/orderInfo",
    tags =["OrderInfo"]
)



@router.post("/" ,summary="Create order", response_model=OrderResponseSchema)
async def create_order_handler(order: OrderCreateSchema , session: AsyncSession = Depends(get_session)):
        new_order = OrderModel(**order.model_dump())
        session.add(new_order)
        await session.commit()
        await session.refresh(new_order)
        return new_order


@router.get("/")
async def get_order_handler():
        return await None


@router.put("/")
async def put_order_handler():
        return await None