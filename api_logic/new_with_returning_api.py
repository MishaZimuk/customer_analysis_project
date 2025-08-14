from utils.data import get_df
from analysis.new_vs_returning_analysis import calculate_new_vs_returning
from charts.new_vs_returning_charts import plot_new_vs_returning
from utils.settings import settings
import os


df=get_df()

def get_new_vs_returning():
    new_vs_returning = calculate_new_vs_returning(df).to_dict()
    return new_vs_returning

def new_vs_returning_chart():
    matrix = calculate_new_vs_returning(df)
    plot_path = os.path.join(settings.IMAGES_DIR, "new_vs_returning.png")
    plot_new_vs_returning(matrix, plot_path)
    return {"image_url":f"{plot_path}"}