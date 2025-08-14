from utils.data import get_df
from analysis.rfm_analysis import calculate_rfm
from charts.rfm_charts import plot_rfm
from utils.settings import settings
import os


df = get_df()

def get_rfm():
    rfm_table = calculate_rfm(df)
    return rfm_table.to_dict()

def rfm_chart():
    matrix = calculate_rfm(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "rfm.png")
    plot_rfm(matrix, plot_path)
    return {"image_url":f"{plot_path}"}