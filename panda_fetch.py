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
    
#   load PrevYear register    
    premium_rgstr_PrevYear = pd.read_csv(premium_rgstr_PrevYear_filePath,dayfirst=True, parse_dates = True)
    premium_rgstr_PrevYear_csv= csv.DictReader(open(premium_rgstr_PrevYear_filePath))
    
#        
    
#   load PrstYear Register
    premium_rgstr_PrstYear = pd.read_csv(premium_rgstr_PrstYear_filePath,dayfirst=1, parse_dates = True)
    premium_rgstr_PrstYear_csv = csv.DictReader(open(premium_rgstr_PrstYear_filePath))


    root1= tk.Tk()
    root1.title('Premium Register PrevYear')
    # width x height + x_offset + y_offset:
    root1.geometry("400x400+30+30") 
    
    scrollbar1 = tk.Scrollbar(root1, orient="vertical") 
    scrollbar1.pack( side = tk.RIGHT, fill = tk.Y ) 
    scrollbar1b = tk.Scrollbar(root1, orient="horizontal") 
    scrollbar1b.pack( side = tk.BOTTOM, fill = tk.X ) 
    mylist1 = tk.Listbox(root1, yscrollcommand = scrollbar1.set, xscrollcommand = scrollbar1b.set ) 
#   DON'T DELETE BELOW CODE
#    for row1 in premium_rgstr_PrevYear_csv:
##        print (row1["Registration Number"])
#        mylist1.insert(tk.END, row1 )
  
        
    for i,row12 in premium_rgstr_PrevYear.iterrows():
        mylist1.insert(tk.END, row12)

    mylist1.pack( expand =1, fill = tk.BOTH ) 
    scrollbar1.config( command = mylist1.yview ) 
    scrollbar1b.config( command = mylist1.xview ) 
    
#   Display premium register of  PrstYear     

    root2= tk.Tk()
    root2.title('Premium Register PrstYear')
    # width x height + x_offset + y_offset:
    root2.geometry("400x400+30+30") 
    scrollbar2 = tk.Scrollbar(root2, orient="vertical") 
    scrollbar2.pack( side = tk.RIGHT, fill = tk.Y ) 
    scrollbar2b = tk.Scrollbar(root2, orient="horizontal") 
    scrollbar2b.pack( side = tk.BOTTOM, fill = tk.X ) 
    mylist2 = tk.Listbox(root2, yscrollcommand = scrollbar2.set, xscrollcommand = scrollbar2b.set ) 
#   DON'T DELETE BELOW CODE
#    for row2 in premium_rgstr_PrstYear_csv:
#        mylist2.insert(tk.END, row2 )
##    mylist2.insert(tk.END, premium_rgstr_PrstYear)
    for i,row22 in premium_rgstr_PrstYear.iterrows():
        mylist2.insert(tk.END, row22)
#        print(row22)

    mylist2.pack(  expand =1, fill = tk.BOTH ) 
    scrollbar2.config( command = mylist2.yview )
    scrollbar2b.config( command = mylist2.xview ) 
    
    print(premium_rgstr_PrstYear.info())
    
#    
#    FIND LIST OF UNIQUE AGENTS
#    
#    
        
    
    

#    
#    
#    PREVIOUS YEAR
#    
#    
    is_motor_PrevYear = premium_rgstr_PrevYear['Department']== 'Motor'
    premium_rgstr_PrevYear_motor= premium_rgstr_PrevYear[is_motor_PrevYear]
    premium_rgstr_PrevYear_motor['Previous year Policy Count'] = 1
    premium_rgstr_PrevYear_motor['Collection Date'] = pd.to_datetime(premium_rgstr_PrevYear_motor['Collection Date'],utc=True)
    premium_rgstr_PrevYear_motor['Effect Date'] = pd.to_datetime(premium_rgstr_PrevYear_motor['Effect Date'],utc=True)
    premium_rgstr_PrevYear_motor['Expiry Date'] = pd.to_datetime(premium_rgstr_PrevYear_motor['Expiry Date'],utc=True)
    premium_rgstr_PrevYear_motor['Insured Name'] = premium_rgstr_PrevYear_motor['Insured Name'].str.replace(',','')
    premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd'] = premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd'].str.replace(' -- NA -- NA','')
    sublist_column_index=['Agent Name', 'Agent Code', 'Package PrevYear', 'Package PrstYear' , 'Act PrevYear', 'Act PrstYear', 'Growth', 'Eligibilty']
    sublist_agents_prevYear={}
    list_agent_PrevYear= premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd'].unique().tolist()
#    messagebox.showinfo("Agent Count", "there are " + str(len(list_agent_PrevYear)) + " unique number of agents in our office.")
    print("there are " + str(len(list_agent_PrevYear)) + " unique number of agents in our office.")
    for agent in list_agent_PrevYear:
        print (agent)
        is_agent = premium_rgstr_PrevYear_motor['Agent/Br.Cd Biz Src Cd']== agent
        sublist_agents_prevYear[agent]= premium_rgstr_PrevYear_motor[is_agent]
    
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
    
    
    
    
    summed_premium_rgstr_prevYear_motor = premium_rgstr_PrevYear_motor.groupby('Agent/Br.Cd Biz Src Cd').sum()
    summed_premium_rgstr_prevYear_motor.fillna(0)
    summed_premium_rgstr_prevYear_motor.to_csv("00_summed_premium_rgstr_prevYear_motor.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
   
    is_package_act_prevYear = premium_rgstr_PrevYear_motor['TP Premium']== premium_rgstr_PrevYear_motor['Total']
    premium_rgstr_prevYear_motor_act = premium_rgstr_PrevYear_motor[is_package_act_prevYear]
    premium_rgstr_prevYear_motor_act.rename(columns={'Total':'Previous Year Total Act Premium', 'TP Premium':'Previous Year Total Act TP Premium', 'Previous year Policy Count': 'Previous year Act Policy Count'}, inplace=True)
    summed_premium_rgstr_prevYear_motor_act = premium_rgstr_prevYear_motor_act.groupby('Agent/Br.Cd Biz Src Cd').sum()
    summed_premium_rgstr_prevYear_motor_act.fillna(0)
    summed_premium_rgstr_prevYear_motor_act.to_csv("00_summed_premium_rgstr_prevYear_motor_act.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
    
    is_package_Package_prevYear = premium_rgstr_PrevYear_motor['TP Premium']!= premium_rgstr_PrevYear_motor['Total']
    premium_rgstr_prevYear_motor_package = premium_rgstr_PrevYear_motor[is_package_Package_prevYear]
    premium_rgstr_prevYear_motor_package.rename(columns={'Total':'Previous Year Total Package Premium', 'TP Premium':'Previous Year Total Package TP Premium', 'Previous year Policy Count': 'Previous year Package Policy Count'}, inplace=True)
    summed_premium_rgstr_prevYear_motor_package = premium_rgstr_prevYear_motor_package.groupby('Agent/Br.Cd Biz Src Cd').sum()
    summed_premium_rgstr_prevYear_motor_package.fillna(0)
    summed_premium_rgstr_prevYear_motor_package.to_csv("00_summed_premium_rgstr_prevYear_motor_package.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    



#    
#    PRESENT YEAR
#    
#    
    
    is_motor_PrstYear = premium_rgstr_PrstYear['Department']== 'Motor'
    premium_rgstr_PrstYear_motor= premium_rgstr_PrstYear[is_motor_PrstYear]
    premium_rgstr_PrstYear_motor['Present year Policy Count'] = 1
    premium_rgstr_PrstYear_motor['Collection Date'] = pd.to_datetime(premium_rgstr_PrstYear_motor['Collection Date'],utc=True)
    premium_rgstr_PrstYear_motor['Effect Date'] = pd.to_datetime(premium_rgstr_PrstYear_motor['Effect Date'],utc=True)
    premium_rgstr_PrstYear_motor['Expiry Date'] = pd.to_datetime(premium_rgstr_PrstYear_motor['Expiry Date'],utc=True)
    premium_rgstr_PrstYear_motor['Insured Name'] = premium_rgstr_PrstYear_motor['Insured Name'].str.replace(',','')
    premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd'] = premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd'].str.replace(' -- NA -- NA','')
    sublist_column_index=['Agent Name', 'Agent Code', 'Package PrevYear', 'Package PrstYear' , 'Act PrevYear', 'Act PrstYear', 'Growth', 'Eligibilty']
    sublist_agents_prstYear={}
    list_agent_PrstYear= premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd'].unique().tolist()
#    messagebox.showinfo("Agent Count", "there are " + str(len(list_agent_PrstYear)) + " unique number of agents in our office.")
    print("there are " + str(len(list_agent_PrstYear)) + " unique number of agents in our office.")
    for agent in list_agent_PrstYear:
        print (agent)
        is_agent = premium_rgstr_PrstYear_motor['Agent/Br.Cd Biz Src Cd']== agent
        sublist_agents_prstYear[agent]= premium_rgstr_PrstYear_motor[is_agent]
   
    
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
    
    
    
    summed_premium_rgstr_prstYear_motor=premium_rgstr_PrstYear_motor.groupby('Agent/Br.Cd Biz Src Cd').sum()
    summed_premium_rgstr_prstYear_motor.fillna(0)
    summed_premium_rgstr_prstYear_motor.to_csv("00_summed_premium_rgstr_prstYear_motor.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
    is_package_act_prstYear = premium_rgstr_PrstYear_motor['TP Premium']== premium_rgstr_PrstYear_motor['Total']
    premium_rgstr_prstYear_motor_act = premium_rgstr_PrstYear_motor[is_package_act_prstYear]
    premium_rgstr_prstYear_motor_act.rename(columns={'Total':'Present Year Total Act Premium', 'TP Premium':'Present Year Total Act TP Premium', 'Present year Policy Count': 'Present year Act Policy Count'}, inplace=True)
    summed_premium_rgstr_prstYear_motor_act = premium_rgstr_prstYear_motor_act.groupby('Agent/Br.Cd Biz Src Cd').sum()
    summed_premium_rgstr_prstYear_motor_act.fillna(0)
    summed_premium_rgstr_prstYear_motor_act.to_csv("00_summed_premium_rgstr_prstYear_motor_act.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
    
    is_package_Package_prstYear = premium_rgstr_PrstYear_motor['TP Premium']!= premium_rgstr_PrstYear_motor['Total']
    premium_rgstr_prstYear_motor_package = premium_rgstr_PrstYear_motor[is_package_Package_prstYear]
    premium_rgstr_prstYear_motor_package.rename(columns={'Total':'Present Year Total Package Premium', 'TP Premium':'Present Year Total Package TP Premium', 'Present year Policy Count': 'Present year Package Policy Count'}, inplace=True)
    summed_premium_rgstr_prstYear_motor_package = premium_rgstr_prstYear_motor_package.groupby('Agent/Br.Cd Biz Src Cd').sum()
    summed_premium_rgstr_prstYear_motor_package.fillna(0)
    summed_premium_rgstr_prstYear_motor_package.to_csv("00_summed_premium_rgstr_prstYear_motor_package.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')


#    merged_Act_data= pd.merge(summed_premium_rgstr_prstYear_motor_act,summed_premium_rgstr_prevYear_motor_act,left_index=True, right_index=True)
    merged_Act_data = summed_premium_rgstr_prstYear_motor_act.combine_first(summed_premium_rgstr_prevYear_motor_act)
    merged_Act_data['Present year Act Policy Count'] = merged_Act_data['Present year Act Policy Count'].add(0,fill_value=0)
    merged_Act_data['Previous year Act Policy Count'] = merged_Act_data['Previous year Act Policy Count'].add(0,fill_value=0)
    merged_Act_data['Growth for Act'] = merged_Act_data['Present Year Total Act Premium'].sub(merged_Act_data['Previous Year Total Act Premium'],fill_value=0)
    merged_Act_data['Growth for Act in %'] = merged_Act_data['Growth for Act'].truediv(merged_Act_data['Previous Year Total Act Premium'],fill_value=0) *100
    merged_Act_data['Incentive for Act in %'] = merged_Act_data['Growth for Act in %'].apply( calcuate_incentive_Act)
    for  index,row in merged_Act_data.iterrows():
        if row['Previous year Act Policy Count'] == 0:
            row['Incentive for Act in %'] = calcuate_incentive_Act_newAgent(row['Present year Act Policy Count'])
#        row['Incentive for Act in %'] = calcuate_incentive_Act(row['Growth for Act in %'])
    
    merged_Act_data['Incentive for Act'] = merged_Act_data['Incentive for Act in %'] * merged_Act_data['Present Year Total Act Premium'] /100
    merged_Act_data.to_csv("01_merged_act_data.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')




#    merged_Package_data= pd.merge(summed_premium_rgstr_prstYear_motor_package,summed_premium_rgstr_prevYear_motor_package,left_index=True, right_index=True)
    merged_Package_data= summed_premium_rgstr_prstYear_motor_package.combine_first(summed_premium_rgstr_prevYear_motor_package)
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
    
    merged_Package_data['Incentive for Package'] = merged_Package_data['Incentive for Package in %'] * merged_Package_data['Present Year Total Package Premium'] /100
    merged_Package_data.to_csv("01_merged_package_data.csv", sep=',',mode='w', quoting=csv.QUOTE_NONE, encoding='utf-8',escapechar='\\', date_format='%d/%m/%y')
    
    os.chdir("..")
    combined_data= merged_Package_data.combine_first(merged_Act_data)
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

