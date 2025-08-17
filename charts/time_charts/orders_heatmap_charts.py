from matplotlib import pyplot as plt
import seaborn as sns
from utils.plots import save_plot


def plot_orders_heatmap(data, save_path):
    plt.figure(figsize=(12, 6))
    sns.heatmap(data, cmap="YlGnBu", annot=False)
    plt.title("Orders Heatmap: Weekday vs Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Day of Week")
    plt.yticks(
        ticks=[0, 1, 2, 3, 4, 5, 6],
        labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        rotation=0
    )
    save_plot(plt, save_path)