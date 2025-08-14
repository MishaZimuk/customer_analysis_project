import pandas as pd


def calculate_monthly_growth(df):
    df['order_month'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    orders_by_month = df.groupby('order_month')['InvoiceNo'].nunique()
    growth = orders_by_month.pct_change().fillna(0) * 100
    growth_df = pd.DataFrame({
        'Month': orders_by_month.index,
        'Orders': orders_by_month.values,
        'Growth (%)': growth.round(2)
    })
    return growth_df