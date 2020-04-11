import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dateutil.parser import parse

df=pd.read_csv('apr11.csv',
               parse_dates=['dateRep']
              )

af_filter=df['geoId']=='AF'
af=df[af_filter]

pd.set_option('display.max_rows',None)
# af.sort_values('dateRep',ascending=True,inplace=True)
af.sort_index(axis=0,ascending=False, inplace=True)

x=af['dateRep']
y1=af['cases']
y2=af['deaths']

print(af['dateRep'].dtype)
plt.bar(x,y1)
plt.tight_layout()
# plt.show()
