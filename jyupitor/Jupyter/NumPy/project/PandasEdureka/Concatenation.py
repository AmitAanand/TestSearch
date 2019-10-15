import pandas as pd


df1=pd.DataFrame({
    "HPI":[80,90,70,60],
    "IntRate":[2,1,2,3],
    "IND_GDP":[50,45,45,67]
},index=[2001,2002,2003,2004])

df2=pd.DataFrame({
    "HPI":[80,90,70,60],
    "IntRate":[80,1,2,3],
    "IND_GDP":[50,45,45,67]
},index=[2005,2006,2007,2008])

concat=pd.concat([df1,df2])

print(concat)