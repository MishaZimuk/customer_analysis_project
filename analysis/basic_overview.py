def basic_stats(df):
    total_orders = df["InvoiceNo"].nunique()
    total_revenue = df["TotalPrice"].sum()
    unique_customers = df["CustomerID"].nunique()
    unique_products = df["StockCode"].nunique()
    avg_order_value = df.groupby("InvoiceNo")["TotalPrice"].sum().mean()
    date_min = df["InvoiceDate"].min().date()
    date_max = df["InvoiceDate"].max().date()

    return {
        "total_orders": int(total_orders),
        "total_revenue": round(float(total_revenue), 2),
        "unique_customers": int(unique_customers),
        "unique_products": int(unique_products),
        "date_min": str(date_min),
        "date_max": str(date_max),
        "avg_order_value": float(avg_order_value)
    }

def monthly_stats(df):
    df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
    monthly = df.groupby('Month').agg(
        total_orders=('InvoiceNo', 'nunique'),
        total_revenue=('TotalPrice', 'sum')
    ).reset_index()
    return monthly