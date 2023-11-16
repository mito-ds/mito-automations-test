from mitosheet.public.v3 import *
import pandas as pd

def bill5(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/Bill5/data/df_export.csv"
bill5(file_name_import_csv_0)