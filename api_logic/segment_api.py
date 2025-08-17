from utils.data import get_df
from analysis.segment_analysis import calculate_segment
from charts.segment_charts import plot_segment
from utils.settings import IMAGES_DIR
import os


df = get_df()

def get_segment():
    segment = calculate_segment(df)
    return segment

def segment_chart():
    matrix = calculate_segment(df)
    plot_path = os.path.join(IMAGES_DIR, "segment.png")
    plot_segment(matrix, plot_path)
    return {"image_url":f"/images/segment.png"}