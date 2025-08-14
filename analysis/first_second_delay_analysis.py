import pandas as pd


def calculate_first_second_delay(df):
    df = df.sort_values(['CustomerID', 'InvoiceDate'])

    df['order_rank'] = df.groupby('CustomerID')['InvoiceDate'].rank(method='first')
    first_orders = df[df['order_rank'] == 1]
    second_orders = df[df['order_rank'] == 2]

    merged = pd.merge(
        first_orders[['CustomerID', 'InvoiceDate']],
        second_orders[['CustomerID', 'InvoiceDate']],
        on='CustomerID',
        suffixes=('_first', '_second')
    )

    merged['delay_days'] = (merged['InvoiceDate_second'] - merged['InvoiceDate_first']).dt.days
    filtered = merged[(merged["delay_days"]>=1)&(merged["delay_days"]<=90)]
    return filtered