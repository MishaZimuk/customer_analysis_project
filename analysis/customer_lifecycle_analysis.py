import pandas as pd
from datetime import timedelta

def calculate_customer_lifecycle(df):
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    reference_date = df['InvoiceDate'].max() + timedelta(days=1)
    
    last_order = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
    last_order['days_since_last_order'] = (reference_date - last_order['InvoiceDate']).dt.days
    
    def classify_lifecycle(days):
        if days <= 30:
            return 'Active'
        elif days <= 90:
            return 'At Risk'
        else:
            return 'Inactive'
    
    last_order['LifecycleStage'] = last_order['days_since_last_order'].apply(classify_lifecycle)
    
    return last_order[['CustomerID', 'days_since_last_order', 'LifecycleStage']]