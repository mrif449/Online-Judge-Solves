number = int(input())
result = ""
def is_palindrome(string):
	return string == string[::-1]

def solve(string):
	x , y = 0, len(string) - 1
	while (x < y) and (string[x] == string[y]):
		x += 1
		y -= 1
	if x == y:
		return -1
	if is_palindrome(string[x + 1 : y + 1]):
		return x
	if is_palindrome(string[x:y]):
		return y
	raise AssertionError

for _ in range(number):
	result += f"{str(solve(input()))}\n"
print(result[:-1])