print('hellow   world~')

#file=open("data.txt", mode="w", encoding="utf-8")
#file.write("測試中文\n好棒棒")
#file.close()
#用with 不用 close()
#with open("data.txt", mode="w", encoding="utf-8") as file:
#    file.write("測試中文\n好棒棒")
#with open("data.txt", mode="r", encoding="utf-8") as file:
#    data=file.read()
#print(data)

#with open("data.txt", mode="w", encoding="utf-8") as file:
#    file.write("3\n5")
#sum=0
#with open("data.txt", mode="r", encoding="utf-8") as file:
#    for line in file:
#        sum+=int(line)
#print(sum)

#隨機模組
import random
#隨機選取
#data=random.choice([1,5,6,10,20])
#print(data)
#data=random.sample([1,5,6,10,20], 3)
#print(data)
#隨機調換順序
#data=[1,5,6,10,20]
#random.shuffle(data)
#print(data)
#隨機取得亂數
#data=random.random() #0~1之間隨機取得亂數
#print(data)
#資料分析(要安裝安裝包pandas)
#import pandas as pd
#data=pd.DataFrame({
#    "name":["Amy", "Bob", "Charles"],
#    "salary":[30000, 50000, 40000]
#}, index=["a", "b", "c"])#index索引，不寫內建是0,1,2,3
#print(data)
#print("====================")
#print("資料數量", data.size)
#print("資料形狀 (列，欄)", data.shape)
#print("資料索引", data.index)
#取得列資料
#print("取得第二列", data.iloc[1], sep="\n")
#print("====================")
#print("取得第C列", data.loc["c"], sep="\n")
#取得欄位資料
#print("取得name欄位", data["name"], sep="\n")
#names=data["name"]
#print("把name全部轉大寫", names.str.upper(), sep="\n")
#計算薪水的平均值
#salaries=data["salary"]
#print("薪水的平均值", salaries.mean(), sep="\n")
#建立新的欄位
#data["revenue"]=[500000, 400000, 300000]
#data["rank"]=pd.Series([3, 6, 1], index=["a", "b", "c"])
#data["cp"]=data["revenue"]/data["salary"]
#print(data)