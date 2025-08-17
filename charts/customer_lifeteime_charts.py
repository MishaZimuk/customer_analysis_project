import matplotlib.pyplot as plt
import seaborn as sns
from utils.plots import save_plot

def plot_customer_lifetime(lifetime_df, save_path):
    plt.figure(figsize=(10, 6))
    sns.histplot(lifetime_df["lifetime_days"], bins=30, kde=False)
    plt.title("Customer Lifetime Distribution")
    plt.xlabel("Lifetime (days)")
    plt.ylabel("Number of Customers")
    save_plot(plt, save_path)