import os
import sys
from mitosheet.public.v3 import *
import pandas as pd
import numpy as np

def test2(file_name_import_csv_0, file_name_export_excel_0):
    performance = pd.read_csv(file_name_import_csv_0)
    
    performance['Date'] = pd.to_datetime(performance['Date'], format='mixed', errors='coerce')
    
    tmp_df = performance[['Fund', 'Date', 'MoM Return']].copy()
    tmp_df['Date (year)'] = tmp_df['Date'].dt.year
    pivot_table = tmp_df.pivot_table(
        index=['Fund'],
        columns=['Date (year)'],
        values=['MoM Return'],
        aggfunc={'MoM Return': ['mean']}
    )
    pivot_table = pivot_table.set_axis([flatten_column_header(col) for col in pivot_table.keys()], axis=1)
    performance_pivot = pivot_table.reset_index()
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        performance_pivot.to_excel(writer, sheet_name="performance_pivot", index=False)
        add_formatting_to_excel_sheet(writer, "performance_pivot", performance_pivot, 
            conditional_formats=[
                {'columns': ['MoM Return mean 2015', 'MoM Return mean 2016', 'MoM Return mean 2017', 'MoM Return mean 2018', 'MoM Return mean 2019', 'MoM Return mean 2020', 'MoM Return mean 2021', 'MoM Return mean 2022', 'MoM Return mean 2023'], 'filters': [{'condition': 'greater', 'value': 1}], 'font_color': '#38571a', 'background_color': '#cce8b5'},
                {'columns': ['MoM Return mean 2015', 'MoM Return mean 2016', 'MoM Return mean 2017', 'MoM Return mean 2018', 'MoM Return mean 2019', 'MoM Return mean 2020', 'MoM Return mean 2021', 'MoM Return mean 2022', 'MoM Return mean 2023'], 'filters': [{'condition': 'less', 'value': -1}], 'font_color': '#831100', 'background_color': '#ffb5af'}
            ]
        )
    
    performance_pivot_styler = performance_pivot.style\
    .apply(lambda series: np.where(series > 1, 'color: #38571a; background-color: #cce8b5', None), subset=['MoM Return mean 2016', 'MoM Return mean 2015', 'MoM Return mean 2023', 'MoM Return mean 2017', 'MoM Return mean 2019', 'MoM Return mean 2020', 'MoM Return mean 2021', 'MoM Return mean 2022', 'MoM Return mean 2018'])\
    .apply(lambda series: np.where(series < -1, 'color: #831100; background-color: #ffb5af', None), subset=['MoM Return mean 2016', 'MoM Return mean 2015', 'MoM Return mean 2023', 'MoM Return mean 2017', 'MoM Return mean 2019', 'MoM Return mean 2020', 'MoM Return mean 2021', 'MoM Return mean 2022', 'MoM Return mean 2018'])
    
    return performance, performance_pivot


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/test2/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/test2/data/performance.csv"
file_name_export_excel_0 = f"automations/test2/runs/{export_time}/file_name_export_excel_0.xlsx"
test2(file_name_import_csv_0, file_name_export_excel_0)