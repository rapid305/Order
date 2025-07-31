from typing import List
from sqlalchemy.orm import Mapped , mapped_column
from sqlalchemy import ForeignKey, Integer, String, func


class StoreModel():
    __tablename__ = "order"

    __table_args__ = {
        "comment": "Таблица для учёта заказов"
    }

    id: Mapped[int] = mapped_column(
        String(36) ,
        primary_key=True , 
        server_default=func.uuid),
    user_id: Mapped[int] = mapped_column(
        String (36) , 
        nullable= False , 
        unique= True),
    product_id: Mapped[int] = mapped_column(
        String(36) , 
        nullable= False)
    quantity: Mapped[int] = mapped_column(
        String(36) , 
        nullable= False)
    order_date: Mapped[str] = mapped_column (
        String(36) , 
        nullable= True)
    delivery_date: Mapped[str] = mapped_column(
        String(36) , 
        nullable= False)
    status: Mapped[str] = mapped_column(
        String(36) , 
        nullable= False)
    payment_method: Mapped[str] = mapped_column(
        String(36) , 
        nullable= True)
    payment_status: Mapped[str] = mapped_column(
        String(36) , 
        nullable= True)
    shipping_address: Mapped[str] = mapped_column(
        String(36) ,
         nullable= False)    
    tracking_number: Mapped[str] = mapped_column(
        String(36) , 
        nullable= False)
    discount_applied: Mapped[str] = mapped_column(
        String(36) , 
        nullable= True)
    total_amount: Mapped[float] = mapped_column(
        String(36) , 
        nullable= False)
    tax_amount: Mapped[float] = mapped_column(
        String(36) , 
        nullable= False)
    notes: Mapped[str] = mapped_column(
        String(36) , 
        nullable= False)
