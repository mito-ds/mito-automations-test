from mitosheet.public.v3 import *
import pandas as pd
import numpy as np

def loanamountpivot(file_name_import_csv_0):
    loans_export = pd.read_csv(file_name_import_csv_0)
    
    loans_export['issue_date'] = pd.to_datetime(loans_export['issue_date'], format='%Y-%m-%d', errors='coerce')
    
    tmp_df = loans_export[['issue_date', 'loan_amount']].copy()
    tmp_df['issue_date (year-month-day)'] = tmp_df['issue_date'].dt.strftime("%Y-%m-%d")
    pivot_table = tmp_df.pivot_table(
        index=['issue_date (year-month-day)'],
        values=['loan_amount'],
        aggfunc={'loan_amount': ['count']}
    )
    pivot_table = pivot_table.set_axis([flatten_column_header(col) for col in pivot_table.keys()], axis=1)
    loans_export_pivot = pivot_table.reset_index()
    
    loans_export_pivot_styler = loans_export_pivot.style\
    .apply(lambda series: np.where(series > 1000, 'background-color: #669c35', None), subset=['loan_amount count'])
    
    return loans_export, loans_export_pivot



# Run the automation
file_name_import_csv_0 = r"automations/LoanAmountPivot/data/loans_export.csv"
loanamountpivot(file_name_import_csv_0)