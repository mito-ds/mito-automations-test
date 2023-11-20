import os
import sys
from mitosheet.public.v3 import *
import pandas as pd

def Net_Rent(file_name_import_csv_0, file_name_import_csv_1, file_name_export_excel_0):
    commercial_real_estate_snowflake = pd.read_csv(file_name_import_csv_0)
    Prologis_v1 = pd.read_csv(file_name_import_csv_1)
    
    Prologis_v1 = Prologis_v1[Prologis_v1['Stategy'].apply(lambda val: all(val != s for s in ['Mixed Use', 'Office']))]
    
    temp_df = commercial_real_estate_snowflake.drop_duplicates(subset=['Lease ID']) # Remove duplicates so lookup merge only returns first match
    df_merge = Prologis_v1.merge(temp_df, left_on=['Lease ID'], right_on=['Lease ID'], how='left', suffixes=['_Prologis_v1', '_commercial_real_estate_snowflake'])
    
    df_merge.insert(17, 'new-column-sdbb', df_merge['Net Effective Rent_Prologis_v1'] - df_merge['Net Effective Rent_commercial_real_estate_snowflake'] == 0)
    
    df_merge = df_merge[df_merge['new-column-sdbb'] == False]
    
    df_merge.rename(columns={'new-column-sdbb': 'Net Rent Check'}, inplace=True)
    
    net_rent_differences = df_merge
    
    with pd.ExcelWriter(file_name_export_excel_0, engine="openpyxl") as writer:
        net_rent_differences.to_excel(writer, sheet_name="net_rent_differences", index=False)
    
    return commercial_real_estate_snowflake, Prologis_v1, net_rent_differences


# Create a folder for this run
export_time = sys.argv[1]
os.makedirs(f"automations/Net_Rent/runs/{export_time}")

# Run the automation
file_name_import_csv_0 = r"automations/Net_Rent/data/commercial_real_estate_snowflake.csv"
file_name_import_csv_1 = r"automations/Net_Rent/data/Prologis v1.csv"
file_name_export_excel_0 = f"automations/Net_Rent/runs/{export_time}/file_name_export_excel_0.xlsx"
Net_Rent(file_name_import_csv_0, file_name_import_csv_1, file_name_export_excel_0)