from utils.data import get_df
from analysis.time_analysis.orders_by_month_analysis import calculate_orders_by_month
from charts.time_charts.orders_by_month_charts import plot_orders_by_month
from utils.settings import settings
import os

df = get_df()

def get_orders_by_month():
    orders_by_month = calculate_orders_by_month(df).to_dict()
    return orders_by_month

def orders_by_month_chart():
    matrix = calculate_orders_by_month(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "orders_by_month.png")
    plot_orders_by_month(matrix, plot_path)
    return {"image_url":f"{plot_path}"}