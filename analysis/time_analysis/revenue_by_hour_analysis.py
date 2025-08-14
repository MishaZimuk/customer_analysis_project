def calculate_revenue_by_hour(df):
    df['hour'] = df['InvoiceDate'].dt.hour
    revenue_by_hour = df.groupby('hour')['TotalPrice'].sum()
    return revenue_by_hour