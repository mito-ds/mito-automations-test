from mitosheet.public.v3 import *
import pandas as pd

def addone2(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-gx6z', 0)
    
    df_export.insert(3, 'new-column-j02u', ADDONE(df_export['new-column-gx6z']))
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/AddOne2/data/df_export.csv"
addone2(file_name_import_csv_0)