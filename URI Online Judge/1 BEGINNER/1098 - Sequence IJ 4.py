i = 0; j = 1; a = 0; b = 0; c = 0
while (i <= 2):
    if (c == 0):
        print("I=%.0f J=%.0f" % (i, j))
    else:
        print("I=%.1f J=%.1f" % (i, j))
    b += 1
    if (b == 3):
        i += 0.2; a += 0.2; j = a; b = 0; c += 1
    if(c == 5):
        c = 0
    j += 1