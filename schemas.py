from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: str
    lead_time: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: Optional[str] = None
    unit_of_measure: Optional[str] = None
    lead_time: Optional[int] = None


class ProductResponse(ProductBase):
    product_id: int
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None

    class Config:
        from_attributes = True
