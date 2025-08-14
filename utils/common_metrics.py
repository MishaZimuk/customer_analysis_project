METRICS = {
    "basic_overview": [
        "Total unique customers",
        "Total orders",
        "Total revenue",
        "Average order value",
        "Date range",
        "Countries / Regions",
        "Unique products (SKUs)",
    ],
    "rfm_analysis": [
        "CustomerID", "Recency", "Frequency", "Monetary",
        "R_score", "F_score", "M_score", "RFM_score"
    ],
    "segment_analysis": [
        "Segment",
        "Customer count",
        "Total revenue",
        "Average order value",
        "Revenue share %",
    ],
    "retention_analysis": [
        "Cohort Month",
        "Cohort size",
        "Month index (since first order)",
        "Retained customers",
        "Retention rate %",
    ],
    "churn_status_analysis": [
        "Status (Active / Churned)",
        "Customers",
        "Share %",
        "Days since last order (threshold)",
    ],
    "customer_lifecycle_analysis": [
        "CustomerID",
        "Days since last order",
        "Lifecycle stage (Active / At Risk / Inactive)",
        "Last order date",
    ],
    "customer_lifetime_analysis": [
        "CustomerID",
        "First order date",
        "Last order date",
        "Lifetime days",
        "Orders",
        "Revenue",
    ],
    "ltv_analysis": [
        "CustomerID",
        "Orders",
        "Revenue",
        "Lifetime days",
        "LTV",
    ],
    "repeat_rate_analysis": [
        "Total customers",
        "Repeat customers",
        "One-time customers",
        "Repeat rate %",
    ],
    "first_second_delay_analysis": [
        "CustomerID",
        "Days between first and second order",
    ],
    "avg_days_between_orders_analysis": [
        "CustomerID",
        "Average days between orders",
        "Global average (all customers)",
        "Global median (all customers)",
    ],
    "cohort_analysis": [
        "Cohort Month",
        "Cohort size",
        "Month index",
        "Retained customers",
        "Retention rate %",
    ],
    "new_vs_returning_analysis": [
        "Month",
        "New customers",
        "Returning customers",
        "Returning share %",
    ],
    "monthly_growth_analysis": [
        "Month",
        "Orders",
        "MoM growth %",
    ],
    "time_analysis/orders_by_hour_analysis": [
        "Hour of day",
        "Orders",
    ],
    "time_analysis/revenue_by_hour_analysis": [
        "Hour of day",
        "Revenue",
    ],
    "time_analysis/avg_order_value_by_hour_analysis": [
        "Hour of day",
        "Average order value",
        "Orders (optional)"
    ],
    "time_analysis/orders_by_day_of_week_analysis": [
        "Weekday",
        "Orders",
    ],
    "time_analysis/orders_by_day_of_month_analysis": [
        "Day of month (1–31)",
        "Orders",
    ],
    "time_analysis/orders_by_month_analysis": [
        "Month",
        "Orders",
    ],
    "time_analysis/orders_heatmap_analysis": [
        "Weekday",
        "Hour of day",
        "Orders (matrix)",
    ],
}

def get_metrics(key: str): return METRICS.get(key, [])