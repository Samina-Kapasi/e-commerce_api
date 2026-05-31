from pydantic import BaseModel , Field
from typing import Optional

class ProductCreate(BaseModel):

    name:str

    description:str

    price:float

    stock:int

    category:str


class Update_ProductCreate(BaseModel):

    name : Optional[str]

    description : Optional[str]

    price : Optional[float]

    stock : Optional[int]

    category : Optional[str]

