#UNICA FUNÇÃO É FAZER O MODELO DO DATABASE
from sqlalchemy import Column,Integer,String,Float,DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = "Products" #será o nome da tabela

    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    email_supplier = Column(String)
    created_at = Column(DateTime(timezone = True), default = func.now())