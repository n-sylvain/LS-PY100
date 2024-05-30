Without running the following code, what do you think it will do?

Copy Code
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)
Solution
The code will raise an error:

Copy Code
SyntaxError: non-default argument follows
default argument
Here, we've defined foo with three parameters, with the second parameter having a default value. This is an error, however. Once Python sees a positional parameter with a default value, all subsequent parameters must have default values.

