def calculate_orders_by_month(df):
    df["order_month"] = df["InvoiceDate"].dt.to_period("M")
    orders_by_month = df["order_month"].value_counts().sort_index()
    return orders_by_month