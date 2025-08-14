from utils.data import get_df
from analysis.avg_days_between_orders_analysis import calculate_avg_days_between_orders
from charts.avg_days_between_orders_charts import plot_avg_days_between_orders
from utils.settings import settings
import os

df = get_df()

def get_avg_days_between_orders():
    avg_days_between_orders = calculate_avg_days_between_orders(df)
    return avg_days_between_orders

def avg_days_between_orders_chart():
    matrix = calculate_avg_days_between_orders(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "avg_days_between_orders.png")
    plot_avg_days_between_orders(matrix, plot_path)
    return {"image_url":f"{plot_path}"}