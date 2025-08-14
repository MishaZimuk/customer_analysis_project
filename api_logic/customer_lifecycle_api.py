from utils.data import get_df
from analysis.customer_lifecycle_analysis import calculate_customer_lifecycle
from charts.customer_lifecycle_charts import plot_customer_lifecycle
from utils.settings import settings
import os

df = get_df()

def get_customer_lifecycle():
    customer_lifecycle = calculate_customer_lifecycle(df)
    return customer_lifecycle

def customer_lifecycle_chart():
    matrix = calculate_customer_lifecycle(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "customer_lifecycle.png")
    plot_customer_lifecycle(matrix, plot_path)
    return {"image_url":f"{plot_path}"}