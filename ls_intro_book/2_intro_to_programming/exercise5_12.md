Without running the following code, what do you think it will do?

Copy Code
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()
Solution
The code will raise an error:

Copy Code
TypeError: foo() missing 1 required positional
argument: 'first'
Here, we've defined foo with three parameters, with the second and third parameters having default values. We haven't passed the function any arguments. That's an error, though - the first parameter has no default value.