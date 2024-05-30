Without running the following code, what do you think it will do?

Copy Code
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)
Solution
The code will raise an error:

Copy Code
TypeError: foo() takes 2 positional arguments,
but 3 were given
We've defined foo with two parameters. However, we've passed the function three arguments. This is an error.