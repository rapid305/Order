from pydantic import BaseModel
from typing import Optional

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