result = ""
count = int(input())
for x in range(count):
    marks = int(input())
    if marks >= 38:
        if marks%5 == 0:
            ceil = marks
        else:
            number = (marks//5)
            ceil = (number*5)+5
        if ceil-marks < 3:
            marks = ceil
        result += str(marks)+"\n"
    else:
        result += str(marks)+"\n"
print(result[:-1])