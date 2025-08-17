from utils.data import get_df
from analysis.time_analysis.orders_heatmap_analysis import calculate_orders_heatmap
from charts.time_charts.orders_heatmap_charts import plot_orders_heatmap
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_orders_heatmap():
    orders_heatmap = calculate_orders_heatmap(df).to_dict()
    return orders_heatmap

def orders_heatmap_chart():
    matrix = calculate_orders_heatmap(df)
    plot_path = os.path.join(IMAGES_DIR, "orders_heatmap.png")
    plot_orders_heatmap(matrix, plot_path)
    return {"image_url":f"/image/orders_heatmap.png"}