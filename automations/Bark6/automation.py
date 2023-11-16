import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def bark6(file_name_import_csv_0, file_name_export_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-g5kj', df_export['2'])
    
    df_export.to_csv(file_name_export_csv_0, index=False)
    
    return df_export


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(os.path.dirname(f"automations/Bark6/runs/{export_time}"))

# Run the automation
file_name_import_csv_0 = r"automations/Bark6/data/df_export.csv"
file_name_export_csv_0 = f"automations/Bark6/runs/{export_time}/file_name_export_csv_0.csv"
bark6(file_name_import_csv_0, file_name_export_csv_0)