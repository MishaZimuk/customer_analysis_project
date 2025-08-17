from utils.data import get_df
from analysis.repeat_rate_analysis import calculate_repeat_rate
from charts.repeat_rate_charts import plot_repeat_rate
from utils.settings import IMAGES_DIR
import os

df = get_df()
def get_repeat_rate():
    repeat_rate = calculate_repeat_rate(df)
    return repeat_rate

def repeat_rate_chart():
    repeat_rate = calculate_repeat_rate(df)
    plot_path = os.path.join(IMAGES_DIR, "repeat_rate.png")
    plot_repeat_rate(repeat_rate, plot_path)
    return {"image_url":f"/images/repeat_rate.png"}