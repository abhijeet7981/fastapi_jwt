

from fastapi import APIRouter, File, UploadFile
from typing_extensions import Annotated





router = APIRouter(tags=["test_upload"])

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
