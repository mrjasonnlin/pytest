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

with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("3\n5")
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)

