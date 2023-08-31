from df_build import *
from api import *

new_row = {'Date': current_date, 'Followers': followers_count}

df = df.append(new_row, ignore_index=True)

print(df)