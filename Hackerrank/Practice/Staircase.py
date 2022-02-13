hash = "#"
space = " "
limit = int(input())
result = ""
for x in range(1,limit+1):
    result += (limit-x)*space + x*hash
    result += "\n"
print(result)