def calculate_cohort(df):
    df['OrderMonth'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    df['CohortMonth'] = df.groupby('CustomerID')['InvoiceDate'].transform('min').dt.to_period('M').dt.to_timestamp()
    df['CohortIndex'] = ((df['OrderMonth'].dt.year - df['CohortMonth'].dt.year) * 12 +
                         (df['OrderMonth'].dt.month - df['CohortMonth'].dt.month) + 1)
    cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerID'].nunique().reset_index()
    cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerID')
    cohort_size = cohort_pivot[1]
    retention = cohort_pivot.divide(cohort_size, axis=0).round(3)
    return retention