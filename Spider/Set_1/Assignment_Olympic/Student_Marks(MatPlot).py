# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:04:22 2019

@author: kamit
"""

import pandas as pd
import sys

from Student_Marks_StudentMarks import StudentMarks 

import matplotlib.pyplot as plt # Import the necessary packages and modules
import numpy as np

class StudentMarksPlot:
        
    def semDSMarksPlot(self,df_student_data):
        
        names_list=df_student_data['Name'].unique().tolist()
        
        color_list=['red','blue','green']
        color=0
        
        for nam in names_list:
            df_ds_marks=pd.DataFrame(df_student_data[df_student_data['Name']==nam])
            ### Y-Axis
            maths_marks_list=df_ds_marks['Maths_Marks'].tolist()
            ###  X-Axis
            sem=df_ds_marks['Test'].tolist()
            ## Graph
            plt.plot(sem,maths_marks_list,color=color_list[color], marker='*')
            color+=1
            #####   Design Chart      ########################
            plt.legend(names_list)
            plt.xlabel('Semester')
            plt.ylabel('Marks')
            plt.xlim(0.5,4)
            plt.title("DS Marks per Semester Chart")
            plt.grid(True)
        plt.show()
         
    def barChart(self,df_student_data,studentMarks_obj):

        df_total_marks=pd.DataFrame(df_student_data.groupby('Name').agg(StudentMarks.aggGtotalMarksShape(studentMarks_obj)))
        print(df_total_marks)
        
        ##      List of Names / and subject Marks  ####################
        names_list=df_student_data['Name'].unique().tolist()
        ds_marks_list=df_total_marks['DS_Marks'].tolist()
        maths_marks_list=df_total_marks['Maths_Marks'].tolist()
        col_list=df_total_marks.columns.tolist()
                
        plt.bar(names_list,ds_marks_list,label='DS_Marks')
        plt.bar(names_list,maths_marks_list,label='Maths_Marks')
        plt.legend(col_list)
        plt.show()
            

def main():
   
    studentMarks_obj=StudentMarks()
    student_data=StudentMarks.loadCSV(studentMarks_obj)
    df_student_data=pd.DataFrame(student_data)
    
    SMP=StudentMarksPlot()
    a=True
    
    while a:
        print('''
    1.  Individual DS Marks Semester wise - Plot Chart
    2.  Total Marks subject wise - Bar Chart
    7.  Exit
              ''')    
        try:
                
            choice=int(input('Enter your Choice : '))
            
            if choice==1:
                SMP.semDSMarksPlot(df_student_data)
            elif choice==2:
                SMP.barChart(df_student_data,studentMarks_obj)    
            elif choice==7:
                sys.exit()
            else:
                print("Please enter valid choice as mentioned.........!")
        except ValueError as e:
            print("Please enter only suggested number choice....!")
        
if __name__=='__main__':
    main()