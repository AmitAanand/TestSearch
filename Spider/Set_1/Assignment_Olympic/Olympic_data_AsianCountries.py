# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:51:38 2019

@author: kamit
"""
import pandas as pd

import matplotlib.pyplot as plt # Import the necessary packages and modules
import numpy as np

class Asian:
    
    def loadCSV(self):
        #oly_file_data=pd.read_csv('C:\\Users\\kamit\\Desktop\\DataScience\\ML_Project\\InputFiles\\OlympicAthletes.csv')
        oly_file_data=pd.read_csv('/home/ec2-user/pythonFiles/InputFiles/OlympicAthletes.csv',sep=',')
        return oly_file_data
        
    def asianAtlete(self,asian_countries_list,df_oly_file_data):
        
        total=0
        max_madel=0
        max_madel_coountry=""
        
        country_madel_list=[]
        
        for country in asian_countries_list:
            if len(df_oly_file_data[df_oly_file_data['Country']==country])>0:
                #print(df_oly_file_data[df_oly_file_data['Country']==country].head())
                df_group_data=pd.DataFrame(df_oly_file_data[df_oly_file_data['Country']==country].groupby('Country').agg({'Total':'sum'}))
                total+=df_group_data.iloc[0][0]
                country_madel_list.append(df_group_data.iloc[0][0])  
                
                if max_madel < df_group_data.iloc[0][0]:
                    max_madel=df_group_data.iloc[0][0]
                    max_madel_coountry=country
            else:
                country_madel_list.append('0')
                    
                
        print("Total Numbers of Madel won by Asian Countries = ",total)
        print("Maximum Madel won = ",max_madel," by ",max_madel_coountry)
        
        ########  Chart              ###########################
        plt.figure(figsize=(20,4),dpi=70)
        plt.scatter(asian_countries_list,country_madel_list,marker="*")
        plt.xlabel('Countries')
        plt.ylabel('No. of Madels')
        plt.grid(True)
        
        plt.title("Madels Won by Asian Countries")
        
            


def main():
    asian_countries_list=['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh','Bhutan','Brunei','Cambodia','China','Cyprus','Georgia',
'India','Indonesia','Iran','Iraq','Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan','Laos','Lebanon','Malaysia','Maldives','Mongolia',
'Myanmar (formerly Burma)','Nepal','North Korea','Oman','Pakistan','Palestine','Philippines','Qatar','Russia','Saudi Arabia','Singapore','South Korea',
'Sri Lanka','Syria','Taiwan','Tajikistan','Thailand','Timor-Leste','Turkey','Turkmenistan','United Arab Emirates (UAE)','Uzbekistan','Vietnam','Yem',]



    asian=Asian()
    df_oly_file_data=pd.DataFrame(asian.loadCSV())
    
    asian.asianAtlete(asian_countries_list,df_oly_file_data)


if __name__=="__main__":
    main()
    



