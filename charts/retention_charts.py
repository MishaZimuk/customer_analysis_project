import matplotlib.pyplot as plt
import seaborn as sns

from utils.plots import save_plot

def plot_retention(df, save_path):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title("Retention Heatmap")
    plt.ylabel("Cohort Month")
    plt.xlabel("Months Since First Purchase")
    save_plot(plt, save_path)
    plt.close()