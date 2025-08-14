from fastapi import APIRouter
from fastapi.responses import FileResponse
import os


router = APIRouter()

@router.get("/images/{image_name}")
def get_image(image_name: str):
    image_path = os.path.join("static", "images", image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    return {"error": "Image not found"}
