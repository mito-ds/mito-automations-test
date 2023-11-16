from mitosheet.public.v3 import *
import pandas as pd

def function_odwu(file_name_import_csv_0):
    df_export = pd.read_csv(file_name_import_csv_0)
    
    df_export.insert(2, 'new-column-g5kj', df_export['2'])
    
    return df_export
