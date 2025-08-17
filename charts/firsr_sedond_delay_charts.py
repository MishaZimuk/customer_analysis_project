import matplotlib.pyplot as plt

from utils.plots import save_plot

def plot_first_second_delay(merged, save_path):
    plt.figure(figsize=(10, 6))
    plt.hist(merged['delay_days'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Delay Between First and Second Orders')
    plt.xlabel('Days Between Orders')
    plt.ylabel('Number of Customers')
    plt.grid(True)
    save_plot(plt, save_path)