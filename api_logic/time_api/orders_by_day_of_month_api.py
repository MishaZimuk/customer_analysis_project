from analysis.time_analysis.orders_by_day_of_month_analysis import calculate_orders_by_day_of_month
from charts.time_charts.orders_by_day_of_month_charts import plot_orders_by_day_of_month
from utils.data import get_df
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_orders_by_day_of_month():
    orders_by_day_of_month = calculate_orders_by_day_of_month(df).to_dict()
    return orders_by_day_of_month

def orders_by_day_of_month_chart():
    matrix = calculate_orders_by_day_of_month(df)
    plot_path = os.path.join(IMAGES_DIR, "orders_by_day_of_month.png")
    plot_orders_by_day_of_month(matrix, plot_path)
    return {"image_url":f"/images/orders_by_day_of_month.png"}