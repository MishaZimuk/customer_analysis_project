def calculate_new_vs_returning(df):
    df['OrderMonth'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    df['FirstOrderMonth'] = df.groupby('CustomerID')['InvoiceDate'].transform('min').dt.to_period('M').dt.to_timestamp()
    
    df['CustomerType'] = df.apply(lambda x: 'New' if x['OrderMonth'] == x['FirstOrderMonth'] else 'Returning', axis=1)
    
    result = df.groupby(['OrderMonth', 'CustomerType'])['CustomerID'].nunique().unstack().fillna(0)
    result.columns.name = None
    return result