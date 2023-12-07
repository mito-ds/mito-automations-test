from mitosheet.public.v3 import *
import pandas as pd
import numpy as np

def test1(file_name_import_csv_0):
    performance = pd.read_csv(file_name_import_csv_0)
    
    performance['Date'] = pd.to_datetime(performance['Date'], format='mixed', errors='coerce')
    
    tmp_df = performance[['Fund', 'Date', 'MoM Return']].copy()
    tmp_df['Date (year)'] = tmp_df['Date'].dt.year
    pivot_table = tmp_df.pivot_table(
        index=['Fund'],
        columns=['Date (year)'],
        values=['MoM Return'],
        aggfunc={'MoM Return': ['mean']}
    )
    pivot_table = pivot_table.set_axis([flatten_column_header(col) for col in pivot_table.keys()], axis=1)
    performance_pivot = pivot_table.reset_index()
    
    performance_pivot_styler = performance_pivot.style\
    .apply(lambda series: np.where(series > 1, 'color: #38571a; background-color: #cce8b5', None), subset=['MoM Return mean 2016', 'MoM Return mean 2015', 'MoM Return mean 2023', 'MoM Return mean 2017', 'MoM Return mean 2019', 'MoM Return mean 2020', 'MoM Return mean 2021', 'MoM Return mean 2022', 'MoM Return mean 2018'])\
    .apply(lambda series: np.where(series < -1, 'color: #831100; background-color: #ffb5af', None), subset=['MoM Return mean 2016', 'MoM Return mean 2015', 'MoM Return mean 2023', 'MoM Return mean 2017', 'MoM Return mean 2019', 'MoM Return mean 2020', 'MoM Return mean 2021', 'MoM Return mean 2022', 'MoM Return mean 2018'])
    
    return performance, performance_pivot



# Run the automation
file_name_import_csv_0 = r"automations/test1/data/performance.csv"
test1(file_name_import_csv_0)