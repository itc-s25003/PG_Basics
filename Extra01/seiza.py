seiza = ["山羊座", "水瓶座", "魚座", "牡羊座", 
         "牡牛座", "双子座", "蟹座", "獅子座", 
         "乙女座", "天秤座", "蠍座", "射手座"]

month = int(input("Month: "))
day = int(input("Day: "))

def seizaFind(month, day):
    if month == 1:
        if day < 20:
            result = seiza[0]
        else:
            result = seiza[1]
    elif month == 2:
        if day < 19:
            result = seiza[1]
        else:
            result = seiza[2]
    elif month == 3:
        if day < 21:
            result = seiza[2]
        else:
            result = seiza[3]
    elif month == 4:
        if day < 20:
            result = seiza[3]
        else:
            result = seiza[4]
    elif month == 5:
        if day < 21:
            result = seiza[4]
        else:
            result = seiza[5]
    elif month == 6:
        if day < 22:
            result = seiza[5]
        else:
            result = seiza[6]
    elif month == 7:
        if day < 23:
            result = seiza[6]
        else:
            result = seiza[7]
    elif month == 8:
        if day < 23:
            result = seiza[7]
        else:
            result = seiza[8]
    elif month == 9:
        if day < 23:
            result = seiza[8]
        else:
            result = seiza[9]
    elif month == 10:
        if day < 24:
            result = seiza[10]
        else:
            result = seiza[11]
    elif month == 11:
        if day < 23:
            result = seiza[11]
        else:
            result = seiza[12]
    elif month == 12:
        if day < 22:
            result = seiza[12]
        else:
            result = seiza[0]
    return result

result = seizaFind(month, day)
print(result)
