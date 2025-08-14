from matplotlib import pyplot as plt
from utils.plots import save_plot


def plot_avg_order_value_by_hour(df, save_path):
    plt.figure(figsize=(10, 6))
    df.plot(kind="bar", color = "mediumseagreen")
    plt.title('Average Order Value by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Order Value')
    plt.xticks(range(0, 24))
    plt.grid(True)
    save_plot(plt, save_path)
    plt.close()