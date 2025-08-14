def calculate_orders_by_day_of_month(df):
    df["order_day"] = df["InvoiceDate"].dt.day
    orders_by_day_of_month = df["order_day"].value_counts().sort_index()
    return orders_by_day_of_month