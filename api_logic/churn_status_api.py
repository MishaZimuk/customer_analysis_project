from utils.data import get_df
from analysis.churn_status_analysis import calculate_churn_status
from charts.churn_status_charts import plot_churn_status
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_churn_status():
    churn_status = calculate_churn_status(df)
    return churn_status

def churn_status_chart():
    matrix = calculate_churn_status(df)
    plot_path = os.path.join(IMAGES_DIR, "churn_status.png")
    plot_churn_status(matrix, plot_path)
    return {"image_url":f"/images/churn_status.png"}