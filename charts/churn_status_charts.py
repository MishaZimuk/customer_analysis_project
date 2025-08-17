import matplotlib.pyplot as plt
from utils.plots import save_plot

def plot_churn_status(churn_df, save_path):
    status_counts = churn_df['ChurnStatus'].value_counts()

    plt.figure(figsize=(6, 6))
    status_counts.plot(kind='pie', autopct='%1.1f%%', colors=['salmon', 'skyblue'])
    plt.title('Customer Churn Status')
    plt.ylabel('')
    save_plot(plt, save_path)