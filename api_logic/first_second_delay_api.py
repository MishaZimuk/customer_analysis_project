from utils.data import get_df
from analysis.first_second_delay_analysis import calculate_first_second_delay
from charts.firsr_sedond_delay_charts import plot_first_second_delay
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_first_second_delay():
    first_second_delay = calculate_first_second_delay(df)
    return first_second_delay

def first_second_delay_chart():
    matrix = calculate_first_second_delay(df)
    plot_path = os.path.join(IMAGES_DIR, "first_second_delay.png")
    plot_first_second_delay(matrix, plot_path)
    return {"image_url":f"/images/first_second_delay.png"}