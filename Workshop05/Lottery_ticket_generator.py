from random import *

number_picks = int(input("How many quick picks? "))
numbers = []

for i in range(1, number_picks + 1):
    numbers1 = randint(range(1, 45), 6)
    numbers.append(numbers1)

print(numbers)



