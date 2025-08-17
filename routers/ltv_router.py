from fastapi import APIRouter, Request
from api_logic.ltv_api import get_ltv, ltv_chart
from fastapi_cache.decorator import cache
from utils.settings import CASHE_EXPIRE
from charts.ltv_charts import plot_ltv
from analysis.ltv_analysis import calculate_ltv
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/ltv")
@cache(expire=CASHE_EXPIRE)
async def ltv():
    return get_ltv()

@router.get("/ltv_chart")
@cache(expire=CASHE_EXPIRE)
async def get_ltv_charts():
    result = ltv_chart()
    return result

@router.get("/ltv_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="LTV",
        get_df=get_df,
        compute=calculate_ltv,
        chart=plot_ltv,
        image_name="ltv.png",
        analysis_key="ltv_analysis",
        result_preview_rows=12
    )