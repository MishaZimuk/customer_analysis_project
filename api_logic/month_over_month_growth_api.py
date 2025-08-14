from utils.data import get_df
from analysis.monthly_growth_analysis import calculate_monthly_growth
from charts.monthly_growth_charts import plot_monthly_growth
from utils.settings import settings
import os


df = get_df()

def get_monthly_growth():
    monthly_growth = calculate_monthly_growth(df)
    return monthly_growth

def monthly_growth_chart():
    matrix = calculate_monthly_growth(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "monthly_growth.png")
    plot_monthly_growth(matrix, plot_path)
    return {"image_url":f"{plot_path}"}