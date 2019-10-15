# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:06:21 2019

@author: kamit
"""

import pandas as pd


class ConsecutiveWon:
    
    def loadCSV(self):
        #oly_file_data=pd.read_csv('C:\\Users\\kamit\\Desktop\\DataScience\\ML_Project\\InputFiles\\OlympicAthletes.csv')
        oly_file_data=pd.read_csv('/home/ec2-user/pythonFiles/InputFiles/OlympicAthletes.csv',sep=',')
        return oly_file_data
    
            
    def ConsecutiveWonAthlete(self,df_oly_file_data):
                
        year_list=df_oly_file_data['Year'].unique().tolist()
        year_list.sort()
        
        athlete_list=df_oly_file_data['Athlete'].unique().tolist()
        

        medal_won=0
        last_year=0

        for athlete in athlete_list:
            #print("Number of Medals Won By =",athlete)
            medal_won=0
            last_year=0
            
            for year in year_list:
                
                ############  Group by  Athlete with sum total of madels in Data Frame & sorted in second line   ##############
                
                df_group_data=pd.DataFrame(df_oly_file_data[df_oly_file_data['Year']==year].groupby('Athlete').agg({'Total':'sum'}))
                df_group_data_sort=df_group_data.sort_values(by=['Total'],ascending=False)      
                              
                if len(df_group_data_sort[df_group_data_sort.index==athlete])>0:    ## Checking if record exist
                    
                    if medal_won==df_group_data_sort[df_group_data_sort.index==athlete].iloc[0][0]:
                       print("\nAthlete Name= ",athlete,"\nWon Consecutive Years=",last_year," and ",year)
                       print("Number of Madels= ",medal_won)
                       medal_won=df_group_data_sort[df_group_data_sort.index==athlete].iloc[0][0]
                       last_year=year
                    else:
                       medal_won=df_group_data_sort[df_group_data_sort.index==athlete].iloc[0][0]
                       last_year=year
                           
               
                
                
                
def main():
    cw=ConsecutiveWon()
    df_oly_file_data=pd.DataFrame(cw.loadCSV())
    
    cw.ConsecutiveWonAthlete(df_oly_file_data)
    
    
if __name__=="__main__":
    main()


