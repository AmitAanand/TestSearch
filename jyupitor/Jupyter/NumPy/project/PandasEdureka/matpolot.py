import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df=pd.DataFrame({ "Day":[1,2,3,4], "Visitors":[200,100,230,300], "Bouce_Rate":[20,45,60,10] })

# Re-name the header
df=df.rename(columns={"Visitors":"Users"})

df.set_index("Day", inplace=True)
print(df)

df.plot()
plt.show()