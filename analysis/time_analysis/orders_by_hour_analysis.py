def calculate_orders_by_hour(df):
    df['order_hour'] = df['InvoiceDate'].dt.hour
    orders_by_hour = df.groupby('order_hour')['InvoiceNo'].nunique()
    return orders_by_hour