max = {}

with open("dane_dzienmiesiacrok1.txt", "r", encoding="utf-8") as file:
    for line in file:
        tmp = (line.replace('\n','').split(";"))
        if tmp[0] not in max.keys():
            max[tmp[0]] = tmp[3]
        elif tmp[3] > max[tmp[0]]:
            max[tmp[0]] = tmp[3]

for i in max:
    print(i, max[i])