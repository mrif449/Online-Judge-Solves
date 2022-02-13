result = []
while True:
    number = int(input())
    result.append(number)
    if len(result) != 0:
        if result[len(result)-2] == 42:
            break
answer = ""    
result.pop()
result.pop()
for x in result:
    answer+= str(x)+"\n"
print(answer)