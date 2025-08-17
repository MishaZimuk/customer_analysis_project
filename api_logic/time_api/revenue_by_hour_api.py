from utils.data import get_df
from analysis.time_analysis.revenue_by_hour_analysis import calculate_revenue_by_hour
from charts.time_charts.revenue_by_hour_charts import plot_revenue_by_hour
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_revenue_by_hour():
    revenue_by_hour = calculate_revenue_by_hour(df).to_dict()
    return revenue_by_hour

def revenue_by_hour_chart():
    matrix = calculate_revenue_by_hour(df)
    plot_path = os.path.join(IMAGES_DIR, "revenue_by_hour.png")
    plot_revenue_by_hour(matrix, plot_path)
    return {"image_url":f"/image/revenue_by_hour.png"}