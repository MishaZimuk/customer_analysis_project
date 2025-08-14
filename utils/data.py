import pandas as pd


def get_df():
    df = df = pd.read_csv('data/processed/online_retail_clean.csv', parse_dates=["InvoiceDate"])
    return df
