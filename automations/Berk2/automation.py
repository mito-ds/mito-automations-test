import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def berk2(file_name_import_csv_0, file_name_export_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-g5kj', df_export['2'])
    
    df_export.to_csv(file_name_export_csv_0, index=False)
    
    return df_export


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(os.path.dirname(f"automations/automations/Berk2/runs/{export_time}"))
# List all of the folders, so we can debug automation
print(os.getcwd())
print(os.listdir(f"automations"))
print(os.listdir(f"automations/automations/Berk2"))
print(os.listdir(f"automations/automations/Berk2/runs"))
print(os.listdir(f"automations/automations/Berk2/runs/{export_time}"))

# Run the automation
file_name_import_csv_0 = r"automations/Berk2/data/df_export.csv"
file_name_export_csv_0 = f"automations/Berk2/runs/{export_time}/file_name_export_csv_0.csv"
berk2(file_name_import_csv_0, file_name_export_csv_0)