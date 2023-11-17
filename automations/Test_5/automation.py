from mitosheet.public.v3 import *
import pandas as pd

def Test_5(file_name_import_csv_0):
    dataset = pd.read_csv(file_name_import_csv_0)
    
    dataset.insert(1, 'new-column-urib', 0)
    
    dataset['cust_number'] = to_float_series(dataset['cust_number'])
    
    dataset['new-column-urib'] = dataset['cust_number'] + 100
    
    dataset.insert(4, 'new-column-b07n', LEFT(dataset['name_customer']))
    
    dataset.insert(2, 'new-column-oj5i', CUSTOM_EDIT(dataset['new-column-urib']))
    
    dataset_styler = dataset.head(1500).style\
    .format("{:.0f}", subset=['new-column-urib'])
    
    return dataset



# Run the automation
file_name_import_csv_0 = r"automations/Test_5/data/dataset.csv"
Test_5(file_name_import_csv_0)