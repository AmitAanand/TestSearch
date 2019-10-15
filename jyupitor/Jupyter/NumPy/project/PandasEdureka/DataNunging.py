import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

#music=pd.read_csv("C:\\Users\\kamit\\Desktop\\DataScience\\NumPy\\New folder\\music.csv")
#music.to_html('edu.html')

train=pd.read_csv("C:\\Users\\kamit\\Desktop\\DataScience\\NumPy\\project\\PandasEdureka\\country.csv")

df=train.head(5)
df=df.set_index(['Country Code'])
sd=df.reindex(columns=['2010','2011'])

print(sd)

db=sd.diff(axis=1)
db.plot(kind='bar')
plt.show()