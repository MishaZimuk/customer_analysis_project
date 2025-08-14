def calculate_avg_order_value_by_hour(df):
    df["Hour"] = df["InvoiceDate"].dt.hour
    avg_order_value_by_hour = df.groupby("Hour")["TotalPrice"].mean().round(3)
    return avg_order_value_by_hour