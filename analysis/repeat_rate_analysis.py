def calculate_repeat_rate(df):
    repeat_rate = round((df.groupby("CustomerID")["InvoiceNo"].nunique()>1).mean(), 3)
    return repeat_rate