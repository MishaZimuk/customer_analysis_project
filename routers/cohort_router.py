from fastapi import APIRouter, Request
from api_logic.cohort_api import get_cohort, cohort_chart
from fastapi_cache.decorator import cache
from utils.settings import settings
from charts.cohort_charts import plot_cohort
from analysis.cohort_analysis import calculate_cohort
from utils.data import get_df
from utils.reports import render_simple_report

router = APIRouter()

@router.get("/cohort")
@cache(expire=settings.CASHE_EXPIRE)
async def cohort():
    return get_cohort()

@router.get("/cohort_chart")
@cache(expire=settings.CASHE_EXPIRE)
async def get_cohort_chart():
    result = cohort_chart()
    return result

@router.get("/cohort_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Cohort",
        get_df=get_df,
        compute=calculate_cohort,
        chart=plot_cohort,
        image_name="cohort.png",
        analysis_key="cohort_analysis",
        result_preview_rows=12
    )