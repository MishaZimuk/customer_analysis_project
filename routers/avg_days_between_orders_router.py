from fastapi import APIRouter, Request
from api_logic.avg_days_between_orders_api import get_avg_days_between_orders, avg_days_between_orders_chart
from fastapi_cache.decorator import cache
from analysis.avg_days_between_orders_analysis import calculate_avg_days_between_orders
from charts.avg_days_between_orders_charts import plot_avg_days_between_orders
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import CASHE_EXPIRE

router = APIRouter()

@router.get("/avg_days_between_orders")
@cache(expire=CASHE_EXPIRE)
async def avg_days_between_orders():
    return get_avg_days_between_orders()

@router.get("/avg_days_between_orders_chart")
@cache(expire=CASHE_EXPIRE)
async def get_avg_days_between_orders():
    result = avg_days_between_orders_chart()
    return result

@router.get("/avg_days_between_orders_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Average Days Between Orders",
        get_df=get_df,
        compute=calculate_avg_days_between_orders,
        chart=plot_avg_days_between_orders,
        image_name="avg_days_between_orders.png",
        analysis_key="avg_days_between_orders_analysis",
        result_preview_rows=12
    )