from fastapi import APIRouter,Depends,status,HTTPException,Response
from product import database,schemas,models

from random import randint

from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from product.database import get_db
from fastapi import APIRouter
from fastapi import FastAPI,Form,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from product.security import get_current_user


from product.routers.email import send_passcode_email

from product.database import get_db
from typing import List
from product.security import ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM,SECRET_KEY,pwd_contex


##############33
from fastapi import BackgroundTasks,APIRouter
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from starlette.responses import JSONResponse

from product.schemas import EmailSchema
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel

######################











oauth_scheme=OAuth2PasswordBearer(tokenUrl="login")



router=APIRouter(tags=["password"])


@router.put('/changepass')
def change_password(request: schemas.ChangePass, db: Session = Depends(get_db),current_user:schemas.Seller=Depends(get_current_user)):
    product = db.query(models.Seller).filter(models.Seller.email==request.email).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    if request.newpass1 !=request.newpass2:
        raise HTTPException(status_code=404, detail='mismatch')
    if not pwd_contex.verify(request.oldpass,product.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='enter correct old password ')
    hashed_password = pwd_contex.hash(request.newpass1)
    product.password = hashed_password
    
    
    db.commit()
    db.refresh(product)
    return product

    





# @router.post("/logout")
# async def logout(authorize_token: str = Depends(oauth_scheme),db: Session = Depends(get_db)):
#         payload = jwt.decode(authorize_token, SECRET_KEY, algorithms=["HS256"])
#         username = payload["sub"]
#         product = db.query(models.Seller).filter(models.Seller.username==username).first()
#         if not product:
#             raise HTTPException(status_code=404, detail='Product not found')
        
#         user = username
#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")
    
#         user.access_token = None
#         user.access_token_expire = None
#         return {"message": "Logout successful"}
        




@router.get("/delete_cookie")
def delete_cookie(response: Response):
    response.delete_cookie(key='sessionid')
    return {"message": "Cookie deleted"}
        

def passcode():
    genrated=randint(100000,999999)
    return  genrated


#six digit passcode genarate
@router.put('/passcode-genrate')
async def add_passcode(request: schemas.GenratePasscode, db: Session = Depends(get_db)):
    user = db.query(models.Seller).filter(models.Seller.email==request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail='user not found')
    
    genrated_passcode=passcode()
    user.passcode=genrated_passcode
    
    db.commit()
    
    return {'passcode updated sucessfully'}



@router.put('/resetpassword')
def reset_password(request: schemas.ResetPassword, db: Session = Depends(get_db)):
    user = db.query(models.Seller).filter(models.Seller.email==request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail='user not found')
    if (user.passcode)!=(request.passcode):
        raise HTTPException(status_code=404, detail='Enter Correct Passcode')
    if (request.newpass1) !=(request.newpass2):
        raise HTTPException(status_code=404, detail='Password mismatch')
    
    newpassword=pwd_contex.hash(request.newpass1)
    user.password=newpassword
    db.commit()
    return {"message":"passwprd changed"}
    

    


