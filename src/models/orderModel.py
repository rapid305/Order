from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Integer, Boolean,  Text
import uuid

class Base(DeclarativeBase):
    pass

class OrderModel(Base):
    __tablename__ = "order"
    
    id: Mapped[str] = mapped_column(
        String(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(
        String(50), 
        nullable=False)
    product_id: Mapped[str] = mapped_column(
        String(50), 
        nullable=False)
    quantity: Mapped[int] = mapped_column(
        Integer, 
        nullable=False)
    order_date: Mapped[Optional[str]] = mapped_column(
        String(50), 
        nullable=True)
    delivery_date: Mapped[str] = mapped_column(
        String(50), 
        nullable=False)
    status: Mapped[bool] = mapped_column(
        Boolean, 
        nullable=False)
    payment_method: Mapped[Optional[str]] = mapped_column(
        String(50), 
        nullable=True)
    payment_status: Mapped[Optional[str]] = mapped_column(
        String(50), 
        nullable=True)
    shipping_address: Mapped[str] = mapped_column(
        Text, 
        nullable=False)
    tracking_number: Mapped[str] = mapped_column(
        String(50), 
        nullable=False)
    discount_applied: Mapped[Optional[int]] = mapped_column(
        Integer, 
        nullable=True)
    total_amount: Mapped[int] = mapped_column(
        Integer, 
        nullable=False)  
    tax_amount: Mapped[int] = mapped_column(
        Integer, 
        nullable=False)    
    notes: Mapped[Optional[str]] = mapped_column(
        Text, 
        nullable=True)