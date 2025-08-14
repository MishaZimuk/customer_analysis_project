import pandas as pd

def calculate_ltv(df):
    df["ltv_rank"] = pd.qcut(df["TotalPrice"], q=5, labels=[5, 4, 3, 2, 1]) # 1 - top
    ltv_by_rank = df.groupby('ltv_rank')['TotalPrice'].sum().reset_index()
    ltv_by_rank['cumulative_amount'] = ltv_by_rank['TotalPrice'].cumsum()
    ltv_by_rank['cumulative_percent'] = 100 * ltv_by_rank['cumulative_amount'] / ltv_by_rank['TotalPrice'].sum()
    return ltv_by_rank