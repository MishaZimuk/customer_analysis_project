from fastapi import APIRouter
from api_logic.basic_overview_api import get_basic_stats, get_monthly_stats
from fastapi_cache.decorator import cache
from utils.settings import settings

router = APIRouter()

@router.get("/basic_stats")
@cache(expire=settings.CASHE_EXPIRE)
async def basic_stats():
    return get_basic_stats()

@router.get("/monthly_stats")
@cache(expire=settings.CASHE_EXPIRE)
async def monthly_stats():
    return get_monthly_stats()
