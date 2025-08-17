from fastapi import APIRouter, Request
from api_logic.time_api.revenue_by_hour_api import get_revenue_by_hour, revenue_by_hour_chart
from fastapi_cache.decorator import cache
from utils.settings import CASHE_EXPIRE
from charts.time_charts.revenue_by_hour_charts import plot_revenue_by_hour
from analysis.time_analysis.revenue_by_hour_analysis import calculate_revenue_by_hour
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/revenue_by_hour")
@cache(expire=CASHE_EXPIRE)
def revenue_by_hour():
    return get_revenue_by_hour()

@router.get("/revenue_by_hour_chart")
@cache(expire=CASHE_EXPIRE)
def get_revenue_by_hour_chart():
    result = revenue_by_hour_chart()
    return result

@router.get("/revenue_by_hour_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Revenue by Hour",
        get_df=get_df,
        compute=calculate_revenue_by_hour,
        chart=plot_revenue_by_hour,
        image_name="revenue_by_hour.png",
        analysis_key="revenue_by_hour_analysis",
        result_preview_rows=12
    )