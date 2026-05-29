from sqlalchemy import Float, String, Integer, Column
from database import Base

class Product(Base):

    __tablename__= "products"

    id= Column(
        Integer,
        primary_key=True,
        index=True
    )

    name=Column(String(250))

    description=Column(String(500))

    price=Column(Float)

    stock=Column(Integer)

    category=Column(String(250))
