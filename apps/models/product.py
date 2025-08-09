import enum
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Enum
from apps.database import Base
from datetime import datetime
from uuid import uuid4

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)  # internal PK
    name = Column(String(50))
    price = Column(DECIMAL(18, 2))
    qty = Column(String(50))
    created_date = Column(DateTime, default=datetime.now)
