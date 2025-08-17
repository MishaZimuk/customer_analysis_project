import matplotlib.pyplot as plt
from utils.plots import save_plot

def plot_rfm(df, save_path):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Recency'], df['Frequency'], s=80, alpha=0.7)
    plt.title("RFM Scatter Plot")
    plt.xlabel("Recency")
    plt.ylabel("Frequency")
    plt.grid(True)
    save_plot(plt, save_path)