from mitosheet.public.v3 import *
import pandas as pd
import numpy as np

def Vanguard_Performance_MoM_Report(file_name_import_csv_0):
    performance = pd.read_csv(file_name_import_csv_0)
    
    performance_styler = performance.head(1500).style\
    .apply(lambda series: np.where(series > 1, 'color: #ffffff; background-color: #38571a', None), subset=['MoM Return'])
    
    return performance



# Run the automation
file_name_import_csv_0 = r"automations/Vanguard_Performance_MoM_Report/data/performance.csv"
Vanguard_Performance_MoM_Report(file_name_import_csv_0)