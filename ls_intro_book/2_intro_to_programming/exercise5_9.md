Without running the following code, what do you think it will do?

Copy Code
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
Solution
The code will print the following:

Copy Code
42
3.141592
2.718
Here, we've defined foo with three parameters, with the second and third parameters having default values. However, we've passed all three arguments to the function, so Python ignores the default values.

