import pandas as pd
from my_regexp_master import rename_extension

# Functions
#convert to excel
def to_excel(textcsv_path,delimitter = "~"):
    # Read the text file, treating all data as strings
    df = pd.read_csv(textcsv_path, dtype=str,sep=delimitter)
    # print(df.head())
    converted_file_path = folder_path + "\\" + rename_extension(file_txtcsv, new_extension=".xlsx")
    # # Save the data to an Excel file, without an index
    df.to_excel(converted_file_path, index=False)

    print(f"Data from {textcsv_path} successfully loaded into {converted_file_path}.")



# Initialisation
delimitter = "~"
folder_path = r"C:\Users\ny4007991\OneDrive - Munich Re\Professional\Munich Re\Email Supp\File Processing\202407 July\MMG CC0363 June file attached"
# Replace 'your_text_file.txt' with the actual path to your text file
file_txtcsv = r"EQB0363BORD (17).txt"
textcsv_path = folder_path + "\\" + file_txtcsv


# Main
to_excel(textcsv_path)

