import pandas as pd

def ct_analysis(df):
    # Select relevant columns
    relevant_data = df[['Station_ID', 'Date_Time', 'PCode', 'Result']].copy()

    # Filter for Station CT
    relevant_data_ct = relevant_data[relevant_data['Station_ID'] == 'CT'].copy()

    # Pivot the CT data
    ct_pivot = relevant_data_ct.pivot(index='Date_Time', columns='PCode', values='Result')

    # Reset index so it looks cleaner in Excel
    ct_pivot.reset_index(inplace=True)

    return ct_pivot


def tus_analysis(df):
    # Select relevant columns
    relevant_data = df[['Station_ID', 'Date_Time', 'PCode', 'Result']].copy()

    # Filter for Station TUS
    relevant_data_tus = relevant_data[relevant_data['Station_ID'] == 'TUS'].copy()

    # Pivot the TUS data
    tus_pivot = relevant_data_tus.pivot(index='Date_Time', columns='PCode', values='Result')

    # Reset index so it looks cleaner in Excel
    tus_pivot.reset_index(inplace=True)

    return tus_pivot
