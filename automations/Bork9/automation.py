import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def bork9(file_name_import_csv_0, file_name_export_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-g5kj', df_export['2'])
    
    df_export.to_csv(file_name_export_csv_0, index=False)
    
    return df_export


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(os.path.dirname(f"automations/automations/Bork9/runs/{export_time}"))
# List all of the folders, so we can debug automation
print(os.getcwd())
print(os.listdir(os.path.dirname(f"automations/automations/automations/Bork9/runs/{export_time}")))
print(os.listdir(os.path.dirname(f"automations/automations/Bork9")))
print(os.listdir(os.path.dirname(f"automations/automations/Bork9/runs")))
print(os.listdir(os.path.dirname(f"automations/automations/Bork9/runs/{export_time}")))

# Run the automation
file_name_import_csv_0 = r"automations/Bork9/data/df_export.csv"
file_name_export_csv_0 = f"automations/Bork9/runs/{export_time}/file_name_export_csv_0.csv"
bork9(file_name_import_csv_0, file_name_export_csv_0)