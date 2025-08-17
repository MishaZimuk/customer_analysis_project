import matplotlib.pyplot as plt
from utils.plots import save_plot

def plot_ltv(df, save_path):
    plt.figure(figsize=(12, 6))
    for cohort in df.index:
        plt.plot(df.columns, df.loc[cohort], label=str(cohort))

    plt.title('LTV by Cohort')
    plt.xlabel('Months Since First Purchase')
    plt.ylabel('Cumulative Revenue per Customer')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    save_plot(plt, save_path)