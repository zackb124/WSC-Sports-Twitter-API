from api import *
from datetime import datetime

data = {
    'Followers': [followers_count],
    'Date': [current_date]
}

df = pd.DataFrame(data)