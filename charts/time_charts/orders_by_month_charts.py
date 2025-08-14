from matplotlib import pyplot as plt
from utils.plots import save_plot


def plot_orders_by_month(data, save_path):
    plt.figure(figsize=(10, 6))
    data.index = data.index.astype(str)
    data.plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.title("Monthly Orders")
    plt.xlabel("Month")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=45)
    save_plot(plt, save_path)
    plt.close()