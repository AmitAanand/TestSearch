
import pandas as pd

df1=pd.DataFrame({
    "IntRate":[2,1,2,3],
    "IND_GDP":[50,45,45,67]
},index=[2001,2002,2003,2004])

df2=pd.DataFrame({
    "Low_Tier_HPI":[50,45,45,67],
    "Unimployment":[1,3,5,6]
},index=[2001,2003,2004,2005])

joined=df1.join(df2)

print(joined)

