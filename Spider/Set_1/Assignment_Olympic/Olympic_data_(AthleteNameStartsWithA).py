#-*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:21:30 2019

@author: kamit
"""

import pandas as pd
import numpy as np

class AthleteName:
    
    def loadCSV(self):
        #oly_file_data=pd.read_csv('C:\\Users\\kamit\\Desktop\\DataScience\\ML_Project\\InputFiles\\OlympicAthletes.csv')        
        oly_file_data=pd.read_csv('/home/ec2-user/pythonFiles/InputFiles/OlympicAthletes.csv',sep=',')
        return oly_file_data
    
    def nameStartWithA(self,df_oly_file_data):
        
        #df_oly_file_data=df_oly_file_data.replace('',np.nan,inplace=True)
       
        df_oly_file_data=df_oly_file_data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
        df_athelete_name=pd.DataFrame(df_oly_file_data.loc[df_oly_file_data['Athlete'].str.startswith('A'),"Athlete"].values)
        
        print(df_athelete_name)

def main():

    athletename = AthleteName()
    oly_file_data=athletename.loadCSV()
    
    df_oly_file_data=pd.DataFrame(oly_file_data)
    athletename.nameStartWithA(df_oly_file_data)


if __name__=="__main__":
    main()
     
