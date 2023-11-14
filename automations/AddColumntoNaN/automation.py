from mitosheet.public.v3 import *
import pandas as pd

def function_wgkg(file_name_import_csv_0):
    test = pd.read_csv(file_name_import_csv_0, sep='A')
    
    test.insert(1, 'new-column-resl', 0)
    
    test['Unnamed: 1'] = test['new-column-resl'] + 10
    
    return test
