from mitosheet.public.v3 import *
from __main__ import ADDONE
import pandas as pd

def addonetest(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-gx6z', 0)
    
    df_export.insert(3, 'new-column-j02u', ADDONE(df_export['new-column-gx6z']))
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/AddOneTest/data/df_export.csv"
addonetest(file_name_import_csv_0)