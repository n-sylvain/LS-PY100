Without running the following code, what do you think it will do?

Copy Code
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

The code will raise an error:

Copy Code
TypeError: foo() missing 1 required positional
argument: 'qux'
We've defined foo with two parameters. However, we've only passed it one argument. This is an error.