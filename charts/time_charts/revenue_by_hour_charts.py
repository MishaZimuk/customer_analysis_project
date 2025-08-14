from matplotlib import pyplot as plt

from utils.plots import save_plot


def plot_revenue_by_hour(df, save_path):
    plt.figure(figsize=(10, 6))
    df.plot(kind="bar", color = "mediumseagreen")
    plt.title('Revenue by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Revenue')
    plt.xticks(range(0, 24))
    plt.grid(True)
    save_plot(plt, save_path)
    plt.close()