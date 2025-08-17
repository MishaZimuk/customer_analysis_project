from fastapi import APIRouter, Request
from api_logic.time_api.avg_order_value_by_hour_api import get_avg_order_value_by_hour, avg_order_value_by_hour_chart
from fastapi_cache.decorator import cache
from charts.time_charts.avg_order_value_by_hour_charts import plot_avg_order_value_by_hour
from analysis.time_analysis.avg_order_value_by_hour_analysis import calculate_avg_order_value_by_hour
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import CASHE_EXPIRE

router = APIRouter()

@router.get("/avg_order_value_by_hour")
@cache(expire=CASHE_EXPIRE)
async def avg_order_value_by_hour():
    return get_avg_order_value_by_hour()

@router.get("/avg_order_value_by_hour_chart")
@cache(expire=CASHE_EXPIRE)
async def get_avg_order_value_by_hour_chart():
    result = avg_order_value_by_hour_chart()
    return result

@router.get("/avg_order_value_by_hour_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Average Order Value by Hour",
        get_df=get_df,
        compute=calculate_avg_order_value_by_hour,
        chart=plot_avg_order_value_by_hour,
        image_name="avg_order_value_by_hour.png",
        analysis_key="avg_order_value_by_hour_analysis",
        result_preview_rows=12
    )