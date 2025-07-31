from typing import Optional
from pydantic import BaseModel

    
class OrderSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int
    order_date: str
    delivery_date: str
    status: bool
    payment_method: str
    payment_status: str
    shipping_address: str
    tracking_number: str
    discount_applied: float
    total_amount: float
    tax_amount: float
    notes: str  

class UpdateOrderSchema(BaseModel):
    product_id: Optional[int]
    quantity: Optional[int]
    order_date: Optional[str]
    delivery_date: Optional[str]
    status: bool
    payment_method: Optional[str]
    payment_status: Optional[str]
    shipping_address: Optional[str]
    tracking_number: Optional[str]
    discount_applied: Optional[float]
    total_amount: Optional[float]
    tax_amount: Optional[float]
    notes: Optional[str]      