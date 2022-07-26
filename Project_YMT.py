import pandas as pd

data = pd.read_csv('/Volumes/LaCie/2022/Code Louisville/purchase_data_exe.csv')
data.head() # Input data files are available in the "../input/" directory.
from datetime import datetime

#df['DateTime'] = pd.to_datetime(df['date'])
df['Year']=[d.split('/')[2] for d in df.date]
df['Month']=[d.split('/')[1] for d in df.date]
df['Day']=[d.split('/')[0] for d in df.date]
df.Year = DFAState.Year.astype('int')
df.Month = df.Month.astype('int')
df.Day = df.Day.astype('int')
df.drop(['date'], axis = 1, inplace= True)
customer_id                 (int64)
product_category            (int64)
payment_method              (int64)
value [USD]               (float64)
time_on_site [Minutes]    (float64)
clicks_in_site              (int64)
Year                        (int64)
Month                       (int64)
Day                         (int64)
dtype: object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.hist(df.payment_method, bins = 2)
plt.xlabel("Payment Method")
plt.ylabel("Frequency")
plt.show()
