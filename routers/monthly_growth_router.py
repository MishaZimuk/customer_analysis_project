from fastapi import APIRouter, Request
from api_logic.month_over_month_growth_api import get_monthly_growth, monthly_growth_chart
from fastapi_cache.decorator import cache
from utils.settings import CASHE_EXPIRE
from charts.monthly_growth_charts import plot_monthly_growth
from analysis.monthly_growth_analysis import calculate_monthly_growth
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/monthly_growth")
@cache(expire=CASHE_EXPIRE)
async def monthly_growth():
    return get_monthly_growth()

@router.get("/monthly_growth_chart")
@cache(expire=CASHE_EXPIRE)
async def get_monthly_growth_chart():
    result = monthly_growth_chart()
    return result

@router.get("/monthly_growth_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Monthly Growth",
        get_df=get_df,
        compute=calculate_monthly_growth,
        chart=plot_monthly_growth,
        image_name="monthly_growth.png",
        analysis_key="monthly_growth_analysis",
        result_preview_rows=12
    )