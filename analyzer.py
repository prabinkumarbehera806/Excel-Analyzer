import pandas as pd

def ct_analysis(df):
    """
    Returns CT pivoted dataframe with natural-sorted columns.
    Expects df to have columns: Station_ID, Date_Time, PCode, Result
    """
    relevant_data = df[['Station_ID', 'Date_Time', 'PCode', 'Result']].copy()
    relevant_data_ct = relevant_data[relevant_data['Station_ID'] == 'CT'].copy()

    ct_pivot = relevant_data_ct.pivot(index='Date_Time', columns='PCode', values='Result')
    ct_pivot.reset_index(inplace=True)

    # Natural sort columns if natsort is available, otherwise do a normal sort
    try:
        from natsort import natsorted
        cols = ['Date_Time'] + natsorted([c for c in ct_pivot.columns if c != 'Date_Time'])
        ct_pivot = ct_pivot[cols]
    except Exception:
        # fallback: keep Date_Time first, then alphabetical
        cols = ['Date_Time'] + sorted([c for c in ct_pivot.columns if c != 'Date_Time'])
        ct_pivot = ct_pivot[cols]

    return ct_pivot


def tus_analysis(df):
    """
    Returns TUS pivoted dataframe with natural-sorted columns.
    Expects df to have columns: Station_ID, Date_Time, PCode, Result
    """
    relevant_data = df[['Station_ID', 'Date_Time', 'PCode', 'Result']].copy()
    relevant_data_tus = relevant_data[relevant_data['Station_ID'] == 'TUS'].copy()

    tus_pivot = relevant_data_tus.pivot(index='Date_Time', columns='PCode', values='Result')
    tus_pivot.reset_index(inplace=True)

    # Natural sort columns if natsort is available, otherwise do a normal sort
    try:
        from natsort import natsorted
        cols = ['Date_Time'] + natsorted([c for c in tus_pivot.columns if c != 'Date_Time'])
        tus_pivot = tus_pivot[cols]
    except Exception:
        # fallback: keep Date_Time first, then alphabetical
        cols = ['Date_Time'] + sorted([c for c in tus_pivot.columns if c != 'Date_Time'])
        tus_pivot = tus_pivot[cols]

    return tus_pivot
