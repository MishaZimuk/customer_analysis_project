from fastapi import APIRouter, Request
from api_logic.first_second_delay_api import get_first_second_delay, first_second_delay_chart
from fastapi_cache.decorator import cache
from utils.settings import settings
from charts.firsr_sedond_delay_charts import plot_first_second_delay
from analysis.first_second_delay_analysis import calculate_first_second_delay
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/firs_second_delay")
@cache(expire=settings.CASHE_EXPIRE)
async def first_second_delay():
    return get_first_second_delay()

@router.get("/first_second_delay_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_first_second_delay_hist():
    result = first_second_delay_chart()
    return result

@router.get("/first_second_delay_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="First Second Delay",
        get_df=get_df,
        compute=calculate_first_second_delay,
        chart=plot_first_second_delay,
        image_name="first_second_delay.png",
        analysis_key="first_second_delay_analysis",
        result_preview_rows=12
    )