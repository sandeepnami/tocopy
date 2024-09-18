"""
Convert the files between formats like txt, csv, xlsx
PreProcess the files and save them in the desired format
"""
import pandas as pd
from my_regexp_master import rename_extension, extract_file_name
import sys

# Functions
#convert to excel
def to_excel(txtcsv_path,excel_path,delimitter = "~"):
    # Read the text file, treating all data as strings
    df = pd.read_csv(txtcsv_path, dtype=str,sep=delimitter)
    # print(df.head())
    # # Save the data to an Excel file, without an index
    df.to_excel(excel_path, index=False)
    print(f"Conversion to excel successful {extract_file_name(excel_path)}")
    return df

######################## Convert from txt to .xlsx
# Initiatilsation
delimitter = "~"
file = r"EQB0363BORD (17).txt"
folder_path = r"C:\Users\ny4007991\OneDrive - Munich Re\Professional\Munich Re\Email Supp\Excel Dumps & Files\PA Lumbermens Cyber Suite (4313) and EPL (3346) inforce and bordereau files - JulyJune 2024"
txtcsv_path = folder_path + "\\" + file
# Convert to Excel
excel_path = folder_path + "\\" + rename_extension(file, new_extension=".xlsx")
excel_df = to_excel(txtcsv_path,excel_path,delimitter)
# # Data grooming
# control_record_df = excel_df.tail(1)
# excel_df = excel_df.drop(excel_df.index[-1]) #drop control record before preprocessing
# excel_df["TX_EFFECTIVE_DATE"] = excel_df["TX_EFFECTIVE_DATE"].str.replace('-','')
# excel_df["COVERAGE_EFFECTIVE_DATE"] = excel_df["COVERAGE_EFFECTIVE_DATE"].str.replace('-','')
# excel_df["COVERAGE_EXPIRATION_DATE"] = excel_df["COVERAGE_EXPIRATION_DATE"].str.replace('-','')
# excel_df["TX_ENTRY_DATE"] = excel_df["TX_ENTRY_DATE"].str.replace('-','')
# excel_df = pd.concat([excel_df,control_record_df]) #add control record back to the dataframe
sys.exit()


######################## Convert from .xlsx to .txt
# Initiatilsation
delimitter = "\t"
file = r"05- Safeco PL Cyber Bordereau - May 2024.xlsx"
folder_path = r"C:\Users\ny4007991\OneDrive - Munich Re\Professional\Munich Re\Email Supp\File Processing\LibertySafeco- June 2024"
excel_path = folder_path + "\\" + file
# Replace 'your_text_file.txt' with the actual path to your text file
new_txtcsv_path = folder_path + "\\" + file.replace(".xlsx",".txt")
excel_df = pd.read_excel(excel_path,sheet_name="Bordereau",dtype=str)
excel_df.to_csv(new_txtcsv_path, sep=delimitter, index=False)
print(f"Conversion to txtcsv successful {extract_file_name(new_txtcsv_path)}")

