from utils.data import get_df
from analysis.customer_lifetime_analysis import calculate_customer_lifetime
from charts.customer_lifeteime_charts import plot_customer_lifetime
from utils.settings import settings
import os

df = get_df()

def get_customer_lifetime():
    customer_lifetime = calculate_customer_lifetime(df)
    return customer_lifetime

def customer_lifetime_chart():
    matrix = calculate_customer_lifetime(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "customer_lifetime.png")
    plot_customer_lifetime(matrix, plot_path)
    return {"image_url":f"{plot_path}"}