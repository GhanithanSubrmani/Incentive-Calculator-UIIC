# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:43:00 2019

@author: Admin
"""
import pandas as pd

import csv
import os

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

premium_rgstr_PrevYear_filePath =""
premium_rgstr_PrstYear_filePath=""
premium_rgstr_PrevYear = pd.DataFrame
premium_rgstr_PrstYear = pd.DataFrame
premium_rgstr_PrevYear_csv = dict()
premium_rgstr_PrstYear_csv = dict()
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)

pd.set_option('display.expand_frame_repr', False)


def csv_file_import_PrevYear():
    global premium_rgstr_PrevYear_filePath
    premium_rgstr_PrevYear_filePath = filedialog.askopenfilename()
    return

def csv_file_import_PrstYear():
    global premium_rgstr_PrstYear_filePath
    premium_rgstr_PrstYear_filePath = filedialog.askopenfilename()
    return



def calcuate_incentive_Act(x):
    output = 0
    if x > 0 and x <= 5:
        output = 0.25
    elif x > 5 and x <= 10:
        output = 0.5
    elif x >10 and x <=15:
        output = 0.75
    elif x >15 and x <=25:
        output = 1
    elif x >25:
        output = 1.5
    
    return output

def calcuate_incentive_Act_newAgent(x):
    output=0
    if x >= 10 and x < 15:
        output = 0.25
    elif x >= 15 and x < 20:
        output = 0.5
    elif x >=20 and x < 25:
        output = 0.75
    elif x >=25 and x < 35:
        output = 1
    elif x >=35:
        output = 1.5
        
    return output


def calcuate_incentive_Package(x):
    output = 0
    if x > 0 and x <= 5:
        output = 0.50
    elif x > 5 and x <= 10:
        output = 1
    elif x >10 and x <=15:
        output = 2
    elif x >15 and x <=25:
        output = 3
    elif x >25:
        output = 4
    
    return output

def calcuate_incentive_Package_newAgent(x):
    output=0
    if x >= 10 and x < 15:
        output = 0.5
    elif x >= 15 and x < 20:
        output = 1
    elif x >=20 and x < 25:
        output = 2
    elif x >=25 and x < 35:
        output = 3
    elif x >=35:
        output = 4
        
    return output



#
#    FUNCTION TO PROCESS INCENTIVE
#    


def process_incentive():
    global premium_rgstr_PrevYear_csv
    global premium_rgstr_PrstYear_csv
    global premium_rgstr_PrevYear
    global premium_rgstr_PrstYear
    premium_rgstr_PrevYear_csv = dict()
    premium_rgstr_PrstYear_csv = dict()
    premium_rgstr_PrevYear = pd.DataFrame
    premium_rgstr_PrstYear = pd.DataFrame
    motor = True
    start_award = True
#   load PrevYear register    
    premium_rgstr_PrevYear_full_data = pd.read_csv(premium_rgstr_PrevYear_filePath,dayfirst=True, parse_dates = True)
    premium_rgstr_PrevYear_csv= csv.DictReader(open(premium_rgstr_PrevYear_filePath))
    
    premium_rgstr_PrevYear = premium_rgstr_PrevYear_full_data.filter(['Policy Number','Insured Name','Effect Date','Expiry Date','Department','Sum Insured','Chassis Number','Engine Number','Registration Number','Agent/Br.Cd Biz Src Cd','Policy Source','Total','Endorsement Number','TP Premium'], axis = 1)
    
#        
#    
#   load PrstYear Register
    premium_rgstr_PrstYear_full_data = pd.read_csv(premium_rgstr_PrstYear_filePath,dayfirst=1, parse_dates = True)
    premium_rgstr_PrstYear_csv = csv.DictReader(open(premium_rgstr_PrstYear_filePath))

    premium_rgstr_PrstYear = premium_rgstr_PrstYear_full_data.filter(['Policy Number','Insured Name','Effect Date','Expiry Date','Department','Sum Insured','Chassis Number','Engine Number','Registration Number','Agent/Br.Cd Biz Src Cd','Policy Source','Total','Endorsement Number','TP Premium'], axis = 1)    
    
#   #for debugging 
#    root1= tk.Tk()
#    root1.title('Premium Register PrevYear')
#    # width x height + x_offset + y_offset:
#    root1.geometry("400x400+30+30") 
#    
#    scrollbar1 = tk.Scrollbar(root1, orient="vertical") 
#    scrollbar1.pack( side = tk.RIGHT, fill = tk.Y ) 
#    scrollbar1b = tk.Scrollbar(root1, orient="horizontal") 
#    scrollbar1b.pack( side = tk.BOTTOM, fill = tk.X ) 
#    mylist1 = tk.Listbox(root1, yscrollcommand = scrollbar1.set, xscrollcommand = scrollbar1b.set ) 
##   DON'T DELETE BELOW CODE
##    for row1 in premium_rgstr_PrevYear_csv:
###        print (row1["Registration Number"])
##        mylist1.insert(tk.END, row1 )
#  
#        
#    for i,row12 in premium_rgstr_PrevYear.iterrows():
#        mylist1.insert(tk.END, row12)
#
#    mylist1.pack( expand =1, fill = tk.BOTH ) 
#    scrollbar1.config( command = mylist1.yview ) 
#    scrollbar1b.config( command = mylist1.xview ) 
#    
##   Display premium register of  PrstYear     
#
#    root2= tk.Tk()
#    root2.title('Premium Register PrstYear')
#    # width x height + x_offset + y_offset:
#    root2.geometry("400x400+30+30") 
#    scrollbar2 = tk.Scrollbar(root2, orient="vertical") 
#    scrollbar2.pack( side = tk.RIGHT, fill = tk.Y ) 
#    scrollbar2b = tk.Scrollbar(root2, orient="horizontal") 
#    scrollbar2b.pack( side = tk.BOTTOM, fill = tk.X ) 
#    mylist2 = tk.Listbox(root2, yscrollcommand = scrollbar2.set, xscrollcommand = scrollbar2b.set ) 
##   DON'T DELETE BELOW CODE
##    for row2 in premium_rgstr_PrstYear_csv:
##        mylist2.insert(tk.END, row2 )
###    mylist2.insert(tk.END, premium_rgstr_PrstYear)
#    for i,row22 in premium_rgstr_PrstYear.iterrows():
#        mylist2.insert(tk.END, row22)
##        print(row22)
#
#    mylist2.pack(  expand =1, fill = tk.BOTH ) 
#    scrollbar2.config( command = mylist2.yview )
#    scrollbar2b.config( command = mylist2.xview ) 
#    
#    print(premium_rgstr_PrstYear.info())
    
#    
#    FIND LIST OF UNIQUE AGENTS
#    
#    
        


#                                                                                  
#   #    #  ####  #####  ####  #####               ####  #####   ##   #####  ##### 
#   ##  ## #    #   #   #    # #    #             #        #    #  #  #    #   #   
#   # ## # #    #   #   #    # #    #    #####     ####    #   #    # #    #   #   
#   #    # #    #   #   #    # #####                   #   #   ###### #####    #   
#   #    # #    #   #   #    # #   #              #    #   #   #    # #   #    #   
#   #    #  ####    #    ####  #    #              ####    #   #    # #    #   #   
#                                                                                  
                                                                                     
    if motor == True:         
    #    
    #    
    #    PREVIOUS YEAR
    #    
    #    
    
#        Filtering Motor LOB
        is_motor_PrevYear = premium_rgstr_PrevYear['Department']== 'Motor'
        premium_rgstr_PrevYear_inter= premium_rgstr_PrevYear[is_motor_PrevYear]
#        remove polcies other than A, B , C and D types
        is_motor_PrevYear_basic = premium_rgstr_PrevYear_inter['Registration Number'].notnull()
        premium_rgstr_PrevYear_motor= premium_rgstr_PrevYear_inter[is_motor_PrevYear_basic]
        
#        introduce column to count polcies for each agent by assigning a count value to every policy 
        premium_rgstr_PrevYear_motor['Previous year Policy Count'] = 1
#        condition the date datatypes to UTC format
        if 'Collection Date' in premium_rgstr_PrevYear_motor.columns:
            premium_rgstr_PrevYear_motor['Collection Date'] = pd.to_datetime(premium_rgstr_PrevYear_motor['Collection Date'],utc=True)
        premium_rgstr_PrevYear_motor['Effect Date'] = pd.to_datetime(premium_rgstr_PrevYear_motor['Effect Date'],utc=True)
        premium_rgstr_PrevYear_motor['Expiry Date'] = pd.to_datetime(premium_rgstr_PrevYear_motor['Expiry Date'],utc=True)
        premium_rgstr_PrevYear_motor['Insured Name'] = premium_rgstr_PrevYear_motor['Insured Name'].str.replace(',','')
#        remove trailing unusable information in the agent column
        premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd'] = premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd'].str.replace(' -- NA -- NA','')
#        just after thought
#        sublist_column_index=['Agent Name', 'Agent Code', 'Package PrevYear', 'Package PrstYear' , 'Act PrevYear', 'Act PrstYear', 'Growth', 'Eligibilty']
        
#        creating array of dataframes to filter agent wise details
        sublist_agents_prevYear={}
        list_agent_PrevYear= premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd'].unique().tolist()
    #    messagebox.showinfo("Agent Count", "there are " + str(len(list_agent_PrevYear)) + " unique number of agents in our office.")
        print("there are " + str(len(list_agent_PrevYear)) + " unique number of agents in our office.")
        for agent in list_agent_PrevYear:
            print (agent)
            is_agent = premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd']== agent
            sublist_agents_prevYear[agent]= premium_rgstr_PrevYear_motor[is_agent]
        
#        printing agentwise details in a different folder 
        os.chdir(os.path.dirname(premium_rgstr_PrevYear_filePath))
        if os.path.isdir('Previous_Year_AgentWise_premium_register') == 0:
            os.makedirs('Previous_Year_AgentWise_premium_register')   
            os.chdir('Previous_Year_AgentWise_premium_register')
        else:
            os.chdir('Previous_Year_AgentWise_premium_register')
        for key in sublist_agents_prevYear.keys():
    #        print("\n" +"="*40)
    #        print(key)
    #        print("-"*40)
            print(sublist_agents_prevYear[key]['Expiry Date'])
            sublist_agents_prevYear[key].to_csv(key+".csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        
        
#        grouping data agentwise without splitting ACT and Package
        summed_premium_rgstr_prevYear_motor = premium_rgstr_PrevYear_motor.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_prevYear_motor.fillna(0)
        summed_premium_rgstr_prevYear_motor.to_csv("00_summed_premium_rgstr_prevYear_motor.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
#       filtering ACT policies 
        is_package_act_prevYear = premium_rgstr_PrevYear_motor['TP Premium']== premium_rgstr_PrevYear_motor['Total']
        premium_rgstr_prevYear_motor_act = premium_rgstr_PrevYear_motor[is_package_act_prevYear]
        premium_rgstr_prevYear_motor_act.rename(columns={'Total':'Previous Year Total Act Premium', 'TP Premium':'Previous Year Total Act TP Premium', 'Previous year Policy Count': 'Previous year Act Policy Count'}, inplace=True)
        summed_premium_rgstr_prevYear_motor_act = premium_rgstr_prevYear_motor_act.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_prevYear_motor_act.fillna(0)
        summed_premium_rgstr_prevYear_motor_act.to_csv("00_summed_premium_rgstr_prevYear_motor_act.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
#        filtering package policies
        is_package_Package_prevYear = premium_rgstr_PrevYear_motor['TP Premium']!= premium_rgstr_PrevYear_motor['Total']
        premium_rgstr_prevYear_motor_package = premium_rgstr_PrevYear_motor[is_package_Package_prevYear]
        premium_rgstr_prevYear_motor_package.rename(columns={'Total':'Previous Year Total Package Premium', 'TP Premium':'Previous Year Total Package TP Premium', 'Previous year Policy Count': 'Previous year Package Policy Count'}, inplace=True)
        summed_premium_rgstr_prevYear_motor_package = premium_rgstr_prevYear_motor_package.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_prevYear_motor_package.fillna(0)
        summed_premium_rgstr_prevYear_motor_package.to_csv("00_summed_premium_rgstr_prevYear_motor_package.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        os.chdir("..")
        premium_rgstr_PrevYear_motor.to_csv("previous_year_data.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
    #    
    #    PRESENT YEAR
    #    
    #    
#        Filtering Motor LOB        
        is_motor_PrstYear = premium_rgstr_PrstYear['Department']== 'Motor'
        premium_rgstr_PrstYear_inter= premium_rgstr_PrstYear[is_motor_PrstYear]
#        remove polcies other than A, B , C and D types
        is_motor_PrstYear_basic = premium_rgstr_PrstYear_inter['Registration Number'].notnull()
        premium_rgstr_PrstYear_motor= premium_rgstr_PrstYear_inter[is_motor_PrstYear_basic]
        
#        introduce column to count polcies for each agent by assigning a count value to every policy 
        premium_rgstr_PrstYear_motor['Present year Policy Count'] = 1
        
#        condition the date datatypes to UTC format
        if 'Collection Date' in premium_rgstr_PrstYear_motor.columns:
            premium_rgstr_PrstYear_motor['Collection Date'] = pd.to_datetime(premium_rgstr_PrstYear_motor['Collection Date'],utc=True)
        premium_rgstr_PrstYear_motor['Effect Date'] = pd.to_datetime(premium_rgstr_PrstYear_motor['Effect Date'],utc=True)
        premium_rgstr_PrstYear_motor['Expiry Date'] = pd.to_datetime(premium_rgstr_PrstYear_motor['Expiry Date'],utc=True)
        premium_rgstr_PrstYear_motor['Insured Name'] = premium_rgstr_PrstYear_motor['Insured Name'].str.replace(',','')
        premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd'] = premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd'].str.replace(' -- NA -- NA','')
    #    print(premium_rgstr_PrstYear_motor.info())
    #    premium_rgstr_PrstYear_motor['Transfer'] = 'Newly Acquired'
    #    print(premium_rgstr_PrstYear_motor.info())
    #    To find transfer of policies between agents
    
#        filtering transfered policies between agents
        premium_rgstr_PrevYear_motor_Transfer = premium_rgstr_PrevYear_motor.copy()
    #    premium_rgstr_PrevYear_motor_Transfer.set_index(['Registration Number'], inplace=True)
        premium_rgstr_PrevYear_motor_Transfer.rename(columns={'Insured Name':'Previous Year Insured Name',
                                                         'Policy Number':'Previous Year Policy Number',
                                                         'Agent/Br.Cd Biz Src Cd':'Previous Year Agent'}, inplace=True)
    #    premium_rgstr_PrevYear_motor_Transfer.set_index(['Previous Year Insured Name',
    #                                                                   'Previous Year Policy Number',
    #                                                                   'Registration Number',
    #                                                                   'Previous Year Agent'], inplace = True)
        premium_rgstr_PrstYear_motor_Transfer = premium_rgstr_PrstYear_motor.copy()
    #    premium_rgstr_PrstYear_motor_Transfer.set_index(['Registration Number'], inplace=True)
        premium_rgstr_PrstYear_motor_Transfer.rename(columns={'Insured Name':'Present Year Insured Name',
                                                         'Policy Number':'Present Year Policy Number',
                                                         'Agent/Br.Cd Biz Src Cd':'Present Year Agent'}, inplace=True)
        
        print(premium_rgstr_PrevYear_motor_Transfer.info())
    #    
        print(premium_rgstr_PrstYear_motor_Transfer.info())
        
        Transfer_check= pd.merge(premium_rgstr_PrevYear_motor_Transfer[['Previous Year Insured Name',
                                                                       'Previous Year Policy Number',
                                                                       'Registration Number',
                                                                       'Previous Year Agent']],
                                 premium_rgstr_PrstYear_motor_Transfer[['Present Year Insured Name',
                                                                       'Present Year Policy Number',
                                                                       'Registration Number',
                                                                       'Present Year Agent']],
                                                                       on = 'Registration Number',
                                                                       how = 'inner')
        
#        conditioning the transfered policies list 
        is_motor_old = Transfer_check['Registration Number']!= 'NEW'
        Transfer_check= Transfer_check[is_motor_old]
     
    #    Transfer_check = Transfer_check[Transfer_check['Registration Number'].str.contains('') == False ]
        is_motor_basic = Transfer_check['Registration Number'].notnull()
        Transfer_check= Transfer_check[is_motor_basic]
        
        is_not_same_agent = Transfer_check['Previous Year Agent'] != Transfer_check['Present Year Agent']
        Transfer_check= Transfer_check[is_not_same_agent]
        
        Transfer_check['Transfer'] = 'Transfered'
        Transfer_check.to_csv("Transfered Policies.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')    
        
#        removing transfered policies form the list to calculate incentive
        premium_rgstr_PrstYear_motor = pd.merge(premium_rgstr_PrstYear_motor,
                                                Transfer_check[['Transfer','Registration Number']],
                                                on = 'Registration Number',
                                                how = 'left').fillna('Newly Acquired')
        
        
        
        premium_rgstr_PrstYear_motor.to_csv("present_year_data_with_transfer_tag.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        is_transfered = premium_rgstr_PrstYear_motor['Transfer'] == 'Transfered'
        premium_rgstr_PrstYear_motor.drop(premium_rgstr_PrstYear_motor[is_transfered].index, inplace = True)
        premium_rgstr_PrstYear_motor.to_csv("present_year_data_without_transfered_policies.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        
        print(premium_rgstr_PrstYear_motor.info())
        
#        creating array of dataframes to filter agent wise details
        sublist_column_index=['Agent Name', 'Agent Code', 'Package PrevYear', 'Package PrstYear' , 'Act PrevYear', 'Act PrstYear', 'Growth', 'Eligibilty']
        sublist_agents_prstYear={}
        list_agent_PrstYear= premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd'].unique().tolist()
    #    messagebox.showinfo("Agent Count", "there are " + str(len(list_agent_PrstYear)) + " unique number of agents in our office.")
        print("there are " + str(len(list_agent_PrstYear)) + " unique number of agents in our office.")
        for agent in list_agent_PrstYear:
            print (agent)
            is_agent = premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd']== agent
            sublist_agents_prstYear[agent]= premium_rgstr_PrstYear_motor[is_agent]
       
#        printing agentwise details in a different folder         
        os.chdir(os.path.dirname(premium_rgstr_PrstYear_filePath))
        if os.path.isdir('Present_Year_AgentWise_premium_register') == 0:
            os.makedirs('Present_Year_AgentWise_premium_register')   
            os.chdir('Present_Year_AgentWise_premium_register')
        else:
            os.chdir('Present_Year_AgentWise_premium_register')
        for key in sublist_agents_prstYear.keys():
    #        print("\n" +"="*40)
    #        print(key)
    #        print("-"*40)
            print(sublist_agents_prstYear[key]['Expiry Date'])
            sublist_agents_prstYear[key].to_csv(key+".csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
            
    #    premium_rgstr_PrstYear_motor
    #    premium_rgstr_PrevYear_motor
        Calc_Incentive_No_transfer_PrstYear = pd.DataFrame(index = list_agent_PrstYear, columns = sublist_column_index )     
        
        
#        grouping data agentwise without splitting ACT and Package        
        summed_premium_rgstr_prstYear_motor=premium_rgstr_PrstYear_motor.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_prstYear_motor.fillna(0)
        summed_premium_rgstr_prstYear_motor.to_csv("00_summed_premium_rgstr_prstYear_motor.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')

#       filtering ACT policies         
        is_package_act_prstYear = premium_rgstr_PrstYear_motor['TP Premium']== premium_rgstr_PrstYear_motor['Total']
        premium_rgstr_prstYear_motor_act = premium_rgstr_PrstYear_motor[is_package_act_prstYear]
        premium_rgstr_prstYear_motor_act.rename(columns={'Total':'Present Year Total Act Premium', 'TP Premium':'Present Year Total Act TP Premium', 'Present year Policy Count': 'Present year Act Policy Count'}, inplace=True)
        summed_premium_rgstr_prstYear_motor_act = premium_rgstr_prstYear_motor_act.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_prstYear_motor_act.fillna(0)
        summed_premium_rgstr_prstYear_motor_act.to_csv("00_summed_premium_rgstr_prstYear_motor_act.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
#       filtering package policies         
        is_package_Package_prstYear = premium_rgstr_PrstYear_motor['TP Premium']!= premium_rgstr_PrstYear_motor['Total']
        premium_rgstr_prstYear_motor_package = premium_rgstr_PrstYear_motor[is_package_Package_prstYear]
        premium_rgstr_prstYear_motor_package.rename(columns={'Total':'Present Year Total Package Premium', 'TP Premium':'Present Year Total Package TP Premium', 'Present year Policy Count': 'Present year Package Policy Count'}, inplace=True)
        summed_premium_rgstr_prstYear_motor_package = premium_rgstr_prstYear_motor_package.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_prstYear_motor_package.fillna(0)
        summed_premium_rgstr_prstYear_motor_package.to_csv("00_summed_premium_rgstr_prstYear_motor_package.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
#        merging previous year data and present year data of ACT policies
        
    #    merged_Act_data= pd.merge(summed_premium_rgstr_prstYear_motor_act,summed_premium_rgstr_prevYear_motor_act,left_index=True, right_index=True)
        merged_Act_data = summed_premium_rgstr_prstYear_motor_act.combine_first(summed_premium_rgstr_prevYear_motor_act).fillna(0)
        merged_Act_data['Present year Act Policy Count'] = merged_Act_data['Present year Act Policy Count'].add(0,fill_value=0)
        merged_Act_data['Previous year Act Policy Count'] = merged_Act_data['Previous year Act Policy Count'].add(0,fill_value=0)
        merged_Act_data['Growth for Act'] = merged_Act_data['Present Year Total Act Premium'].sub(merged_Act_data['Previous Year Total Act Premium'],fill_value=0)
        merged_Act_data['Growth for Act in %'] = merged_Act_data['Growth for Act'].truediv(merged_Act_data['Previous Year Total Act Premium'],fill_value=0) *100
        merged_Act_data['Incentive for Act in %'] = merged_Act_data['Growth for Act in %'].apply( calcuate_incentive_Act)
        for  index,row in merged_Act_data.iterrows():
            if row['Previous year Act Policy Count'] == 0:
                row['Incentive for Act in %'] = calcuate_incentive_Act_newAgent(row['Present year Act Policy Count'])
    #        row['Incentive for Act in %'] = calcuate_incentive_Act(row['Growth for Act in %'])
        
#        calculate incentive for ACT policies
        merged_Act_data['Incentive for Act'] = merged_Act_data['Incentive for Act in %'] * merged_Act_data['Present Year Total Act Premium'] /100
        merged_Act_data.to_csv("01_merged_act_data.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
    
    
#        merging previous year data and present year data of package policies    
        
    #    merged_Package_data= pd.merge(summed_premium_rgstr_prstYear_motor_package,summed_premium_rgstr_prevYear_motor_package,left_index=True, right_index=True)
        merged_Package_data = summed_premium_rgstr_prstYear_motor_package.combine_first(summed_premium_rgstr_prevYear_motor_package).fillna(0)
        merged_Package_data['Present year Package Policy Count'] = merged_Package_data['Present year Package Policy Count'].add(0,fill_value=0)
        merged_Package_data['Previous year Package Policy Count'] = merged_Package_data['Previous year Package Policy Count'].add(0,fill_value=0)
        merged_Package_data['Growth for Package'] = merged_Package_data['Present Year Total Package Premium'].sub(merged_Package_data['Previous Year Total Package Premium'],fill_value=0)
        merged_Package_data['Growth for Package in %'] = merged_Package_data['Growth for Package'].truediv(merged_Package_data['Previous Year Total Package Premium'],fill_value=0) *100
        merged_Package_data['Incentive for Package in %'] = merged_Package_data['Growth for Package in %'].apply( calcuate_incentive_Package)
        for  index,row in merged_Package_data.iterrows():
    #        print(row['Previous year Package Policy Count'])
            if row['Previous year Package Policy Count'] == 0:
                row['Incentive for Package in %'] = calcuate_incentive_Package_newAgent(row['Present year Package Policy Count'])
    #        row['Incentive for Package in %'] = calcuate_incentive_Package(row['Growth for Package in %'])
        
#        calculate incentive for package policies
        merged_Package_data['Incentive for Package'] = merged_Package_data['Incentive for Package in %'] * merged_Package_data['Present Year Total Package Premium'] /100
        merged_Package_data.to_csv("01_merged_package_data.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        
#        combine both the incentive data for ACT and Package policies and arrive at total incentive
        os.chdir("..")
        combined_data= merged_Package_data.combine_first(merged_Act_data).fillna(0)
        combined_data['Previous year Policy Count'] = combined_data['Previous year Act Policy Count'].add(combined_data['Previous year Package Policy Count'],fill_value=0)
        combined_data['Present year Policy Count'] = combined_data['Present year Act Policy Count'].add(combined_data['Present year Package Policy Count'],fill_value=0)
        
        combined_data['Present year Total Premium'] = combined_data['Present Year Total Act Premium'] + combined_data['Present Year Total Package Premium']
        combined_data['Previous year Total Premium'] = combined_data['Previous Year Total Act Premium'] + combined_data['Previous Year Total Package Premium']
        combined_data['New Agent'] = ''
        for  index,row in combined_data.iterrows():
            if row['Previous year Policy Count'] == 0:
                combined_data.at[index,'New Agent'] ="New Agent"
                print(row['New Agent'])
        print(combined_data['New Agent'])
        combined_data['Total Incentive'] = combined_data['Incentive for Package'] + combined_data['Incentive for Act']
        combined_data['TDS'] = combined_data['Total Incentive'] * 5 / 100
        combined_data['Total Incentive to be Paid'] = combined_data['Total Incentive'] - combined_data['TDS']
        combined_data.to_csv("00_combined_incentive_data.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        


#                                                                      
#   #    #  ####  #####  ####  #####              ###### #    # #####  
#   ##  ## #    #   #   #    # #    #             #      ##   # #    # 
#   # ## # #    #   #   #    # #    #    #####    #####  # #  # #    # 
#   #    # #    #   #   #    # #####              #      #  # # #    # 
#   #    # #    #   #   #    # #   #              #      #   ## #    # 
#   #    #  ####    #    ####  #    #             ###### #    # #####  
#                                                                      
   

#                                                                                                                     
#    ####  #####   ##   #####       #####  ###### #    #   ##   #####  #####      ####  #####   ##   #####  ##### 
#   #        #    #  #  #    #      #    # #      #    #  #  #  #    # #    #    #        #    #  #  #    #   #   
#    ####    #   #    # #    #      #    # #####  #    # #    # #    # #    #     ####    #   #    # #    #   #   
#        #   #   ###### #####       #####  #      # ## # ###### #####  #    #         #   #   ###### #####    #   
#   #    #   #   #    # #   #       #   #  #      ##  ## #    # #   #  #    #    #    #   #   #    # #   #    #   
#    ####    #   #    # #    #      #    # ###### #    # #    # #    # #####      ####    #   #    # #    #   #   
#                                                                                                                     

    if start_award == True:
        

        premium_rgstr_PrevYear['Agent/Br.Cd Biz Src Cd'] = premium_rgstr_PrevYear['Agent/Br.Cd Biz Src Cd'].str.replace(' -- NA -- NA','')
        premium_rgstr_PrstYear['Agent/Br.Cd Biz Src Cd'] = premium_rgstr_PrstYear['Agent/Br.Cd Biz Src Cd'].str.replace(' -- NA -- NA','')
        

        
        premium_rgstr_PrevYear_star = premium_rgstr_PrevYear.copy()
        premium_rgstr_PrstYear_star = premium_rgstr_PrstYear.copy()
        
        premium_rgstr_PrevYear_star.drop(['Sum Insured','TP Premium','Endorsement Number'], axis = 1, inplace = True)
        
        premium_rgstr_PrstYear_star.drop(['Sum Insured','TP Premium','Endorsement Number'], axis = 1, inplace = True)
        
        
        
        summed_premium_rgstr_PrevYear_star=premium_rgstr_PrevYear_star.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_PrevYear_star.fillna(0)
        summed_premium_rgstr_PrevYear_star.rename(columns={'Total': "Grand Total Previous Year"}, inplace=True)
        
#        calculating total department wise
        departmant_wise_prevYear={}
        List_of_departments_prevYear = premium_rgstr_PrevYear_star['Department'].unique().tolist()
    #    messagebox.showinfo("Agent Count", "there are " + str(len(list_agent_PrevYear)) + " unique number of agents in our office.")
        print("there are " + str(len(List_of_departments_prevYear)) + " number of departments underwritten in our office.")
        for departments in List_of_departments_prevYear:
            print (departments)
            is_department = premium_rgstr_PrevYear_star['Department']== departments
            departmant_wise_prevYear[departments] = premium_rgstr_PrevYear_star[is_department]
            departmant_wise_prevYear[departments] = departmant_wise_prevYear[departments].groupby('Agent/Br.Cd Biz Src Cd').sum()
            departmant_wise_prevYear[departments].fillna(0)
            departmant_wise_prevYear[departments].rename(columns={'Total': departments + " Total Previous Year"}, inplace=True)
            summed_premium_rgstr_PrevYear_star = pd.merge(summed_premium_rgstr_PrevYear_star,
                                                departmant_wise_prevYear[departments][[departments + " Total Previous Year"]],
                                                on = 'Agent/Br.Cd Biz Src Cd',
                                                how = 'left').fillna(0)

            
        summed_premium_rgstr_PrevYear_star.to_csv("00_summed_premium_rgstr_prevYear_star.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')

        summed_premium_rgstr_PrstYear_star=premium_rgstr_PrstYear_star.groupby('Agent/Br.Cd Biz Src Cd').sum()
        summed_premium_rgstr_PrstYear_star.fillna(0)
        summed_premium_rgstr_PrstYear_star.rename(columns={'Total': "Grand Total Present Year"}, inplace=True)
        
        
        
        #        calculating total department wise
        departmant_wise_prsntYear={}
        List_of_departments_prsntYear= premium_rgstr_PrstYear_star['Department'].unique().tolist()
    #    messagebox.showinfo("Agent Count", "there are " + str(len(list_agent_PrevYear)) + " unique number of agents in our office.")
        print("there are " + str(len(List_of_departments_prsntYear)) + " number of departments underwritten in our office.")
        for departments in List_of_departments_prsntYear:
            print (departments)
            is_department = premium_rgstr_PrstYear_star['Department']== departments
            departmant_wise_prsntYear[departments] = premium_rgstr_PrstYear_star[is_department]
            departmant_wise_prsntYear[departments] = departmant_wise_prsntYear[departments].groupby('Agent/Br.Cd Biz Src Cd').sum()
            departmant_wise_prsntYear[departments].fillna(0)
            departmant_wise_prsntYear[departments].rename(columns={'Total': departments + " Total Present Year"}, inplace=True)
            summed_premium_rgstr_PrstYear_star = pd.merge(summed_premium_rgstr_PrstYear_star,
                                                departmant_wise_prsntYear[departments][[departments + " Total Present Year"]],
                                                on = 'Agent/Br.Cd Biz Src Cd',
                                                how = 'left').fillna(0)

        
        summed_premium_rgstr_PrstYear_star.to_csv("00_summed_premium_rgstr_prstYear_star.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        merged_premium_rgstr_star = pd.merge(summed_premium_rgstr_PrstYear_star,
                                                summed_premium_rgstr_PrevYear_star,
                                                on = 'Agent/Br.Cd Biz Src Cd',
                                                how = 'left').fillna(0)
        merged_premium_rgstr_star.to_csv("00_merged_premium_rgstr_star.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
        
        
        List_of_departments_prsntYear_1 = ['Aviation','Engineering','Fire','Health','Liability','Marine Cargo','Marine Hull','Miscellaneous','Motor','Package','Personal Accident','Property Insurance','Social and Rural','Travel']
        for departments in List_of_departments_prsntYear_1:
            if (departments + " Total Present Year") in merged_premium_rgstr_star.columns:
#                do nothing
                print(departments + " Total Present Year ok")
            else:
                merged_premium_rgstr_star[departments + " Total Present Year"] = 0
                
                
        merged_premium_rgstr_star.drop(['Health Total Previous Year','Motor Total Previous Year','Social and Rural Total Previous Year','Personal Accident Total Previous Year','Marine Cargo Total Previous Year','Liability Total Previous Year','Package Total Previous Year','Fire Total Previous Year','Property Insurance Total Previous Year','Engineering Total Previous Year'], axis = 1, inplace = True)

        merged_premium_rgstr_star['Other Misc'] = merged_premium_rgstr_star['Personal Accident Total Present Year'].add(merged_premium_rgstr_star['Liability Total Present Year'],fill_value=0)
        merged_premium_rgstr_star['Other Misc'] = merged_premium_rgstr_star['Other Misc'].add(merged_premium_rgstr_star['Package Total Present Year'],fill_value=0)
        merged_premium_rgstr_star['Other Misc'] = merged_premium_rgstr_star['Other Misc'].add(merged_premium_rgstr_star['Property Insurance Total Present Year'],fill_value=0)
        
        merged_premium_rgstr_star.drop(['Personal Accident Total Present Year','Liability Total Present Year','Package Total Present Year','Property Insurance Total Present Year'], axis = 1, inplace = True)
        

                           
        
        merged_premium_rgstr_star['Fire %'] = merged_premium_rgstr_star['Fire Total Present Year'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        merged_premium_rgstr_star['Marine %'] = merged_premium_rgstr_star['Marine Cargo Total Present Year'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        merged_premium_rgstr_star['Health %'] = merged_premium_rgstr_star['Health Total Present Year'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        merged_premium_rgstr_star['Motor %'] = merged_premium_rgstr_star['Motor Total Present Year'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        merged_premium_rgstr_star['Engg %'] = merged_premium_rgstr_star['Engineering Total Present Year'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        merged_premium_rgstr_star['Social %'] = merged_premium_rgstr_star['Social and Rural Total Present Year'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        merged_premium_rgstr_star['Other Misc %'] = merged_premium_rgstr_star['Other Misc'].truediv(merged_premium_rgstr_star['Grand Total Present Year'],fill_value=0) *100
        
        merged_Package_data['Growth for Package'] = merged_Package_data['Present Year Total Package Premium'].sub(merged_Package_data['Previous Year Total Package Premium'],fill_value=0)
                
        merged_premium_rgstr_star['Growth from previous year'] = merged_premium_rgstr_star['Grand Total Present Year'].sub(merged_premium_rgstr_star['Grand Total Previous Year'],fill_value=0)
        merged_premium_rgstr_star['Growth from previous year in %'] = merged_premium_rgstr_star['Growth from previous year'].truediv(merged_premium_rgstr_star['Grand Total Previous Year'],fill_value=0) *100
        
        merged_premium_rgstr_star.to_csv("star_calculation.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')

#                                                                                                         
#    ####  #####   ##   #####     #####  ###### #    #   ##   #####  #####     ###### #    # #####  
#   #        #    #  #  #    #    #    # #      #    #  #  #  #    # #    #    #      ##   # #    # 
#    ####    #   #    # #    #    #    # #####  #    # #    # #    # #    #    #####  # #  # #    # 
#        #   #   ###### #####     #####  #      # ## # ###### #####  #    #    #      #  # # #    # 
#   #    #   #   #    # #   #     #   #  #      ##  ## #    # #   #  #    #    #      #   ## #    # 
#    ####    #   #    # #    #    #    # ###### #    # #    # #    # #####     ###### #    # #####  
#                                                                                                         



#                                                                       
#   ###### # #####  ######              ####  #####   ##   #####  ##### 
#   #      # #    # #                  #        #    #  #  #    #   #   
#   #####  # #    # #####     #####     ####    #   #    # #    #   #   
#   #      # #####  #                       #   #   ###### #####    #   
#   #      # #   #  #                  #    #   #   #    # #   #    #   
#   #      # #    # ######              ####    #   #    # #    #   #   
#                                                                       

       
        
   
        
        
        
        
        

#                                                           
#   ###### # #####  ######             ###### #    # #####  
#   #      # #    # #                  #      ##   # #    # 
#   #####  # #    # #####     #####    #####  # #  # #    # 
#   #      # #####  #                  #      #  # # #    # 
#   #      # #   #  #                  #      #   ## #    # 
#   #      # #    # ######             ###### #    # #####  
#                                                           
        
        
        
        
           
    messagebox.showinfo("Completed","Process has been completed")
    
    return

#
#    MAIN FUNCTION
#           
        
root= tk.Tk()
root.title('Motor Incentive Calculator')
#root.config(bg='lightblue' font=('times',12,'bold'))
# width x height + x_offset + y_offset:
root.geometry("400x400+30+30") 

button_height=10
button_width=20



menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 



btn_import_PrevYear_premium_rgstr=tk.Button(root,text="Select PrevYear Register", command = csv_file_import_PrevYear)
#btn_import_PrevYear_premium_rgstr.pack()
btn_import_PrevYear_premium_rgstr.place(x=20, y=80)

btn_import_PrevYear_premium_rgstr=tk.Button(root,text="Select PrstYear Register", command = csv_file_import_PrstYear)
#btn_import_PrevYear_premium_rgstr.pack()
btn_import_PrevYear_premium_rgstr.place(x=20, y=120)

btn_print_csv=tk.Button(root,text="Process CSV", command = process_incentive)
#btn_import_PrevYear_premium_rgstr.pack()
btn_print_csv.place(x=20, y=160)

root.mainloop()
root.withdraw()

