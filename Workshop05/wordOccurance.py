string = str(input("Input a string: "))
words = string.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(string)
print(words)

