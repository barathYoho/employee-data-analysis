
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    square = number * number
    total = total + square

print("Total:", total)
print("Average:", total / len(numbers))
