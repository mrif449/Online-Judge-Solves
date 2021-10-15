N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:

while len(sumArray) <= len(numArray1)/2:
    for x in range(0,N):
        sumArray.append(numArray1[x]+numArray2[x])

# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")