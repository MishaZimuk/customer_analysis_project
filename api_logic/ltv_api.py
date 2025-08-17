from utils.data import get_df
from analysis.ltv_analysis import calculate_ltv
from charts.ltv_charts import plot_ltv
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_ltv():
    ltv_cum_by_rank_table = calculate_ltv(df).to_dict()
    return ltv_cum_by_rank_table

def ltv_chart():
    matrix = calculate_ltv(df)
    plot_path = os.path.join(IMAGES_DIR, "ltv.png")
    plot_ltv(matrix, plot_path)
    return {"image_url":f"/images/ltv.png"}