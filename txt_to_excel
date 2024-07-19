import pandas as pd

# Replace 'your_text_file.txt' with the actual path to your text file
text_file_path = 'your_text_file.txt'

# Read the text file, treating all data as strings
df = pd.read_csv(text_file_path, dtype=str)

# Replace 'output.xlsx' with the desired output Excel file name
output_file_path = 'output.xlsx'

# Save the data to an Excel file, without an index
df.to_excel(output_file_path, index=False)

print(f"Data from {text_file_path} successfully loaded into {output_file_path}.")
