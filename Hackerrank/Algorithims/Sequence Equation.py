number = int(input())
array = list(map(int, input().split()))
sortt = []
for x in array:
    sortt.append(x)
sortt.sort()
position1 = []
position2 = []
for x in sortt:
    index = array.index(x)
    position1.append(index+1)
for y in position1:
    index2 = array.index(y)
    position2.append(index2+1)
result = ""
for z in position2:
    result += str(z)+"\n"
print(result[:-1])