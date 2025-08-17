from fastapi import APIRouter, Request
from api_logic.segment_api import get_segment, segment_chart
from fastapi_cache.decorator import cache
from charts.segment_charts import plot_segment
from analysis.segment_analysis import calculate_segment
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import CASHE_EXPIRE

router = APIRouter()

@router.get("/segment")
@cache(expire=CASHE_EXPIRE)
async def segment():
    return get_segment()

@router.get("/segment_chart")
@cache(expire=CASHE_EXPIRE)
async def get_segment_chart():
    result = segment_chart()
    return result

@router.get("/segment_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Segment",
        get_df=get_df,
        compute=calculate_segment,
        chart=plot_segment,
        image_name="segment.png",
        analysis_key="segment_analysis",
        result_preview_rows=12
    )