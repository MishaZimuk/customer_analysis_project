def calculate_churn_status(df, churn_days=60):
    last_date = df['InvoiceDate'].max()
    last_order = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
    last_order['DaysSinceLastOrder'] = (last_date - last_order['InvoiceDate']).dt.days
    last_order['ChurnStatus'] = last_order['DaysSinceLastOrder'].apply(
        lambda x: 'Churned' if x >= churn_days else 'Active'
    )
    return last_order