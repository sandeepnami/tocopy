import pandas as pd

delimitter = "~"
folder_path = r"C:\Users\ny4007991\OneDrive - Munich Re\Professional\Munich Re\Email Supp\File Processing\202407 July\MMG CC0363 June file attached"
# Replace 'your_text_file.txt' with the actual path to your text file
file = r"EQB0363BORD (17).txt"
text_file_path = folder_path + "\\" + file

# Read the text file, treating all data as strings
df = pd.read_csv(text_file_path, dtype=str,sep=delimitter)
# print(df.head())
# Replace 'output.xlsx' with the desired output Excel file name
output_file_path = folder_path + "\\" + file.replace(".txt",".xlsx")
# # Save the data to an Excel file, without an index
df.to_excel(output_file_path, index=False)

print(f"Data from {text_file_path} successfully loaded into {output_file_path}.")
