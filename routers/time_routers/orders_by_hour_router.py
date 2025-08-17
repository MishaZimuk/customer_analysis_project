from fastapi import APIRouter, Request
from api_logic.time_api.orders_by_hour_api import get_orders_by_hour, orders_by_hour_chart
from fastapi_cache.decorator import cache
from charts.time_charts.orders_by_hour_charts import plot_orders_by_hour
from analysis.time_analysis.orders_by_hour_analysis import calculate_orders_by_hour
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import CASHE_EXPIRE

router = APIRouter()

@router.get("/orders_by_hour")
@cache(expire=CASHE_EXPIRE)
async def orders_by_hour():
    return get_orders_by_hour()

@router.get("/orders_by_hour_chart")
@cache(expire=CASHE_EXPIRE)
async def get_orders_by_hour_chart():
    result = orders_by_hour_chart()
    return result

@router.get("/orders_by_hour_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Orders by Hour Analysis",
        get_df=get_df,
        compute=calculate_orders_by_hour,
        chart=plot_orders_by_hour,
        image_name="orders_by_hour.png",
        analysis_key="orders_by_hour_analysis",
        result_preview_rows=12
    )