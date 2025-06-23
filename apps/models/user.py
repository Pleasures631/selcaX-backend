from sqlalchemy import Column, Integer, String, DateTime, DECIMAL
from apps.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=True)
    password_hash = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
