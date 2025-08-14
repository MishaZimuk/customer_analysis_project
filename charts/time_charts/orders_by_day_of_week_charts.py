from matplotlib import pyplot as plt
from utils.plots import save_plot


def plot_orders_by_day_of_week(df, save_path):
    plt.figure(figsize=(10, 5))
    df.plot(kind='bar', color='mediumseagreen')
    plt.title('Orders by Day of the Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Orders')
    plt.grid(axis='y')
    save_plot(plt, save_path)
    plt.close()