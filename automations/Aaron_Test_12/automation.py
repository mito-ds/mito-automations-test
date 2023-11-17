import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def Aaron_Test_12(file_name_import_csv_0, file_name_export_excel_0):
    dataset = pd.read_csv(file_name_import_csv_0)
    
    dataset.insert(6, 'NEW', LEFT(dataset['doc_id']))
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        dataset.to_excel(writer, sheet_name="dataset", index=False)
    
    return dataset


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/Aaron_Test_12/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/Aaron_Test_12/data/dataset.csv"
file_name_export_excel_0 = f"automations/Aaron_Test_12/runs/{export_time}/file_name_export_excel_0.xlsx"
Aaron_Test_12(file_name_import_csv_0, file_name_export_excel_0)