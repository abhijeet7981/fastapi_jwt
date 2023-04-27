from fastapi import FastAPI,Form,Depends,HTTPException,status,Response
from typing import List
from product.routers import change_pass, product,seller,login,images,email,upload
from product import models
from product.database import engine,SessionLocal,get_db

################





















app = FastAPI(
    title="Product API",
    description="Get all products",
    terms_of_service="htttp://www.google.co.in",
    contact={
    "Developer Name":"Abhijeet",
    "email":"xyz@gmail.com"
    },
    license_info={
    "name":"xyz"
    }

    # docs_url="/documentation",redoc_url=None
 
)


####################
##########################














app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)
app.include_router(change_pass.router)
app.include_router(images.router)
app.include_router(email.router)
app.include_router(upload.router)




#database create table
models.Base.metadata.create_all(engine)




