from analysis.basic_overview import basic_stats, monthly_stats
from utils.data import get_df

df = get_df()

def get_basic_stats():
    stats = basic_stats(df)
    return stats

def get_monthly_stats():
    monthly = monthly_stats(df).to_dict()
    return monthly