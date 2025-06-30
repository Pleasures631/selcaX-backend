from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from apps.models.order import TypeEnum, MaterialEnum, StatusEnum

class OrderCreate(BaseModel):
    name: str
    amount: str
    qty: str
    type: TypeEnum
    material: MaterialEnum

class UpdateOrderStatus(BaseModel):
    status: StatusEnum

    # misal mau post cuman boleh null
    # order_date: Optional[datetime] = None