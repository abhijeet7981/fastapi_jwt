
from pydantic import BaseModel,Field,HttpUrl,EmailStr
from typing import Optional,List




class Seller(BaseModel):
    username:str
    email:str
    password:str


class Displayseller(BaseModel):
    username:str
    email:str

    class Config:
        orm_mode=True

class GenratePasscode(BaseModel):
    email:str

class ResetPassword(BaseModel):
    email:str
    passcode:int
    newpass1:str
    newpass2:str
    




class Product(BaseModel):
    name:str
    decscription:str
    price:int
    seller_id:int


class DisplayProduct(BaseModel):
    name:str
    decscription:str
    seller:Displayseller

    class Config:
        orm_mode=True


#login 
class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:Optional[str]=None



class ChangePass(BaseModel):
    email:str
    oldpass:str
    newpass1:str
    newpass2:str





class EmailSchema(BaseModel):
    email: EmailStr
    
    
    




    