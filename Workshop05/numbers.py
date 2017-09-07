numbers = []
nums = 5

for i in range(1, nums + 1):
    number = int(input("Number " + str(i) + ": "))
    numbers.append(number)

print(numbers)

print("The first number is " + str(numbers[0]))
print("The last number is " + str(numbers[4]))

numbers.sort()

print("The smallest number is " + str(numbers[0]))
print("The largest number is " + str(numbers[4]))
print("The average number is " + str(sum(numbers)/len(numbers)))


