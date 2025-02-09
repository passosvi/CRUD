from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductReponse, ProductUpdate, ProductCreate
from typing import List
from crud import (create_product,get_product,get_products,delete_product,update_product)

router = APIRouter() # segregacao de rota

## create route to find all
# It must has two attributes, Path and RESPONSE
@router.get("/products/", response_model= List[ProductReponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

## create route to find one item
@router.get("/products/{product_id}", response_model= ProductReponse)
def read_one_product(product_id:int, db: Session = Depends(get_db)):
    db_product = get_product(db=db,product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code= 404 , detail= "The product not exist")
## create route to add item
@router.post("/products/", response_model= ProductReponse)
def create_product(product:ProductCreate, db: Session = Depends(get_db)):
    return create_product(db = db, product = product)
## create route to delete item
@router.delete("/products/{product_id}", response_model= ProductReponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(product_id=product_id, db= db)
    if db_product is None:
        raise HTTPException(status_code= 404 , detail= "The product not exist to delete")
    return db_product
## create route to update item
@router.put("/products/{product_id}", response_model= ProductReponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
       db_product = update_product(db=db,product_id=product_id, product=product)
       if db_product is None:
            raise HTTPException(status_code= 404 , detail= "The product not exist to delete")
       return db_product