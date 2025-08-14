import matplotlib.pyplot as plt
from utils.plots import save_plot

def plot_segment(summary_df, save_path):
    plt.figure(figsize=(10, 5))
    plt.bar(summary_df["segment"], summary_df["total_revenue"])
    plt.title("Total Revenue per RFM Segment")
    plt.ylabel("Revenue")
    plt.xlabel("Segment")
    plt.xticks(rotation=45)
    save_plot(plt, save_path)
    plt.close()