import pandas as pd
from glob import glob
import os

path = r'data' 

all_files = glob(os.path.join(path, "*.csv"))

dataframes = []
for f in all_files:
    df = pd.read_csv(f)
    # Filter for 'pink morsel'
    df = df[df['product'] == 'pink morsel'].copy()
    
    # Convert price string (e.g. '$3.00') to float
    df['price'] = df['price'].str.replace('$', '').astype(float)
    df['quantity'] =  df['quantity'].astype(int)
    
    # Create required fields: 'Sales', 'Date', 'Region'
    df['Sales'] = df['price'] * df['quantity']
    df = df.rename(columns={'date': 'Date', 'region': 'Region'})
    
    # Keep only the desired columns
    df = df[['Sales', 'Date', 'Region']]
    dataframes.append(df)

final_df = pd.concat(dataframes, ignore_index=True)

final_df.to_csv('formatted_output.csv', index=False)
print("Data processing complete. Saved to formatted_output.csv")
