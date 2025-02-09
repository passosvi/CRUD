#FUNÇAO DE VIEW, CADA OPERAÇAO TEM UM PADRAO DISTINTO QUE PRECISA SER VALIDADO
from pydantic import BaseModel,PositiveFloat,EmailStr,validator
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name : str
    description : str
    price : PositiveFloat
    category : str
    email_supplier : EmailStr

class ProductCreate(ProductBase):
    pass


class ProductReponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_supplier: Optional[EmailStr] = None
    