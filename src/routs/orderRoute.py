from typing import Optional
from fastapi import APIRouter ,Depends, HTTPException
from src.schemas.orderSchema import OrderResponseSchema, OrderCreateSchema, OrderUpdateSchema , PaginatedOrderSchema
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.orderModel import OrderModel
from sqlalchemy.future import select
from src.order_services.OrderService import create_order , get_order , update_order, delete_order

router = APIRouter(
    prefix = "/orderInfo",
    tags =["OrderInfo"]
)



@router.post("/" ,summary="Create order", response_model=OrderResponseSchema)
async def create_order_handler(order: OrderCreateSchema , session: AsyncSession = Depends(get_session)):
        return await create_order(order , session)


@router.get("/", summary = "Get order" ,response_model=PaginatedOrderSchema)
async def get_order_handler(
     skip: int = 0,
     limit: int = 10,
     user_id: Optional[str] = None,
     product_id: Optional[str] = None,
     session: AsyncSession = Depends(get_session)):
    return await get_order(skip=skip,
    limit=limit,
    user_id=user_id,
    product_id=product_id,
    session=session)


@router.put("/" , summary= "Change order by id" , response_model= OrderUpdateSchema)
async def put_order_handler(
    id: str,
    order: OrderUpdateSchema,
    session: AsyncSession = Depends(get_session),
) -> OrderResponseSchema:
    return await update_order(session = session, id = id , order = order)

@router.delete("/{order_id}" , summary= "Delete order")
async def delete_order_handler(
    order_id: Optional[str] = None,  
    user_id: Optional[str] = None,   
    session: AsyncSession = Depends(get_session)
):
    return await delete_order(session = session , order_id = order_id , user_id = user_id)

