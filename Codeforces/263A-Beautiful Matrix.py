array = []
for x in range(5):
    temp_array = list(map(int, input().split()))
    array.append(temp_array)
answer = 0
for x in range(5):
    if 1 in array[x]:
        if x < 2:
            for y in range(5):
                if array[x][y] == 1:
                    answer = (13 - x*5)-(y+1)

        elif x == 2:
            for y in range(5):
                if array[x][y] == 1:
                    if y == 2:
                        answer = 0
                    elif y < 2:
                        answer = abs((3-y)-1)
                    else:
                        answer = abs(y-2)
        else:
            for y in range(5):
                if array[x][y] == 1:
                    answer = (x*5-13)+(y+1)
print(answer)