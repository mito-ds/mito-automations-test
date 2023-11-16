from mitosheet.public.v3 import *
import pandas as pd

def bark1(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-g5kj', df_export['2'])
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/Bark1/data/df_export.csv"
bark1(file_name_import_csv_0)