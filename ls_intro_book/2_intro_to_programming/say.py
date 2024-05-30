def say():
    print('Output from say')

print('First')
say()
print('Last')

def say2():
    """
    The say2 function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say2.__doc__)
print('-' * 60)
help(say2)