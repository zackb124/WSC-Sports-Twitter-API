from df_build import *
from api import *

for row in df:
    if current_date in df['Date']:
        continue
    else:
        new_row = {'Date': current_date, 'Followers': followers_count}
        df.append(new_row, ignore_index=True)
        
print(df)