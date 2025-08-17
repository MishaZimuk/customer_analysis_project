from fastapi import APIRouter, Request
from api_logic.new_with_returning_api import get_new_vs_returning, new_vs_returning_chart
from fastapi_cache.decorator import cache
from utils.settings import CASHE_EXPIRE
from charts.new_vs_returning_charts import plot_new_vs_returning
from analysis.new_vs_returning_analysis import calculate_new_vs_returning
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/new_vs_returning")
@cache(expire=CASHE_EXPIRE)
async def new_vs_returning():
    return get_new_vs_returning()

@router.get("/new_vs_returning_chart")
@cache(expire=CASHE_EXPIRE)
async def get_new_vs_returning_chart():
    result = new_vs_returning_chart()
    return result

@router.get("/new_vs_returning_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="New vs Returning",
        get_df=get_df,
        compute=calculate_new_vs_returning,
        chart=plot_new_vs_returning,
        image_name="new_vs_returning.png",
        analysis_key="new_vs_returning_analysis",
        result_preview_rows=12
    )