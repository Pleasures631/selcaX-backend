from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from apps.models.order import TypeEnum, MaterialEnum, StatusEnum

class OrderCreate(BaseModel):
    order_id: str
    item_name: str
    amount: str
    qty: str
    status: StatusEnum
    notes: str
    cust_name: str
    cust_address: str

class UpdateOrderStatus(BaseModel):
    status: StatusEnum

    # misal mau post cuman boleh null
    # order_date: Optional[datetime] = None