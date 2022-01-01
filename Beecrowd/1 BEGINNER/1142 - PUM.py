num = int(input())
list1 = [1,2,3]
count = 0
while count<num:
    print('{0} {1} {2} PUM'.format(list1[0],list1[1],list1[2]))
    count += 1
    list1[2] += 2
    list1[0] = list1[2]
    list1[1] = list1[2]
    list1[1] += 1
    list1[2] += 2