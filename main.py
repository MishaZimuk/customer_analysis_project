from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import (basic_router, ltv_router, monthly_growth_router, retention_router, rfm_router, repeat_rate_router,
                     first_second_delay_router, churn_status_router, cohort_router, customer_lifetime_router,
                     new_vs_returning_router, segment_router, home_router,
                     avg_days_between_orders_router, customer_lifecycle_router, static_router, health_router)
from routers.time_routers import (orders_by_day_of_week_router, orders_by_day_of_month_router, orders_by_month_router,
                                  orders_by_hour_router, orders_heatmap_router, revenue_by_hour_router,
                                  avg_order_value_by_hour_router)
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.requests import Request
from utils.settings import STATIC_DIR, IMAGES_DIR


app = FastAPI()

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name=STATIC_DIR)

@app.exception_handler(Exception)
async def unhandled(request: Request, exc: Exception):
    return JSONResponse({"error":"Internal error"}, status_code=500)

app.include_router(home_router.router)
app.include_router(basic_router.router)
app.include_router(rfm_router.router)
app.include_router(ltv_router.router)
app.include_router(retention_router.router)
app.include_router(orders_by_day_of_week_router.router)
app.include_router(orders_by_day_of_month_router.router)
app.include_router(orders_by_month_router.router)
app.include_router(orders_by_hour_router.router)
app.include_router(revenue_by_hour_router.router)
app.include_router(orders_heatmap_router.router)
app.include_router(avg_order_value_by_hour_router.router)
app.include_router(avg_days_between_orders_router.router)
app.include_router(repeat_rate_router.router)
app.include_router(churn_status_router.router)
app.include_router(cohort_router.router)
app.include_router(new_vs_returning_router.router)
app.include_router(customer_lifetime_router.router)
app.include_router(segment_router.router)
app.include_router(monthly_growth_router.router)
app.include_router(first_second_delay_router.router)
app.include_router(customer_lifecycle_router.router)
app.include_router(static_router.router)
app.include_router(health_router.router)
app.mount("/images", StaticFiles(directory=IMAGES_DIR), name="images")