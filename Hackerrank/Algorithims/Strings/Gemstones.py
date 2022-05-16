counter = 0
array = [0]*26
number = 2
total = 0
for x in range(number):   
    string = input()
    total += len(string)
    array2 = []
    for y in string:
        #if y not in array2:
            #array2.append(y)
            array[ord(y)-97] += 1
for z in array:
    if z == number:
        counter += 1
result = total - (2*counter)
print(result) 