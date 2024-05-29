import random

value = random.randint(1, 100)

if value <= 10:
    print('value <= 10')
    if value >= 5:
        print('value >= 5')
    else:
        print('value < 5')
else:
    print('value > 10')

print(value)
