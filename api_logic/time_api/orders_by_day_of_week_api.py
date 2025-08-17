from utils.data import get_df
from analysis.time_analysis.orders_by_day_of_week_analysis import calculate_orders_by_day_of_week
from charts.time_charts.orders_by_day_of_week_charts import plot_orders_by_day_of_week
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_orders_by_day_of_week():
    orders_by_day = calculate_orders_by_day_of_week(df).to_dict()
    return orders_by_day

def orders_by_day_of_week_chart():
    matrix = calculate_orders_by_day_of_week(df)
    plot_path = os.path.join(IMAGES_DIR, "orders_by_day_of_week.png")
    plot_orders_by_day_of_week(matrix, plot_path)
    return {"image_url":f"/images/orders_by_day_of_week.png"}