from fastapi import APIRouter, Request
from api_logic.churn_status_api import get_churn_status, churn_status_chart
from fastapi_cache.decorator import cache
from utils.settings import settings
from charts.churn_status_charts import plot_churn_status
from analysis.churn_status_analysis import calculate_churn_status
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/churn_status")
@cache(expire=settings.CASHE_EXPIRE)
async def churn_status():
    return get_churn_status()

@router.get("/churn_status_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_churn_status_chart():
    result = churn_status_chart()
    return result

@router.get("/churn_status_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Churn Status",
        get_df=get_df,
        compute=calculate_churn_status,
        chart=plot_churn_status,
        image_name="churn_status.png",
        analysis_key="churn_status_analysis",
        result_preview_rows=12
    )