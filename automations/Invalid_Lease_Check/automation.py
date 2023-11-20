import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def Invalid_Lease_Check(file_name_import_csv_0, file_name_import_csv_1, file_name_export_excel_0):
    commercial_real_estate_snowflake = pd.read_csv(file_name_import_csv_0)
    Prologis_v1 = pd.read_csv(file_name_import_csv_1)
    
    Prologis_v1 = Prologis_v1[Prologis_v1['Stategy'].apply(lambda val: all(val != s for s in ['Mixed Use', 'Office']))]
    
    temp_df = commercial_real_estate_snowflake.drop_duplicates(subset=['Lease ID']) # Remove duplicates so lookup merge only returns first match
    df_merge = Prologis_v1.merge(temp_df, left_on=['Lease ID'], right_on=['Lease ID'], how='left', suffixes=['_Prologis_v1', '_commercial_real_estate_snowflake'])
    
    df_merge.insert(17, 'Net Effective Check', ABS(df_merge['Net Effective Rent_commercial_real_estate_snowflake']-df_merge['Net Effective Rent_Prologis_v1']) < 10)
    
    df_merge = df_merge[df_merge['Net Effective Check'] == False]
    
    invalid_leases = df_merge
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        invalid_leases.to_excel(writer, sheet_name="invalid_leases", index=False)
    
    return commercial_real_estate_snowflake, Prologis_v1, invalid_leases


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/Invalid_Lease_Check/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/Invalid_Lease_Check/data/commercial_real_estate_snowflake.csv"
file_name_import_csv_1 = r"automations/Invalid_Lease_Check/data/Prologis v1.csv"
file_name_export_excel_0 = f"automations/Invalid_Lease_Check/runs/{export_time}/file_name_export_excel_0.xlsx"
Invalid_Lease_Check(file_name_import_csv_0, file_name_import_csv_1, file_name_export_excel_0)