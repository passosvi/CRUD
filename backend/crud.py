from sqlalchemy.orm import Session
from schemas import ProductUpdate,ProductCreate
from models import ProductModel

#get all (select * from)
def get_products(db: Session):
    return db.query(ProductModel).all()
#get where id=1
def get_product(db: Session, product_id:int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()
#insert into (create)
def create_product(db: Session, product:ProductCreate):
    #transform my view to ORM
    db_product =ProductModel(**product.model_dump()) # that ** works to transform pydantic to ORM
    #add in table
    db.add(db_product)
    #commit in table
    db.commit()
    #refresh
    db.refresh(db_product)
    #return to user item created
    return db_product
#update where id = 1
def update_product(db:Session,product_id:int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.category is not None:
        db_product.category = product.category
    if product.email_supplier is not None:
        db_product.email_supplier = product.email_supplier
    db.commit()
    db.refresh(db_product)
    return db_product
#delete where id = 1
def delete_product(db:Session,product_id:int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(product_id)
    db.commit()
    return db_product