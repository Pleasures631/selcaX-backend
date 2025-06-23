from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderCreate(BaseModel):
    name: str
    amount: str
    qty: str
    
    # misal mau post cuman boleh null
    # order_date: Optional[datetime] = None