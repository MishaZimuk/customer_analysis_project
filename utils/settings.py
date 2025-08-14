from pydantic import BaseSettings

class Settings(BaseSettings):
    CASHE_EXPIRE: int = 300
    STATIC_DIR: str = 'static'
    IMAGES_DIR: str = 'static/images'

settings= Settings()