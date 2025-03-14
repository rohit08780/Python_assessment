from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    product_image = Column(String(255), nullable=True)
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(String(50), nullable=False)
    lead_time = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now())
