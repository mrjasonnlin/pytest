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