list1 = list(map(int, input().split()))
word = input()
highest = 0
word_length = len(word)
for x in word:
    if list1[ord(x)-97] > highest:
        highest = list1[ord(x)-97]
result = highest*word_length
print(result)