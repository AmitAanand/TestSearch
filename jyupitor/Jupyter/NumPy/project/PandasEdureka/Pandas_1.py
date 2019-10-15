import pandas as pd

xyz_web={
    'Day':[1,2,3,4,5,6],
    "Visitors":[1000,700,6000,1000,400,350],
    'Bounce_Rate':[20,20,30,15,10,34]
}

df=pd.DataFrame(xyz_web)
print(df)

##  Slicing     ##
print("----------------Slicing--------------")
print(df.head(2))
print(df.tail(2))

