import seaborn as sns
import matplotlib.pyplot as plt

from utils.plots import save_plot

def plot_cohort(retention, save_path):
    plt.figure(figsize=(12, 6))
    sns.heatmap(retention, annot=True, fmt='.0%', cmap="Blues", cbar=False)
    plt.title('Monthly Retention by Cohort')
    plt.ylabel('Cohort (First Order Month)')
    plt.xlabel('Months Since First Order')
    save_plot(plt, save_path)
    plt.close()