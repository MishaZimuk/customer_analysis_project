from fastapi import APIRouter, Request
from api_logic.time_api.orders_by_month_api import get_orders_by_month, orders_by_month_chart
from fastapi_cache.decorator import cache
from charts.time_charts.orders_by_month_charts import plot_orders_by_month
from analysis.time_analysis.orders_by_month_analysis import calculate_orders_by_month
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import settings

router = APIRouter()

@router.get("/orders_by_month")
@cache(expire=settings.CASHE_EXPIRE)
async def orders_by_month():
    return get_orders_by_month()

@router.get("/orders_by_month_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_orders_by_momth_chart():
    result = orders_by_month_chart()
    return result

@router.get("/orders_by_month_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Orders by Month",
        get_df=get_df,
        compute=calculate_orders_by_month,
        chart=plot_orders_by_month,
        image_name="orders_by_month.png",
        analysis_key="orders_by_month_analysis",
        result_preview_rows=12
    )