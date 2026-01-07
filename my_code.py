import pandas as pd
import os

# create a dataframe with coloumn names
data = {
    'Name': ['Rachit', 'Krish', 'Kaushik'],
    'Age': [21, 18, 22],
    'City': ['Noida', 'Surat', 'Vadodara']
}

df = pd.DataFrame(data)

# adding new data to df for v2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'Noida'}
df.loc[len(df.index)] = new_row_loc

# adding new data to df for v3 
#new_row_loc2 = {'Name': 'GF1', 'Age': 20, 'City': 'Noida'}
#df.loc[len(df.index)] = new_row_loc2

# ensure "data" directory at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, "sample_data.csv")

# save the dataframe to a csv file (including column names)
df.to_csv(file_path, index=False)

print(f"Csv File Saved to {file_path}")