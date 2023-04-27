from fastapi import BackgroundTasks,APIRouter,Depends,HTTPException
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from product.database import get_db
from product.schemas import EmailSchema
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from product import models,schemas
from dotenv.main import load_dotenv
import os


load_dotenv()



router=APIRouter()


conf = ConnectionConfig(
    MAIL_USERNAME =os.environ['MAIL_USERNAME'],
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD'],
    MAIL_FROM = os.environ['MAIL_USERNAME'],
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)









def generate_passcode_email(passcode: str, recipient_email: str):
    subject = "Password reset passcode"
    body = f"Your password reset passcode is: <strong><h1>{passcode}</h1></strong>"
    recipients = [recipient_email]
    return MessageSchema(subject=subject, body=body, recipients=recipients, subtype=MessageType.html)

@router.post("/email")
async def send_passcode_email(email: str, db: Session = Depends(get_db)) -> JSONResponse:
    seller = db.query(models.Seller).filter(models.Seller.email == email).first()
    if not seller:
        raise HTTPException(status_code=404, detail="Seller not found")

    message = generate_passcode_email(seller.passcode, email)

    try:
        fm = FastMail(conf)
        await fm.send_message(message)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send email. Please try again later.")

    return JSONResponse(status_code=200, content={"message": "An email has been sent with a passcode to reset your account."})








# html =f'<p>your passcode for the reste password is {passcode}</p>.'.format(genrated_passcode)

#     async def simple_send(email:user.email) -> JSONResponse:

#         message = MessageSchema(
#             subject="Fastapi-Mail module",
#             recipients=email.dict().get("email"),
#             body=html,
#             subtype=MessageType.html)

#         fm = FastMail(conf)
#         await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})





#@router.post("/email")
# async def simple_send(email:str,db: Session = Depends(get_db)) -> JSONResponse:
#     seller = db.query(models.Seller).filter(models.Seller.email == email).first()

#     message = MessageSchema(
#         subject="Tesing Mail-Passcode",
#         recipients=[email],
#         body='this is test data: ' + str(seller.passcode),
        
#         subtype=MessageType.html
#         )

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent with passcode to reset your account"})   