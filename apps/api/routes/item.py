from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Union
from apps.database import get_db
from apps.models.product import Product
from apps.schemas.products import ProductCreate

router = APIRouter()

@router.post("/items/create")
def create_product(product: ProductCreate, db:Session = Depends(get_db)):
    new_product = Product(
        name = product.name,
        price = product.price   ,
        qty = product.qty,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/items")
def get_all_items(db:Session = Depends(get_db)):
    product = db.query(Product).all()

    return product