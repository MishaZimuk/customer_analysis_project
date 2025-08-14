def calculate_orders_by_day_of_week(df):
    df['order_weekday'] = df['InvoiceDate'].dt.dayofweek
    day_map = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
    df["order_weekday"] = df["order_weekday"].map(day_map)
    orders_by_day = df["order_weekday"].value_counts().reindex(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    return orders_by_day