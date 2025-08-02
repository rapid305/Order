from typing import Optional
from fastapi import APIRouter ,Depends, HTTPException
from src.schemas.orderSchema import OrderResponseSchema, OrderCreateSchema
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.orderModel import OrderModel
from sqlalchemy.future import select

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


@router.get("/", response_model=list[OrderResponseSchema])
async def get_order_handler(
     skip: int = 0,
     limit: int = 10,
     user_id: Optional[str] = None,
     product_id: Optional[str] = None,
     session: AsyncSession = Depends(get_session)):
    try:

        query = select(OrderModel).offset(skip).limit(limit)
        if user_id:
            query = query.where(OrderModel.user_id == user_id)
        if product_id:    
            query = query.where(OrderModel.product_id == product_id)
        result = await session.execute(query)
        orders = result.scalars().all()
        
        if not orders:
            raise HTTPException(status_code=404, detail="Orders not found")
        
        return orders  
        
    except Exception as e:
        print(f"Error fetching orders: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/")
async def put_order_handler():
        return await None