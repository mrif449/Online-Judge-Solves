result = ""
number = int(input())
for i in range(number):
	string= (input())
	length = len(string)
	if (length%2==0):
		half = int(length/2)
		a = string[:half]
		b = string[half:]
		counter = 0
		for x in a:
			if x in b:
				pos = b.find(x)
				b=b[:pos]+b[pos+1:]
			else:
			 counter += 1
		result += str(counter) + "\n"
	else:
		result += "-1\n"
print(result[:-1])