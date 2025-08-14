def calculate_orders_heatmap(df):
    df["order_weekday"] = df["InvoiceDate"].dt.dayofweek
    df["order_hour"] = df["InvoiceDate"].dt.hour
    heatmap_data = df.groupby(["order_weekday", "order_hour"])["InvoiceNo"].count().unstack(fill_value = 0)
    return heatmap_data