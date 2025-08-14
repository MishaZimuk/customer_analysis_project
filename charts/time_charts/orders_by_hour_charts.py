from matplotlib import pyplot as plt
from utils.plots import save_plot


def plot_orders_by_hour(df, save_path):
    plt.figure(figsize=(10, 5))
    df.plot(kind='bar', color='skyblue')
    plt.title('Number of Orders by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Orders')
    plt.grid(axis='y')
    save_plot(plt, save_path)
    plt.close()