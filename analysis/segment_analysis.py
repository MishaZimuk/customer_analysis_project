from analysis.rfm_analysis import calculate_rfm

def map_segment(rfm_row):
    score = rfm_row['RFM_score']
    if score.startswith('5'):
        return 'Champions'
    elif score[0] in ['4', '3'] and score[1] in ['4', '5']:
        return 'Loyal Customers'
    elif score[0] == '5':
        return 'Recent Customers'
    elif score[2] == '5':
        return 'Big Spenders'
    elif score[0] in ['1', '2']:
        return 'At Risk'
    else:
        return 'Others'


def calculate_segment(df):
    rfm = calculate_rfm(df)
    rfm['segment'] = rfm.apply(map_segment, axis=1)
    summary = (
        rfm.groupby("segment")
        .agg(customer_count=("CustomerID", "nunique"),
            total_revenue=("Monetary", "sum"))
        .reset_index()
        .sort_values("total_revenue", ascending=False)
     )
    return summary