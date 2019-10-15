# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 12:23:35 2019

@author: kamit
"""

import pandas as pd

class StudentMarks:
    
    
    def loadCSV(self):
        student_data=pd.read_csv('E:\\Personal\\DataScience\\Spider\\InputFiles\\student_marks.csv',sep=',')        
        #student_data=pd.read_csv('/home/ec2-user/pythonFiles/InputFiles/student_marks.csv',sep=',')        
        return student_data
   
    
    def aggMarksShape(self):
            agg_shape={
            'DS_Marks':{
                        'Total_DS_Marks':'sum',
                        'Avg_DS_Marks':'mean',
                        'Num_DS_Sem':'count'
                        },
            'Maths_Marks':{
                        'Total_Maths_Marks':'sum',
                        'Avg_Maths_Marks':'mean',
                        'Num_Maths_Sem':'count'
                        }
            }
            return agg_shape
    
    def aggGtotalMarksShape(self):
        agg_gtotal_shape={
                        'DS_Marks':'sum',
                        'Maths_Marks':'sum'
                        
                }
        return agg_gtotal_shape
    
    def ifMaxDuplicate(df_student_data,nam,avg,avg_ifequal,max_student_name,duplicate_flag):
        DS_Math=df_student_data[df_student_data['DS_Marks']==df_student_data['DS_Marks'].max()].iloc[0][2] + df_student_data[df_student_data['DS_Marks']==df_student_data['DS_Marks'].max()].iloc[0][3]    
        avg=DS_Math / 2
        if avg > avg_ifequal:
            avg_ifequal=df_student_data['DS_Marks'].max()
            max_student_name=nam
            duplicate_flag=1
            return max_student_name,duplicate_flag
        else:
            return max_student_name,duplicate_flag
        
    def maxDSMarks(self,student_data,names_list):
                avg=0
                max_marks_ifequal=0
                max_ds_marks=0
                avg_ifequal=0
                duplicate_flag=0
                max_student_name=""
                for nam in names_list:
                    df_student_data=pd.DataFrame(student_data[student_data['Name']==nam]) #.groupby('Name').agg(agg_shape))
                    print("Name : ",nam)
                    #print("DS Max Marks =",df_student_data['DS_Marks'].max(),"/ DS Min Marks =",df_student_data['DS_Marks'].min())
                    #print("Maths Max Marks =",df_student_data['Maths_Marks'].max(),"/ Maths Min Marks =",df_student_data['Maths_Marks'].min())
                    #print("Grand Total = ",df_student_data['DS_Marks'].sum() + df_student_data['Maths_Marks'].sum())
                    print(df_student_data[df_student_data['DS_Marks']==df_student_data['DS_Marks'].max()].iloc[0][2])
                
                    if max_ds_marks == df_student_data['DS_Marks'].max():
                        StudentMarks.ifMaxDuplicate(df_student_data,nam,avg,avg_ifequal,max_student_name,duplicate_flag)
                        
                    elif max_ds_marks < df_student_data['DS_Marks'].max():
                        max_ds_marks=df_student_data['DS_Marks'].max()
                        max_student_name=nam
                        max_marks_ifequal=df_student_data[df_student_data['DS_Marks']==df_student_data['DS_Marks'].max()].iloc[0][2] + df_student_data[df_student_data['DS_Marks']==df_student_data['DS_Marks'].max()].iloc[0][3]    
                        avg_ifequal=max_marks_ifequal / 2
                if duplicate_flag==1:
                    print(max_student_name," has Max DS Marks = ",avg_ifequal)
                else:
                    print(max_student_name," has Max DS Marks = ",max_ds_marks)
    
    #def plotMarks():
        

def main():
    studentmarks=StudentMarks()
    student_data=studentmarks.loadCSV()
    names_list=student_data['Name'].unique().tolist()
    
    print("#########################     Find Name & Max DS Marks obtained       ##############################")
    studentmarks.maxDSMarks(student_data,names_list)
    
    
    print("#########################     Grand Total Subject Wise Marks obtained       ##############################")
    for nam in names_list:
        df_student_data=pd.DataFrame(student_data[student_data['Name']==nam].groupby('Name').agg(studentmarks.aggMarksShape()))
        print(nam)
        print("Total DS Marks= ",df_student_data.iloc[0][0])
        print("Total Maths Marks= ",df_student_data.iloc[0][3])
        print("Grand Total= ",df_student_data.iloc[0][0]+df_student_data.iloc[0][3])
        print("Average Marks= ",df_student_data.iloc[0][1])
        print("Num of Semester Attempted= ",df_student_data.iloc[0][2])
        
    print("#########################     Grand Total Marks obtained       ##############################")
    for nam in names_list:
        df_student_data=pd.DataFrame(student_data[student_data['Name']==nam].groupby('Name').agg(studentmarks.aggGtotalMarksShape()))
        print(nam)
        print("Total Marks = ",df_student_data.iloc[0][0]+df_student_data.iloc[0][1])
    
    
    
if __name__=="__main__":
    main()
