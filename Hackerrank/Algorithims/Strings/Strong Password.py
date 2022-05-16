length = int(input())
string = input()
case_check = [0,0,0,0]
special_character = ["!","@","#","$","%","^","&","*","(",")","-","+"]
for x in string:
    if 48<=ord(x)<=57:
        case_check[0] += 1
    if x.islower():
        case_check[1] += 1
    if x.isupper():
        case_check[2] += 1
    if x in special_character:
        case_check[3] += 1
    
counter = 0
for y in case_check:
    if y == 0:
        counter += 1
result = 6-length
if result >= counter:
    result == result
elif result < counter:
        result = counter
print(result)