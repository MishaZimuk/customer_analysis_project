from fastapi import APIRouter, Request
from api_logic.repeat_rate_api import get_repeat_rate, repeat_rate_chart
from fastapi_cache.decorator import cache
from utils.settings import CASHE_EXPIRE
from charts.repeat_rate_charts import plot_repeat_rate
from analysis.repeat_rate_analysis import calculate_repeat_rate
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/repeat_rate")
@cache(expire=CASHE_EXPIRE)
async def repeat_rate():
    return get_repeat_rate()

@router.get("/repeat_rate_chart")
@cache(expire=CASHE_EXPIRE)
async def get_repeat_rate_piechart():
    result = repeat_rate_chart()
    return result

@router.get("/repeat_rate_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Repeat Rate",
        get_df=get_df,
        compute=calculate_repeat_rate,
        chart=plot_repeat_rate,
        image_name="repeat_rate.png",
        analysis_key="repeat_rate_analysis",
        result_preview_rows=12
    )