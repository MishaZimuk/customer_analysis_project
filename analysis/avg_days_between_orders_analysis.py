def calculate_avg_days_between_orders(df):
    df = df.sort_values(['CustomerID', 'InvoiceDate'])
    df['PrevOrderDate'] = df.groupby('CustomerID')['InvoiceDate'].shift(1)
    df['DaysBetween'] = (df['InvoiceDate'] - df['PrevOrderDate']).dt.days
    avg_days = df.groupby('CustomerID')['DaysBetween'].mean().round(2).fillna(0).reset_index()
    avg_days.columns = ['CustomerID', 'AvgDaysBetweenOrders']
    return avg_days