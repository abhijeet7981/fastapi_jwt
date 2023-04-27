from fastapi import APIRouter
from fastapi import FastAPI,Form,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from product.security import get_current_user



from product import models,schemas
from product.database import get_db










router=APIRouter(
    tags=["Products"],
    prefix="/v1")





#getting Data from database
@router.get('/product/{id}')
def get_product(id: int, db: Session = Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    
    product= db.query(models.Product.name, models.Product.decscription,models.Product.price).all()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return [{"name": name, "decscription": decscription,"price":price} for name, decscription,price in product]



#display prodcut details with seller information in output
@router.get('/product/product',response_model=schemas.DisplayProduct)
def getProduct(id,response:Response,db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        if not product:
            raise HTTPException(status_code=404, detail='Product not found')
        
    return product

#return all fields
@router.get('/product')
def getProduct(db: Session = Depends(get_db)):
    product=db.query(models.Product).all()
    return product






# #adding data in database 
@router.post('/product',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Product,db:Session=Depends(get_db)):
    new_product=models.Product(name=request.name,decscription=request.decscription,price=request.price,seller_id=request.seller_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request


#Updating Data in database
@router.put('/product/{id}')
def update_product(id: int, request: schemas.Product, db: Session = Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    for key, value in request.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product





#delete data from database
@router.delete('/product/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    db.delete(product)
    db.commit()
    return {'message': f'Product {id} deleted'}







######################
from pydantic import BaseModel
from typing import Union,Set


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()

#descriptions include in swagger
@router.post("/items/", response_model=Item,summary='this explain function')
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item