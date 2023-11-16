from mitosheet.public.v3 import *
import pandas as pd

def gjgg(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/gjgg/data/df_export.csv"
gjgg(file_name_import_csv_0)