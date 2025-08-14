from fastapi import APIRouter, Request
from utils.data import get_df
from utils.templates import templates
from analysis.basic_overview import basic_stats

router = APIRouter()

@router.get("/", include_in_schema=False)
async def home(request: Request):
    df = get_df()
    overview = basic_stats(df)

    kpis = [
        ("Уникальных клиентов", f"{overview['unique_customers']:,}"),
        ("Всего заказов", f"{overview['total_orders']:,}"),
        ("Выручка", f"{overview['total_revenue']:,.0f}"),
        ("Средний чек", f"{overview['avg_order_value']:,.2f}"),
        ("Период", f"{overview['date_min']} – {overview['date_max']}"),
        ("SKU", f"{overview['unique_products']:,}"),
    ]

    links = [
        ("RFM", "/rfm_report"),
        ("Segment", "/segment_report"),
        ("Retention", "/retention_report"),
        ("Churn", "/churn_status_report"),
        ("New vs Returning", "/new_vs_returning_report"),
        ("Monthly Growth", "/monthly_growth_report"),
        ("LTV", "/ltv_report"),
        ("Customer Lifetime", "/customer_lifetime_report"),
        ("Lifecycle", "/customer_lifecycle_report"),
        ("First–Second Delay", "/first_second_delay_report"),
        ("Avg Days Between Orders", "/avg_days_between_orders_report"),
        ("Orders by Hour", "/orders_by_hour_report"),
        ("Revenue by Hour", "/revenue_by_hour_report"),
        ("AOV by Hour", "/avg_order_value_by_hour_report"),
        ("Orders by Weekday", "/orders_by_day_of_week_report"),
        ("Orders by Day of Month", "/orders_by_day_of_month_report"),
        ("Orders by Month", "/orders_by_month_report"),
        ("Orders Heatmap", "/orders_heatmap_report"),
    ]

    return templates.TemplateResponse(
        "home.html",
        {"request": request, "kpis": kpis, "links": links}
    )