from matplotlib import pyplot as plt

from utils.plots import save_plot


def plot_orders_by_day_of_month(df, save_path):
    plt.figure(figsize=(10, 6))
    df.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Orders by Day of Month")
    plt.xlabel("Day of Month")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=0)
    save_plot(plt, save_path)
   