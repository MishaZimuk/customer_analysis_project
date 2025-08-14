from utils.data import get_df
from analysis.retention_analysis import calculate_retention
from charts.retention_charts import plot_retention
from utils.settings import settings
import os

df = get_df()

def get_retention():
    retention = calculate_retention(df)
    retention_table = {
        "index": retention.index.astype(str).tolist(),
        "columns": retention.columns.astype(str).to_list(),
        "data": retention.values.tolist()
    }
    return retention_table

def retention_chart():
    matrix = calculate_retention(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "retention.png")
    plot_retention(matrix, plot_path)
    return {"image_url":f"{plot_path}"}