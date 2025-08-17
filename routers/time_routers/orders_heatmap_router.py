from fastapi import APIRouter, Request
from api_logic.time_api.orders_heatmap_api import get_orders_heatmap, orders_heatmap_chart
from fastapi_cache.decorator import cache
from charts.time_charts.orders_heatmap_charts import plot_orders_heatmap
from analysis.time_analysis.orders_heatmap_analysis import calculate_orders_heatmap
from utils.data import get_df
from utils.reports import render_simple_report
from utils.settings import CASHE_EXPIRE

router = APIRouter()

@router.get("/orders_heatmap")
@cache(expire=CASHE_EXPIRE)
def orders_heatmap():
    return get_orders_heatmap()

@router.get("/orders_heatmap_chart")
@cache(expire=CASHE_EXPIRE)
def get_orders_heatmap_chart():
    result = orders_heatmap_chart()
    return result

@router.get("/orders_heatmap_report")
async def rfm_report(request: Request):
    return render_simple_report(
        request=request,
        title="Orders Heatmap",
        get_df=get_df,
        compute=calculate_orders_heatmap,
        chart=plot_orders_heatmap,
        image_name="orders_heatmap.png",
        analysis_key="orders_heatmap_analysis",
        result_preview_rows=12
    )