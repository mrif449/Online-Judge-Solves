while True:
    try:
        number = int(input())
        if number == 0:
            print("vai ter copa!")
        elif number > 0:
            print("vai ter duas!")
    except EOFError:
        break