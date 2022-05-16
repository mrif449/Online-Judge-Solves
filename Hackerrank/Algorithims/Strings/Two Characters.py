def char_range(string1, string2):
    for c in range(ord(string1), ord(string2)+1):
        yield chr(c)      
def is_alternating(string):
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return False
    return True  
number = int(input())
s = input()
counter = 0    
for string1 in char_range('a', 'z'):
    for string2 in char_range('a', 'z'):
        if string1 == string2:
            continue
        string = [c for c in s if c == string1 or c == string2]
        length = len(string)
        if is_alternating(string) and length > 1:
            if length > counter:
                counter = length           
print(counter)