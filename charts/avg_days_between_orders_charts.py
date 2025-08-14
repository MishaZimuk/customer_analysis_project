import matplotlib.pyplot as plt
import seaborn as sns
from utils.plots import save_plot

def plot_avg_days_between_orders(df_avg_days, save_path):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_avg_days, x='AvgDaysBetweenOrders', color='skyblue')
    plt.title('Distribution of Average Days Between Orders')
    plt.xlabel('Average Days')
    plt.grid(axis='x')
    save_plot(plt, save_path)
    plt.close()
