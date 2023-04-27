from fastapi import APIRouter,Depends,status,HTTPException
from product import database,schemas,models
from product.schemas import Login

from sqlalchemy.orm import Session
from datetime import datetime,timedelta

from product.security import pwd_contex,SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES,genrateToken
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm















router=APIRouter()



# from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2AuthorizationCodeBearer
# from fastapi_microsoft_identity import MicrosoftAuthorizationCodeBearer

# app = FastAPI()

# oauth2_scheme = OAuth2AuthorizationCodeBearer(
#     authorizationUrl="https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize",
#     tokenUrl="https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
#     scopes={"openid": "OpenID Connect", "{scope}": "{scope} scope"},
# )

# @app.get("/secure_route")
# async def secure_route(
#     token: str = Depends(MicrosoftAuthorizationCodeBearer(scheme=oauth2_scheme))
# ):
#     return {"token": token}



@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
    user=db.query(models.Seller).filter(models.Seller.username==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='username not found/Invalid User')
    
    if not pwd_contex.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Password Invalid ')
    #Token functnality
    access_token=genrateToken(
        data={'sub':user.username}
    )
    return {"access_token":access_token,"token_type":"bearer"}


    





