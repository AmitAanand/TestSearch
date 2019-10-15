import pandas as pd
import numpy as np


class MaxMadelWon:
    
    def loadCSV(self):
        #olympic_data=pd.read_csv('C:\\Users\\kamit\\Desktop\\DataScience\\ML_Project\\InputFiles\\OlympicAthletes.csv')
        olympic_data=pd.read_csv('/home/ec2-user/pythonFiles/InputFiles/OlympicAthletes.csv',sep=',')
        return olympic_data
        
    def topFiveCountry(self,df_oly_data):
        
################# Group By with Country to find the Top 5 countries having max count of Medal ##############################
        group_oly_data=df_oly_data.groupby(['Country'])
        df_agg=pd.DataFrame(group_oly_data.aggregate({'Total':np.sum}))
 
        print(df_agg.sort_values(by=['Total'],ascending=False).head())



def main():

    maxmadelwon = MaxMadelWon()

    df_oly_file_data=pd.DataFrame(maxmadelwon.loadCSV())
    maxmadelwon.topFiveCountry(df_oly_file_data)


if __name__=="__main__":
    main()