number = int(input())
white = 0
black = 0
if number%2 == 0:
    white = (number/2)*number
    black = white
else:
    number = number + 1
    white = ((number/2)*number)-(number-1)
    black = white - 1
print(int(white),"casas brancas e",int(black),"casas pretas")