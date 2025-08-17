from matplotlib import pyplot as plt
from utils.plots import save_plot


def plot_new_vs_returning(data, save_path):
    data.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightcoral', 'skyblue'])
    plt.title('New vs Returning Customers by Month')
    plt.ylabel('Number of Customers')
    plt.xlabel('Order Month')
    plt.xticks(rotation=45)
    save_plot(plt, save_path)