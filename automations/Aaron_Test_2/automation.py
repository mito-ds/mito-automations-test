from mitosheet.public.v3 import *
import pandas as pd

def Aaron_Test_2(file_name_import_csv_0):
    dataset = pd.read_csv(file_name_import_csv_0)
    
    dataset.insert(1, 'new-column-urib', 0)
    
    dataset['cust_number'] = to_float_series(dataset['cust_number'])
    
    dataset['new-column-urib'] = dataset['cust_number'] + 100
    
    dataset.insert(4, 'new-column-b07n', LEFT(dataset['name_customer']))
    
    dataset_styler = dataset.head(1500).style\
    .format("{:.0f}", subset=['new-column-urib'])
    
    return dataset



# Run the automation
file_name_import_csv_0 = r"automations/Aaron_Test_2/data/dataset.csv"
Aaron_Test_2(file_name_import_csv_0)