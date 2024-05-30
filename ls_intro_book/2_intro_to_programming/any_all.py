numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers])

print(any([number % 2 == 0 for number in numbers]))
print(all([number % 2 == 0 for number in numbers])) # False

numbers = [5, 13]
print(any([number % 2 == 0 for number in numbers])) # False
print(all([number % 2 == 0 for number in numbers])) # False

numbers = [2, 8, 10]
print(any([number % 2 == 0 for number in numbers])) # True
print(all([number % 2 == 0 for number in numbers])) # True