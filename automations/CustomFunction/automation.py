import os
import sys
from mitosheet.public.v3 import *
from __main__ import ADDONE
import pandas as pd
import numpy as np

def customfunction(file_name_import_csv_0, file_name_export_excel_0):
    loans_export = pd.read_csv(file_name_import_csv_0)
    
    loans_export['issue_date'] = pd.to_datetime(loans_export['issue_date'], format='%Y-%m-%d', errors='coerce')
    
    tmp_df = loans_export[['loan_amount', 'issue_date']].copy()
    tmp_df['issue_date (year-month-day)'] = tmp_df['issue_date'].dt.strftime("%Y-%m-%d")
    pivot_table = tmp_df.pivot_table(
        index=['issue_date (year-month-day)'],
        values=['loan_amount'],
        aggfunc={'loan_amount': ['count']}
    )
    pivot_table = pivot_table.set_axis([flatten_column_header(col) for col in pivot_table.keys()], axis=1)
    loans_export_pivot = pivot_table.reset_index()
    
    loan_count = loans_export_pivot
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        loan_count.to_excel(writer, sheet_name="loan_count", index=False)
        add_formatting_to_excel_sheet(writer, "loan_count", loan_count, 
            conditional_formats=[
                {'columns': ['loan_amount count'], 'filters': [{'condition': 'greater', 'value': 1000}], 'font_color': None, 'background_color': '#669c35'}
            ]
        )
    
    loan_count.insert(2, 'new-column-na9u', ADDONE(loan_count['loan_amount count']))
    
    loan_count_styler = loan_count.style\
    .apply(lambda series: np.where(series > 1000, 'background-color: #669c35', None), subset=['loan_amount count'])
    
    return loans_export, loan_count


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/CustomFunction/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/CustomFunction/data/loans_export.csv"
file_name_export_excel_0 = f"automations/CustomFunction/runs/{export_time}/file_name_export_excel_0.xlsx"
customfunction(file_name_import_csv_0, file_name_export_excel_0)