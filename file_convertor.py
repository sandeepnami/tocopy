import pandas as pd
from my_regexp_master import rename_extension, extract_file_name

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

# Initialisation
delimitter = "~"
folder_path = r"C:\Users\ny4007991\OneDrive - Munich Re\Professional\Munich Re\Email Supp\File Processing\202407 July\MMG CC0363 June file attached"
# Replace 'your_text_file.txt' with the actual path to your text file
file = r"EQB0363BORD (17).txt"
txtcsv_path = folder_path + "\\" + file



# Main
# Convert to Excel and data grooming
excel_path = folder_path + "\\" + rename_extension(file, new_extension=".xlsx")
excel_df = to_excel(txtcsv_path,excel_path,delimitter)
excel_df["TX_EFFECTIVE_DATE"] = excel_df["TX_EFFECTIVE_DATE"].str.replace('-','')

# Convert to txtcsv
new_txtcsv_path = folder_path + "\\new_" + file
excel_df.to_csv(new_txtcsv_path, sep=delimitter, index=False)
print(f"Conversion to txtcsv successful {extract_file_name(new_txtcsv_path)}")

