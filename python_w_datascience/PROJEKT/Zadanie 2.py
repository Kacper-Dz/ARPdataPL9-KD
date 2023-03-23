with open("dane_dzienmiesiacrok.txt", "r", encoding="utf-8") as file:
    with open("dane_dzienmiesiacrok1.txt", "a", encoding="utf-8") as output:
        for line in file:
            tmp = (line.replace('\n','').split(";"))
            row = tmp[0][:2] + ";" \
                  + tmp[1] + ";" + tmp[2] \
                  + ";" + str(round(int(tmp[1]) * float(tmp[2]), 2)) + "\n"
            output.write(row)
