from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps.database import get_db
from apps.models.order import Order, StatusEnum
from apps.schemas.order import OrderCreate, UpdateOrderStatus
from apps.core.deps import get_current_user
import sys

router = APIRouter()

#create order
@router.post("/order/create")
def create_order(order: OrderCreate, db:Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    new_order = Order(
        name = order.name,
        amount = order.amount,
        qty = order.qty,
        type = order.type,
        material = order.material,
        status = 'IP'
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

#get order by id
@router.get("/order/{order_id}")
def get_order_by_id(order_id: str, db:Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    order = db.query(Order).filter(order_id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order ID Not Found")
    
    return order

#get all data orders
@router.get("/orders")
def get_all_orders(db:Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    order = db.query(Order).all()

    return order

#update status order
@router.put("/order/{order_id}/status")
def update_order(order_id: str, new_status: UpdateOrderStatus,  db:Session = Depends(get_db), current_user: dict = Depends(get_current_user)):

    order = db.query(Order).filter(Order.order_id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order ID Not Found")
    
    order.status = new_status.status

    db.commit()
    db.refresh(order)

    return order

#delete order
@router.delete("/order/{order_id}/delete")
def delete_order(order_id: str, db:Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    order = db.query(Order).filter(Order.order_id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order ID Not Found")
    
    db.delete(order)
    db.commit()

    return {"message": f"Order {order_id} deleted successfully"}
