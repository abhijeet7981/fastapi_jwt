
from sqlalchemy import Column,Integer,String,ForeignKey,LargeBinary
from .database import Base
from sqlalchemy.orm import relationship



class Product(Base):
    __tablename__='products'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    decscription=Column(String)
    price=Column(Integer)
    seller_id=Column(Integer,ForeignKey('sellers.id'))
    seller=relationship("Seller",back_populates='products')



class Seller(Base):
    __tablename__='sellers'

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    passcode=Column(Integer,nullable=True)
    products=relationship("Product",back_populates="seller")


class Upload(Base):
    __tablename__='Image'

    id=Column(Integer,primary_key=True,index=True)
    image = Column(LargeBinary)

    


# class Address(Base):
#     __tablename__='address'

#     id=Column(Integer,primary_key=True,index=True)
#     address1=Column(String)
#     address1=Column(String)
#     city=Column(String)
#     state=Column(String)
#     county=Column(String)
#     postalcode=Column(Integer)
    




