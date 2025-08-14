from utils.data import get_df
from analysis.time_analysis.avg_order_value_by_hour_analysis import calculate_avg_order_value_by_hour
from charts.time_charts.avg_order_value_by_hour_charts import plot_avg_order_value_by_hour
from utils.settings import settings
import os

df = get_df()

def get_avg_order_value_by_hour():
    avg_order_value_by_hour = calculate_avg_order_value_by_hour(df).to_dict()
    return avg_order_value_by_hour

def avg_order_value_by_hour_chart():
    matrix = calculate_avg_order_value_by_hour(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "avg_order_value_by_hour.png")
    plot_avg_order_value_by_hour(matrix, plot_path)
    return {"image_url":f"{plot_path}"}