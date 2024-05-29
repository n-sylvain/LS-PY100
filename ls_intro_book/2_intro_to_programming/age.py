import random

age = random.randint(1, 100)

print(f'You are {age} years old.')

for years in [10, 20, 30, 40]:
    print(f'In {years} years, you will be {age + years} old')
