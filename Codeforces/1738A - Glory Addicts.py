number = int(input())
for x in range(number):
    limit = int(input())
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    ice = []
    fire = []
    for y in range(len(array1)):
        if array1[y] == 0:
            fire.append(array2[y])
        else:
            ice.append(array2[y])
    sum = 0
    result = abs(len(fire)-len(ice))
    array2.sort()
    ice.sort()
    fire.sort()
    if result > 0:
        sum1 = 0
        if len(fire) > len(ice):
            for a in range(len(fire)):
                if a < result:
                    sum1 += fire[a]
                else:
                    sum1 += fire[a]*2
            for a in range(len(ice)):
                sum1 += ice[a]*2
        else:
            for a in range(len(ice)):
                if a < result:
                    sum1 += ice[a]
                else:
                    sum1 += ice[a]*2
            for a in range(len(fire)):
                sum1 += fire[a]*2
        print(sum1)
    else:
        for z in range(len(array2)):
            if z == 0:
                sum += array2[z]
            else:
                sum += array2[z]*2
        print(sum)