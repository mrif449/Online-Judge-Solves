number = int(input())
string = input()
store = 0
for x in range(12):
    for y in range(12):
        inp = float(input())
        if x == number:
            store += inp
if string == "S":
    print("{:.1f}".format(store))
else:
    print("{:.1f}".format(store/12.0))