number = int(input())
result_array = []
for x in range(number):
    array = []
    var = (input())
    for y in range(8):
        temp = []
        value = input()
        for z in range(8):
            temp.append(value[z])
        array.append(temp)
    for a in array:
        counter1 = 0
        counter2 = 0
        for b in a:
            if b == "R":
                counter1 += 1
            elif b == "B":
                counter2 += 1
        if counter1 == 8:
            #print("R")
            result_array.append("R")
            counter1 = 0
            break
        """elif counter2 == 8:
            counter2 = 0
            #print("B")
            result_array.append("B")
            break"""
    for a in range(8):
        counter3 = 0
        counter4 = 0
        for b in range(8):
            if array[b][a] == "R":
                counter3 += 1
            elif array[b][a] == "B":
                counter4 += 1
        """if counter3 == 8:
            counter3 = 0
            result_array.append("R")
            #print("R")
            break"""
        if counter4 == 8:
            counter3 = 0
            #print("B")
            result_array.append("B")
            break

for x in result_array:
    print(x)
