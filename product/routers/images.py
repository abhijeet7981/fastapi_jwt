from fastapi import APIRouter,File,UploadFile
from fastapi import Depends,status,Response
from sqlalchemy.orm import Session




from product import models,schemas
from product.database import get_db
from typing import List





router=APIRouter(
    tags=["Image Upload"],
    prefix="/v1")




#upload Image
@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    upload = models.Upload(image=contents)
    db.add(upload)
    db.commit()
    db.refresh(upload)
    return {"id": upload.id, "name": file.filename, "size": len(contents)}





# endpoint for retrieving a list of all uploaded images
@router.get("/images/{image_id}/")
async def get_image(image_id: int, db: Session = Depends(get_db)):
    image = db.query(models.Upload).filter(models.Upload.id == image_id).first()
    if not image:
        return Response(status_code=404)
    return Response(content=image.image, media_type="image/jpeg")