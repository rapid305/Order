from pydantic import BaseModel
from typing import Optional, List

class OrderCreateSchema(BaseModel):
    user_id: str
    product_id: str
    quantity: int
    order_date: Optional[str] = None
    delivery_date: str
    status: bool
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    shipping_address: str
    tracking_number: str
    discount_applied: Optional[int] = None
    total_amount: int  
    tax_amount: int    
    notes: Optional[str] = None

class OrderResponseSchema(BaseModel):
    id: str
    user_id: str
    product_id: str
    quantity: int
    order_date: Optional[str] = None
    delivery_date: str
    status: bool
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    shipping_address: str
    tracking_number: str
    discount_applied: Optional[int] = None
    total_amount: int
    tax_amount: int
    notes: Optional[str] = None

    class Config:
        from_attributes = True

class PaginatedOrderSchema(BaseModel):
    items: List[OrderResponseSchema]
    total: int
    skip: int
    limit: int        

class OrderUpdateSchema(BaseModel):
    user_id: Optional[str] = None
    product_id: Optional[str] = None
    quantity: Optional[int] = None
    order_date: Optional[str] = None
    delivery_date: Optional[str] = None
    status: Optional[bool] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    shipping_address: Optional[str] = None
    tracking_number: Optional[str] = None
    discount_applied: Optional[int] = None
    total_amount: Optional[int] = None  
    tax_amount: Optional[int] = None    
    notes: Optional[str] = None