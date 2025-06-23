from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from apps.database import get_db
from apps.models.order import Order
from apps.schemas.order import OrderCreate

router = APIRouter()

@router.post("/order/create")
def create_order(order: OrderCreate, db:Session = Depends(get_db)):
    new_order = Order(
        name = order.name,
        amount = order.amount,
        qty = order.qty,
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order