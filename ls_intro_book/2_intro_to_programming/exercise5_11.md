Without running the following code, what do you think it will do?

Copy Code
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
Solution
The code will print the following:

Copy Code
42
3
2
Here, we've defined foo with three parameters, with the second and third parameters having a default value. We've passed the function one argument, so Python uses the default value for the last two parameters.