
from dotenv.main import load_dotenv
import os
from datetime import datetime,timedelta
from datetime import datetime,timedelta
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status,Depends
from product import schemas
from passlib.context import CryptContext



load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_LINK']


SECRET_KEY=os.environ['SECRET_KEY']
ALGORITHM=os.environ['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES=os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']




pwd_contex=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_scheme=OAuth2PasswordBearer(tokenUrl="login")


def genrateToken(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt



def get_current_user(token:str=Depends(oauth_scheme)):
    cred_exp=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                           detail='Invalid auth cred',
                           headers={'WWW-Authenticate':'Bearer'})
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        username:str=payload.get('sub')
        if username is None:
            raise cred_exp
        token_data=schemas.TokenData(username=username)
    except JWTError:
        raise cred_exp
    
'''from fastapi import FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer, HTTPException
from fastapi_microsoft_identity import MicrosoftAuthorizationCodeBearer

app = FastAPI()


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize",
    tokenUrl="https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
    scopes={"openid": "OpenID Connect", "{scope}": "{scope} scope"},
)


@app.post("/secure_post_route")
async def secure_post_route(
    request_data: dict,
    authorization: str = Header(None),
    token: str = Depends(MicrosoftAuthorizationCodeBearer(scheme=oauth2_scheme))
):
    if authorization is None or token != authorization.split(" ")[1]:
        raise HTTPException(status_code=401, detail="Invalid access token")
    # Your code logic goes here
    return {"message": "This route is secured with AAD authentication."}
'''