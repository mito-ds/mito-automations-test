import os
import sys
from mitosheet.public.v3 import *
import pandas as pd
import numpy as np

def blah123123(file_name_import_csv_0, file_name_export_excel_0):
    performance = pd.read_csv(file_name_import_csv_0)
    
    performance['Date'] = pd.to_datetime(performance['Date'], format='mixed', errors='coerce')
    
    tmp_df = performance[['MoM Return', 'Date']].copy()
    tmp_df['Date (year-month)'] = tmp_df['Date'].dt.strftime("%Y-%m")
    pivot_table = tmp_df.pivot_table(
        index=['Date (year-month)'],
        values=['MoM Return'],
        aggfunc={'MoM Return': ['mean']}
    )
    pivot_table = pivot_table.set_axis([flatten_column_header(col) for col in pivot_table.keys()], axis=1)
    performance_pivot = pivot_table.reset_index()
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        performance_pivot.to_excel(writer, sheet_name="performance_pivot", index=False)
        add_formatting_to_excel_sheet(writer, "performance_pivot", performance_pivot, 
            conditional_formats=[
                {'columns': ['MoM Return mean'], 'filters': [{'condition': 'greater', 'value': 0}], 'font_color': None, 'background_color': '#77bb41'},
                {'columns': ['MoM Return mean'], 'filters': [{'condition': 'less', 'value': 0}], 'font_color': None, 'background_color': '#ff4013'}
            ]
        )
    
    performance_pivot_styler = performance_pivot.style\
    .apply(lambda series: np.where(series > 0, 'background-color: #77bb41', None), subset=['MoM Return mean'])\
    .apply(lambda series: np.where(series < 0, 'background-color: #ff4013', None), subset=['MoM Return mean'])
    
    return performance, performance_pivot


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/blah123123/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/blah123123/data/performance.csv"
file_name_export_excel_0 = f"automations/blah123123/runs/{export_time}/file_name_export_excel_0.xlsx"
blah123123(file_name_import_csv_0, file_name_export_excel_0)