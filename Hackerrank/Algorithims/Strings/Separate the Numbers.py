result = ""
for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    x = ''
    for i in s[:-1]:
        x += i
        y = int(x)
        z = ''
        while len(z) < n:
            z += str(y)
            y += 1
        if n == len(z) and z == s:
            result += f"YES {str(x)}\n"
            break
    else:
        result += "NO\n"
print(result[:-1])