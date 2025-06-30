import enum
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Enum
from apps.database import Base
from datetime import datetime
from uuid import uuid4

class TypeEnum(enum.Enum):
    SH = 'Sepatu'
    TS = 'Tas'
    TP = 'Topi'

class MaterialEnum(enum.Enum):
    KL = 'Kulit'
    SD = 'Suede'
    KV = 'Kanvas'

class StatusEnum(enum.Enum):
    CP = 'Complete'
    CL = 'Cancel'
    IP = 'In Progress'


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)  # internal PK
    order_id = Column(String(30), unique=True, nullable=False, default=lambda: "ORD-" + uuid4().hex[:8].upper())
    name = Column(String(50))
    order_date = Column(DateTime, default=datetime.now)
    amount = Column(DECIMAL(18, 2))
    qty = Column(String(50))
    type = Column(Enum(TypeEnum), nullable=False)
    material = Column(Enum(MaterialEnum), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)

