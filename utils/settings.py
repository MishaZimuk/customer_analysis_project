from pathlib import Path


CASHE_EXPIRE: int = 300
BASE_DIR = Path(__file__).resolve().parents[1]
STATIC_DIR: str = BASE_DIR/'static'
IMAGES_DIR: str = STATIC_DIR/'images'
