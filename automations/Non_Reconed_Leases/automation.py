import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def Non_Reconed_Leases(file_name_import_csv_0, file_name_import_csv_1, file_name_import_csv_2, file_name_export_csv_0):
    commercial_real_estate_snowflake = pd.read_csv(file_name_import_csv_0)
    Prologis_v1 = pd.read_csv(file_name_import_csv_1)
    Warehouse_REIT_v1 = pd.read_csv(file_name_import_csv_2)
    
    Warehouse_REIT_v1.rename(columns={'SQM': 'Square Meters'}, inplace=True)
    
    Prologis_v1 = Prologis_v1[Prologis_v1['Stategy'].apply(lambda val: all(val != s for s in ['Mixed Use', 'Office']))]
    
    df_concat = pd.concat([Warehouse_REIT_v1, Prologis_v1], join='inner', ignore_index=True)
    
    temp_df = commercial_real_estate_snowflake.drop_duplicates(subset=['Lease ID']) # Remove duplicates so lookup merge only returns first match
    df_merge = df_concat.merge(temp_df, left_on=['Lease ID'], right_on=['Lease ID'], how='left', suffixes=['_df_concat', '_commercial_real_estate_snowflake'])
    
    df_merge.insert(16, 'Net Effective Rent Check', (df_merge['Net Effective Rent_df_concat'] - df_merge['Net Effective Rent_commercial_real_estate_snowflake']) < 1)
    
    df_merge = df_merge[df_merge['Net Effective Rent Check'] == False]
    
    Failing_Rentals = df_merge
    
    Failing_Rentals.to_csv(file_name_export_csv_0, index=False)
    
    return commercial_real_estate_snowflake, Prologis_v1, Warehouse_REIT_v1, df_concat, Failing_Rentals


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/Non_Reconed_Leases/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/Non_Reconed_Leases/data/commercial_real_estate_snowflake.csv"
file_name_import_csv_1 = r"automations/Non_Reconed_Leases/data/Prologis v1.csv"
file_name_import_csv_2 = r"automations/Non_Reconed_Leases/data/Warehouse REIT v1.csv"
file_name_export_csv_0 = f"automations/Non_Reconed_Leases/runs/{export_time}/file_name_export_csv_0.csv"
Non_Reconed_Leases(file_name_import_csv_0, file_name_import_csv_1, file_name_import_csv_2, file_name_export_csv_0)