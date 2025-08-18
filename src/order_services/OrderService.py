
from typing import Optional
from fastapi import Depends, HTTPException, Query
from sqlalchemy import select , func
from src.models.orderModel import OrderModel
from src.schemas.orderSchema import OrderResponseSchema, OrderCreateSchema, OrderUpdateSchema , OrderResponseSchema , PaginatedOrderSchema
from src.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

async def create_order(order: OrderCreateSchema , session: AsyncSession = Depends(get_session)) -> OrderResponseSchema:
        new_order = OrderModel(**order.model_dump())
        session.add(new_order)
        await session.commit()
        await session.refresh(new_order)
        return OrderResponseSchema.model_validate(new_order)

async def get_order(
     skip: int = Query(0, ge=0),  
    limit: int = Query(10, gt=0, le=100),
     user_id: Optional[str] = None,
     product_id: Optional[str] = None,
     session: AsyncSession = Depends(get_session)) -> PaginatedOrderSchema:
    try:
        # Получаем данные
        query = select(OrderModel).offset(skip).limit(limit)
        if user_id:
            query = query.where(OrderModel.user_id == user_id)
        if product_id:
            query = query.where(OrderModel.product_id == product_id)
        
        result = await session.execute(query)
        orders = result.scalars().all()
        
        # Получаем общее количество
        count_query = select(func.count()).select_from(OrderModel)
        if user_id:
            count_query = count_query.where(OrderModel.user_id == user_id)
        if product_id:
            count_query = count_query.where(OrderModel.product_id == product_id)
        
        total = (await session.execute(count_query)).scalar_one()
        
        if not orders:
            raise HTTPException(status_code=404, detail="No orders found")
        
        return PaginatedOrderSchema(
            items=[OrderResponseSchema.model_validate(order) for order in orders],
            total=total,
            skip=skip,
            limit=limit
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def update_order(
    id: str,
    order: OrderUpdateSchema,
    session: AsyncSession = Depends(get_session),
) -> OrderResponseSchema:
    try:
        query = select(OrderModel).where(OrderModel.id == id)
        result = await session.execute(query)
        order_to_update = result.scalar_one_or_none()
        if not order_to_update:
            raise HTTPException(status_code=404, detail="Order not found")
        for key, value in order.model_dump(exclude_unset=True).items():
            setattr(order_to_update, key, value)
        await session.commit()
        await session.refresh(order_to_update)
        return OrderResponseSchema.model_validate(order_to_update)
    except Exception as e:
        print(f"Error fetching order: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

async def delete_order(
    order_id: Optional[str] = None,  
    user_id: Optional[str] = None,   
    session: AsyncSession = Depends(get_session)
):
    if order_id:
        result = await session.execute(
            select(OrderModel).where(OrderModel.id == order_id)
        )
        order = result.scalars().first()  
        
        if not order:
            raise HTTPException(
                status_code=404,
                detail=f"Order with id {order_id} not found"
            )
        
        await session.delete(order)
        await session.commit()
        return {"message": f"Order {order_id} deleted successfully"}
    
    elif user_id:
        result = await session.execute(
            select(OrderModel).where(OrderModel.user_id == user_id)
        )
        order = result.scalars().first()
        
        if not order:
            raise HTTPException(
                status_code=404,
                detail=f"No orders found for user {user_id}"
            )
        
        await session.delete(order)
        await session.commit()
        return {"message": f"Order for user {user_id} deleted successfully"}
    
    else:
        raise HTTPException(
            status_code=400,
            detail="Either order_id or user_id must be provided"
        )    
     
