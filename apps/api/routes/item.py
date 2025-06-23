from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

router = APIRouter()

class requestBody(BaseModel): 
    name: str
    price: float
    is_offer: Union[bool, None] = None


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
def update_item(item_id: int, item: requestBody):
    return {"item_id": item_id, "item name:": item.name, "item price:": item.price}