import os
import sys
from mitosheet.public.v3 import *
import pandas as pd
import numpy as np

def This_Has_Spaces_and_Others(file_name_import_csv_0, file_name_export_excel_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-cerq', 0)
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        df_export.to_excel(writer, sheet_name="df_export", index=False)
        add_formatting_to_excel_sheet(writer, "df_export", df_export, 
            conditional_formats=[
                {'columns': ['new-column-cerq'], 'filters': [{'condition': 'number_exactly', 'value': 0}], 'font_color': '#e32400', 'background_color': None}
            ]
        )
    
    df_export_styler = df_export.style\
    .apply(lambda series: np.where(series == 0, 'color: #e32400', None), subset=['new-column-cerq'])
    
    return df_export


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/This_Has_Spaces_and_Others/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/This_Has_Spaces_and_Others/data/df_export.csv"
file_name_export_excel_0 = f"automations/This_Has_Spaces_and_Others/runs/{export_time}/file_name_export_excel_0.xlsx"
This_Has_Spaces_and_Others(file_name_import_csv_0, file_name_export_excel_0)