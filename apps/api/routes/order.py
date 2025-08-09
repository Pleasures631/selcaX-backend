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
def create_order(order: OrderCreate, db:Session = Depends(get_db)):
    new_order = Order(
        order_id = order.order_id,
        item_name = order.item_name,
        amount = order.amount,
        qty = order.qty,
        cust_name = order.cust_name,
        cust_address = order.cust_address,
        notes = order.notes,
        # type = order.type,
        # material = order.material,
        status = order.status
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
def get_distinct_order_ids(db: Session = Depends(get_db)):
    result = db.query(Order.order_id, Order.cust_name, Order.cust_address).distinct().all()
    print("RAW RESULT:", result)  # Debug: lihat isi hasil query

    order_ids = [{"label": f"{row[0]} - {row[1]}", "value": row[0], "cust_name": row[1], "cust_address": row[2]} for row in result]
    print("FORMATTED:", order_ids)  # Debug: lihat hasil akhir yang dikembalikan

    return order_ids

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

@router.post("/order/split")
def create_order_split(order: OrderCreate, db:Session = Depends(get_db)):
    new_order_split = Order(
        order_id = order.order_id,
        item_name = order.item_name,
        amount = order.amount,
        qty = order.qty,
        cust_name = order.cust_name,
        cust_address = order.cust_address,
        notes = order.notes,
        status = order.status
    )
    db.add(new_order_split)
    db.commit()
    db.refresh(new_order_split)
