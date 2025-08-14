from fastapi import APIRouter, Request
from api_logic.rfm_api import get_rfm, rfm_chart
from fastapi_cache.decorator import cache
from analysis.rfm_analysis import calculate_rfm
from charts.rfm_charts import plot_rfm
from utils.reports import render_simple_report
from utils.data import get_df
from utils.settings import settings

router = APIRouter()

@router.get("/rfm")
@cache(expire=settings.CASHE_EXPIRE)
async def rfm():
    return get_rfm()

@router.get("/rfm_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_rfm_chart():
    result = rfm_chart()
    return result

@router.get("/rfm_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="RFM",
        get_df=get_df,
        compute=calculate_rfm,
        chart=plot_rfm,
        image_name="rfm.png",
        analysis_key="rfm_analysis",
        result_preview_rows=12,
    )