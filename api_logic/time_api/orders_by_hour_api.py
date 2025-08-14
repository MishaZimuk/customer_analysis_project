from utils.data import get_df
from analysis.time_analysis.orders_by_hour_analysis import calculate_orders_by_hour
from charts.time_charts.orders_by_hour_charts import plot_orders_by_hour
from utils.settings import settings
import os

df = get_df()

def get_orders_by_hour():
    orders_by_hour = calculate_orders_by_hour(df).to_dict()
    return orders_by_hour

def orders_by_hour_chart():
    matrix = calculate_orders_by_hour(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "orders_by_hour.png")
    plot_orders_by_hour(matrix, plot_path)
    return {"image_url":f"{plot_path}"}