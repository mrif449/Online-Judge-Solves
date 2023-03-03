import math
result = ""
while True:
    string = input().split()
    if string[0] == "0":
        break
    else:
        array = []
        for x in string:
            array.append(int(x))
        temp = math.sqrt(((array[0])*(array[1])*100)/(array[2]))
        result += str(int(round(temp,0)))+"\n"
print(result[:-1])
