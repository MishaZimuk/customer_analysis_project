import matplotlib.pyplot as plt
from utils.plots import save_plot

def plot_repeat_rate(repeat_rate,save_path):
    labels = ['Repeat Customers', 'One-time Customers']
    sizes = [repeat_rate, 1 - repeat_rate]
    colors = ['#66b3ff','#ff9999']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Repeat Rate')
    plt.axis('equal')
    save_plot(plt, save_path)
    plt.close()