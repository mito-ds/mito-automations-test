from mitosheet.public.v3 import *
import pandas as pd

def bork1002(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/Bork1002/data/df_export.csv"
bork1002(file_name_import_csv_0)