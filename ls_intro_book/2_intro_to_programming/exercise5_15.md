Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

```python
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
```

| Category | Identifiers                                             |
|----------|---------------------------------------------------------|
| Global   | multiply, get_num, first_number, second_number, product |
| Local    | left, right, prompt                                     |
| Built-in | float, input, print                                     |

Functions defined in a program file are global identifiers unless those functions are defined as an object property or nested inside another function. Thus, multiply, get_num, and product are globals in this program. Function parameters and variables initialized inside a function are always local identifiers. Thus, left, right, and prompt are all local variables. first_number and second_number are initialized on lines 7 and 8 respectively, then used on lines 9 and 10.