from matplotlib import pyplot as plt


def plot_monthly_growth(df, save_path):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.bar(df['Month'], df['Orders'], color='lightgray', label='Orders')
    ax1.set_ylabel('Orders', color='black')
    ax1.set_xlabel('Month')
    ax2 = ax1.twinx()
    ax2.plot(df['Month'], df['Growth (%)'], color='green', marker='o', label='Growth (%)')
    ax2.set_ylabel('Growth (%)', color='green')
    plt.title("Month-over-Month Order Growth")
    fig.tight_layout()
    plt.savefig(save_path)
    plt.close()