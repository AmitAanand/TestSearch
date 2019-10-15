# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:31:30 2019

@author: kamit
"""


import pandas as pd


class MaxAthleteCountry:
    
    def loadCSV(self):
        #oly_file_data=pd.read_csv('C:\\Users\\kamit\\Desktop\\DataScience\\ML_Project\\InputFiles\\OlympicAthletes.csv')
        oly_file_data=pd.read_csv('/home/ec2-user/pythonFiles/InputFiles/OlympicAthletes.csv',sep=',')
        return oly_file_data
    
    def maxAthlete(self,oly_file_data):
        ###############    Exclude Swimming from Sports column    ###############################
        #oly_file_data_exclude = oly_file_data.loc[oly_file_data['Sport']!='Swimming',['Country','Sport']]
        oly_file_data_exclude = oly_file_data.loc[oly_file_data['Sport']!='Swimming']

        ################# Assigning File Data in DataFrame  ###########################################
        df_oly_file_data = pd.DataFrame(oly_file_data_exclude)
        
        df_agg=pd.DataFrame(df_oly_file_data.groupby('Country').agg({'Athlete':'count', 'Total': 'sum'}).rename(columns={'Athlete':'Athlete_Count'}))
 
        ################# Sorting the Aggregated Data and assigning to new Data Frame  ###########################################
        df_agg_sort=pd.DataFrame(df_agg.sort_values(by=['Athlete_Count'],ascending=False).head(1))
        ################# Printing the Result as required OutPut  ###########################################
        print("Maximum count of Athlete Excluding Swimming = ",df_agg_sort.iloc[0][1],"\nCountry Name = ",df_agg_sort.index[0])
        
def main():
    
    maxathletecountry=MaxAthleteCountry()
    oly_file_data=maxathletecountry.loadCSV()
    
    maxathletecountry.maxAthlete(oly_file_data)

if __name__=='__main__':
    main()