from fastapi import APIRouter, Request
from api_logic.customer_lifetime_api import get_customer_lifetime, customer_lifetime_chart
from fastapi_cache.decorator import cache
from utils.settings import settings
from charts.customer_lifeteime_charts import plot_customer_lifetime
from analysis.customer_lifetime_analysis import calculate_customer_lifetime
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/customer_lifetime")
@cache(expire=settings.CASHE_EXPIRE)
async def customer_lifetime():
    return get_customer_lifetime()

@router.get("/customer_lifetime_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_customer_lifetime_chart():
    result = customer_lifetime_chart()
    return result

@router.get("/customer_lifetime_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Customer Lifetime",
        get_df=get_df,
        compute=calculate_customer_lifetime,
        chart=plot_customer_lifetime,
        image_name="customer_lifetime.png",
        analysis_key="customer_lifetime_analysis",
        result_preview_rows=12
    )