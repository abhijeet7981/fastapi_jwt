from fastapi import APIRouter
from fastapi import Depends,HTTPException,status,Response
from sqlalchemy.orm import Session



from product import models,schemas
from product.database import get_db

from product.security import pwd_contex



router=APIRouter()

@router.post('/seller',response_model=schemas.Displayseller,tags=['Seller'])
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_pass=pwd_contex.hash(request.password)
    new_seller=models.Seller(username=request.username,password=hashed_pass,email=request.email)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller

@router.delete('/seller/{id}')
def delete_seller(id: int, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.id == id).first()
    if not seller:
        raise HTTPException(status_code=404, detail='seller not found')
    db.delete(seller)
    db.commit()
    return {'message': f'seller {id} deleted'}


@router.get('/getseller')
def getProduct(email,response:Response,db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.email == email).first()

    if not seller:
        if not seller:
            raise HTTPException(status_code=404, detail='Product not found')
        
    return seller