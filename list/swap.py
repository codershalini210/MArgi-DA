# Swap the first and last elements of a list without using any method.
numbers = [101,125,526,635,98]
print(numbers)
t = numbers[0]
numbers[0] = numbers[4]
print(numbers)
numbers[4]=t
print(numbers)

