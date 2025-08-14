def calculate_customer_lifetime(df):
    lifetime_df = (
        df.groupby("CustomerID")
        .agg(first_order_date=("InvoiceDate", "min"),
             last_order_date=("InvoiceDate", "max"))
        .assign(lifetime_days=lambda x: (x["last_order_date"] - x["first_order_date"]).dt.days)
        .reset_index()
    )
    return lifetime_df