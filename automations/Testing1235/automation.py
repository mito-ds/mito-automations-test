from mitosheet.public.v3 import *
import pandas as pd

def testing1235(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    return df_export



# Run the automation
file_name_import_csv_0 = r"automations/Testing1235/data/df_export.csv"
testing1235(file_name_import_csv_0)