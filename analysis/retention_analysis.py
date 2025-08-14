def get_month_diff(d1, d2):
        return (d1.dt.year - d2.dt.year)*12 + (d1.dt.month - d2.dt.month)
def calculate_retention(df):
    df["OrderMonth"] = df["InvoiceDate"].dt.to_period("M")
    df["CohortMonth"] = df.groupby("CustomerID")["InvoiceDate"].transform("min").dt.to_period("M")    
    df["CohortIndex"] = get_month_diff(df["OrderMonth"], df["CohortMonth"])+1
    cohort_data = df.groupby(["CohortMonth", "CohortIndex"])["CustomerID"].nunique().reset_index()
    cohort_pivot = cohort_data.pivot(index="CohortMonth", columns="CohortIndex", values="CustomerID") 
    cohort_size = cohort_pivot.iloc[:, 0]
    retention = cohort_pivot.divide(cohort_size, axis=0).round(2).fillna(0)
    return retention
                                          