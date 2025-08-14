from fastapi import APIRouter, Request
from api_logic.customer_lifecycle_api import get_customer_lifecycle, customer_lifecycle_chart
from fastapi_cache.decorator import cache
from utils.settings import settings
from charts.customer_lifecycle_charts import plot_customer_lifecycle
from analysis.customer_lifecycle_analysis import calculate_customer_lifecycle
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/customer_lifecycle")
@cache(expire=settings.CASHE_EXPIRE)
async def customer_lifecycle():
    return get_customer_lifecycle()

@router.get("/customer_lifecycle_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_customer_lifecycle_chart():
    result = customer_lifecycle_chart()
    return result

@router.get("/customer_lifecycle_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Customer Lifecycle",
        get_df=get_df,
        compute=calculate_customer_lifecycle,
        chart=plot_customer_lifecycle,
        image_name="customer_lifecycle.png",
        analysis_key="customer_lifecycle_analysis",
        result_preview_rows=12
    )