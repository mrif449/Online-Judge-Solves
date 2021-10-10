a,b = list(map(int,input().split()))
count = 1
for x in range(1,int(b/a)+1):
    store = ""
    for y in range(a):
        store += str(count)+" "
        count += 1
    print(store[:-1])