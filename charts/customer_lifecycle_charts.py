import matplotlib.pyplot as plt
from utils.plots import save_plot

def plot_customer_lifecycle(df_lifecycle, save_path):
    stage_counts = df_lifecycle['LifecycleStage'].value_counts().sort_index()

    plt.figure(figsize=(8, 6))
    stage_counts.plot(kind='bar', color=['green', 'orange', 'red'])
    plt.title('Customer Lifecycle Distribution')
    plt.xlabel('Lifecycle Stage')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=0)
    save_plot(plt, save_path)
