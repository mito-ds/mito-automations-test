from mitosheet.public.v3 import *
import pandas as pd

def function_dsfh(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(1, 'new-column-4706', 0)
    
    return df_export
