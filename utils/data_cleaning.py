import pandas as pd

df = pd.read_excel("data/raw/Online Retail.xlsx")
df = df.dropna(subset=["CustomerID"])
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[(df["Quantity"]>0)&(df["UnitPrice"]>0)]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalPrice"] = df["Quantity"]*df["UnitPrice"]
df.to_csv("data/processed/online_retail_clean.csv", index=False)