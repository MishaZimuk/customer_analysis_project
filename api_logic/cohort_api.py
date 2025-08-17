from utils.data import get_df
from analysis.cohort_analysis import calculate_cohort
from charts.cohort_charts import plot_cohort
from utils.settings import IMAGES_DIR
import os

df = get_df()

def get_cohort():
    cohort = calculate_cohort(df)
    return cohort

def cohort_chart():
    matrix = calculate_cohort(df)
    plot_path = os.path.join(IMAGES_DIR, "cohort.png")
    plot_cohort(matrix, plot_path)
    return {"image_url":f"/images/cohort.png"}