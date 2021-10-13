def print_array_reverse(a):
    result = ""
    i = len(a)-1
    while i >= 0:
        result += str(a[i])+" "
        i -= 1
    print(result[:-1])
number = int(input())
list_1 = list(map(int, input().split()))

print_array_reverse(list_1)