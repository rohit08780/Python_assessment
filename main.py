from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, Product
from schemas import ProductCreate, ProductUpdate, ProductResponse
from typing import List


app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)

@app.get("/api/product/list", response_model=List[ProductResponse])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    products = db.query(Product).offset(offset).limit(limit).all()
    return products


@app.get("/api/product/{pid}/info", response_model=ProductResponse)
def get_product_info(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == pid).first()
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product with ID {pid} not found")
    return product


@app.post("/api/product/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.put("/api/product/{pid}/update", response_model=ProductResponse)
def update_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.product_id == pid).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail=f"Product with ID {pid} not found")

    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(existing_product, key, value)

    db.commit()
    db.refresh(existing_product)
    return existing_product
