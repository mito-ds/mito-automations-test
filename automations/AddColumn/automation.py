from mitosheet.public.v3 import *
import pandas as pd

def function_rrjl(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-d8ci', 0)
    
    return df_export
