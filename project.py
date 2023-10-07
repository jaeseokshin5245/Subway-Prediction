# Import dataset
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

N = 274

sheet_list = [
    'Banseok', 'Jijock', 'Nonoun','Worldcup','Natcem', 'Guamn', 'Yoosung', 'Gapchun', 'Walpyeon', 'Galma', 'Govcom',
    'Cityhall', 'Tanbang',  'Yongmun', 'Oryong', 'Westdae','Midoffice', 'Midroad',  'Daejeon',  'Daedong','Sinhyun', 'Phanam'
]

file_list = ["geton.xlsx", "getoff.xlsx", "timetable.xlsx"]

On_data_list = []
Off_data_list = []
wk_ac_list = []
wk_dc_list = []
wkday_list_Off = []
wkday_list_On = []
Needed_getondff_list = []
total_time = []
wk_ac_list = []
wk_dc_list = []
split_list = []
intlist = []
temp_list = []
splited_list = []
getonlist = []
getofflist = []
total_list = []
time_list = []
time_inner_list = []

dir_path = os.path.dirname(os.path.abspath("project.ipynb"))
On_file_path = os.path.join(dir_path, file_list[0]) 
Off_file_path = os.path.join(dir_path, file_list[1])
tt_path = os.path.join(dir_path, file_list[2])


for i in range(len(sheet_list)):
    df = pd.read_excel(On_file_path, sheet_name = sheet_list[i])
    On_data_list.append(df)
    

for j in range(len(sheet_list)):
    df = pd.read_excel(Off_file_path, sheet_name = sheet_list[j])
    Off_data_list.append(df)

df_wk_ac = pd.read_excel(tt_path, sheet_name = "wk_ac")
df_wk_dc = pd.read_excel(tt_path, sheet_name = "wk_dc")

WKDAY = input("무슨 요일인가요? : ")

CLSTIME = int(input("몇 시 수업인가요? : "))

ORIGIN = input("출발역은 어디인가요? : ")

DESTI = input("도착역은 어디인가요? : ")

wkday_dict = {"일요일": 0,"월요일": 1,"화요일": 2,"수요일": 3,"목요일": 4,"금요일": 5,"토요일": 6}

station_list = {
    "반석" : 0, "지족" : 1, "노은" : 3, "월드컵경기장" : 4, "현충원" : 5, "구암" : 6, "유성온천" : 7, "갑천" : 8, "월평" : 9, "갈마" : 10, "정부청사" : 11, "시청" : 12,
    "탄방" : 13, "용문" : 14, "오룡" : 15, "서대전네거리" : 16, "중구청" : 17, "중앙로" : 18, "대전역" : 19, "대동" : 20, "신흥" : 21, "판암" : 22
    }

sum_time_On = 0
sum_time_Off = 0

for stations in range(station_list[ORIGIN], station_list[DESTI]):
    if wkday_dict[WKDAY] == 6:
        for wk in range(0, 11):

            wk = wk * 7 + wkday_dict[WKDAY]
            row = On_data_list[stations].iloc[wk]
            wkday_list_On.append(row)

        for k in range(0, 11):
            sum_time_On += wkday_list_On[k][CLSTIME]
        
        GetONAv = sum_time_On // 11
        Needed_getondff_list.append(GetONAv)

        for wk_1 in range(0, 11):
            wk_1 = wk_1 * 7 + wkday_dict[WKDAY]
            row_1 = Off_data_list[stations].iloc[wk_1]
            wkday_list_Off.append(row_1)

        for l in range(0, 11):
            sum_time_Off += wkday_list_Off[l][CLSTIME]

        GetOffAv = sum_time_Off // 11
        Needed_getondff_list.append(GetOffAv)
    
    else:

        for wk in range(0, 12):
            wk = wk * 7 + wkday_dict[WKDAY]
            row = On_data_list[stations].iloc[wk]
            wkday_list_On.append(row)
        
        for k in range(0, 12):
            sum_time_On += wkday_list_On[k][CLSTIME]
        
        GetONAv = sum_time_On // 12
        Needed_getondff_list.append(GetONAv)

        for wk_1 in range(0, 12):
            wk_1 = wk_1 * 7 + wkday_dict[WKDAY]
            row_1 = Off_data_list[stations].iloc[wk_1]
            wkday_list_Off.append(row_1)

        for l in range(0, 12):
            sum_time_Off += wkday_list_Off[l][CLSTIME]
        
        GetOffAv = sum_time_Off // 12
        Needed_getondff_list.append(GetOffAv)

wk_ac_list = df_wk_ac.values.T.tolist()
wk_dc_list = df_wk_dc.values.T.tolist()

for m in range(121):
    if wk_ac_list[0][m] == 0:
        split_list.append(wk_ac_list[0][m])
    else:
        split_list += wk_ac_list[0][m].split(":")

for string in split_list:
    intlist.append(int(string))

for n in range(121):
    if intlist[n] == 0:
        continue
    else:
        del intlist[n]

lastOne = intlist[-1]

for item in range(120):
    temp_list.append(intlist[item])
    
    if ((item == 0) or (item == 1)):
        splited_list.append(temp_list)
        temp_list = []
    
    if intlist[item] > intlist[item+1]:
        splited_list.append(temp_list)
        temp_list = []
    
if temp_list:
     splited_list.append(temp_list)

splited_list[-1].append(lastOne)

length_list = []

for p in range(len(splited_list)):
    length_list.append(len(splited_list[p]))

for w in range(0, len(Needed_getondff_list),2 ):
    getonlist.append(Needed_getondff_list[w])

for v in range(1, len(Needed_getondff_list),2 ):
    getofflist.append(Needed_getondff_list[v])

total_list.append(getonlist)
total_list.append(getofflist)

for aa in range(2):
    left_avg = total_list[aa][0]
    mid_avg = total_list[aa][int(len(total_list[aa])/2)]
    right_avg = total_list[aa][-1]


    length = length_list[CLSTIME-4]
    
    for bb in range(len(total_list[aa])):
        Aver = int(total_list[aa][bb] / length)
        slope = int((right_avg - mid_avg) / left_avg)
        alpha = int(Aver - (0.5 * slope * length))

        x = 0

        if left_avg < mid_avg > right_avg:
            x1 = np.linspace(-1, 0, 20)
            x2 = np.linspace(0, 1, 20)
            
            sec_slope = round((mid_avg - left_avg), 2)
            
            y1 = slope * x1 + mid_avg
            y2 = sec_slope * x2 + mid_avg
            
        elif left_avg > mid_avg < right_avg:
            x1 = np.linspace(-1, 0, 20)
            x2 = np.linspace(0, 1, 20)   
            sec_slope = round(left_avg - mid_avg, 2)
            
            y1 = slope * x1 + mid_avg
            y2 = sec_slope * x2 + mid_avg

        else:
            y1 = slope * x + alpha

        final_x = list(range(length))

        final_x_list = []
        time_inner_list = []

        for r in range(len(final_x)):
            final_y1 = slope * final_x[r] + alpha
            time_inner_list.append(final_y1)
        time_list.append(time_inner_list)
        
divder = int(len(time_list) /2)

y_final = []
Cur_Congestion = 0

for ab in range(len(time_list[0])-1):
    if station_list[ORIGIN] < station_list[DESTI]:          
        Cur_Congestion = round(((Cur_Congestion / 100 * N ) + time_list[0][ab+1] - time_list[0 + divder][ab+1]) / N * 100, 2)
        y_final.append(Cur_Congestion)
                
    elif station_list[ORIGIN] > station_list[DESTI]:
        Cur_Congestion = 0
        Cur_Congestion = round(((Cur_Congestion / 100 * N ) + time_list[0][ab+1] - time_list[0 + divder][ab+1]) / N * 100, 2)
        y_final.append(Cur_Congestion)

X = np.array(list(range(length-1)))
Y = y_final

def plot_prediction(pred, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, color='red')
    plt.plot(X, pred, color= 'blue')
    plt.show()
    
a = np.random.uniform(0, 20)
b = np.random.uniform(0, 20)

LR = 0.05
EpNum = 900

for epoch in range(EpNum):
    Y_Pred = a * X + b

    error = np.abs(Y_Pred - Y).mean()
    if error < 0.001:
        break

    # gradient descent calculation
    a_grad = LR * ((Y_Pred - Y)*X).mean()
    b_grad = LR * (Y_Pred - Y).mean()

    # updating W, b 
    a = a - a_grad
    b = b - b_grad

    if epoch % 30 == 0:
        Y_pred = a * X + b
        plot_prediction(Y_Pred, Y)