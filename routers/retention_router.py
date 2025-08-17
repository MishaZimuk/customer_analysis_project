from fastapi import APIRouter, Request
from api_logic.retention_api import get_retention, retention_chart
from fastapi_cache.decorator import cache
from charts.retention_charts import plot_retention
from analysis.retention_analysis import calculate_retention
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import CASHE_EXPIRE

router = APIRouter()

@router.get("/retention")
@cache(expire=CASHE_EXPIRE)
async def retention():
    return get_retention()

@router.get("/retention_chart")
@cache(expire=CASHE_EXPIRE)
async def get_retention_charts():
    result = retention_chart()
    return result

@router.get("/retention_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Retention",
        get_df=get_df,
        compute=calculate_retention,
        chart=plot_retention,
        image_name="retention.png",
        analysis_key="retention_analysis",
        result_preview_rows=12
    )