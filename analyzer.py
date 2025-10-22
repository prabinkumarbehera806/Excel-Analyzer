import pandas as pd
from natsort import natsorted

def analyze_excel(file):
    # Read the Excel file
    df = pd.read_excel(file)

    # Keep relevant columns
    relevant_data = df[['Station_ID', 'Date_Time', 'PCode', 'Result']].copy()

    # Convert datetime
    relevant_data['Date_Time'] = pd.to_datetime(relevant_data['Date_Time']).dt.date

    # Split by Station
    rd_ct = relevant_data[relevant_data['Station_ID'] == 'CT'][['Station_ID', 'Date_Time', 'PCode', 'Result']]
    rd_tus = relevant_data[relevant_data['Station_ID'] == 'TUS'][['Station_ID', 'Date_Time', 'PCode', 'Result']]

    # Pivot
    ct_pivot = rd_ct.pivot_table(
        index=['Station_ID', 'Date_Time'],
        columns='PCode',
        values='Result',
        aggfunc='mean',
        fill_value=' '
    )
    tus_pivot = rd_tus.pivot_table(
        index=['Station_ID', 'Date_Time'],
        columns='PCode',
        values='Result',
        aggfunc='mean',
        fill_value=' '
    )

    # Sort columns naturally
    ct_pivot = ct_pivot[natsorted(ct_pivot.columns)]
    tus_pivot = tus_pivot[natsorted(tus_pivot.columns)]

    # Save to Excel
    ct_output = 'CT Analysis.xlsx'
    tus_output = 'TUS Analysis.xlsx'
    ct_pivot.to_excel(ct_output, index=True)
    tus_pivot.to_excel(tus_output, index=True)

    return ct_output, tus_output
