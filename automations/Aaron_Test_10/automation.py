from mitosheet.public.v3 import *
import pandas as pd

def Aaron_Test_10(file_name_import_csv_0):
    dataset = pd.read_csv(file_name_import_csv_0)
    
    dataset.insert(6, 'NEW', LEFT(dataset['doc_id']))
    
    return dataset



# Run the automation
file_name_import_csv_0 = r"automations/Aaron_Test_10/data/dataset.csv"
Aaron_Test_10(file_name_import_csv_0)