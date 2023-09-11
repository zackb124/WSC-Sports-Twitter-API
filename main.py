from df_build import *
from api import *
       
# Check if 'current_date' already exists in the 'Date' column
if current_date not in df['Date'].values:
    new_row = {'Date': current_date, 'Followers': followers_count} # Create a new row as a dictionary
    df = df.append(new_row, ignore_index=True) # Append the new row to the DataFrame
        
print(df)