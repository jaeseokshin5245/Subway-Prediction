import pandas as pd
import os

sheet_list = ['Phanam', 'Sinhyun']
file_list = ["geton.xlsx", "getoff.xlsx"]

On_data_list = []
Off_data_list = []

dir_path = os.path.dirname(os.path.abspath("project.ipynb"))
On_file_path = os.path.join(dir_path, file_list[0])
Off_file_path = os.path.join(dir_path, file_list[1])


for i in range(len(sheet_list)):
    df = pd.read_excel(On_file_path, sheet_name = sheet_list[i])
    On_data_list.append(df)
    

for j in range(len(sheet_list)):
    df = pd.read_excel(Off_file_path, sheet_name = sheet_list[j])
    Off_data_list.append(df)

wkday_list = []

wkday_dict = {"Sun": 0,"Mon": 1,"Tues": 2,"Weds": 3,"Thurs": 4,"Fri": 5,"Sat": 6}

for wk in range(0, 13):
    wk = wk * 7 + wkday_dict["Thurs"]
    row = Off_data_list[1].iloc[wk]
    wkday_list.append(row)
    