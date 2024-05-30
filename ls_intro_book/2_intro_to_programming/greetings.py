import time

name = 'Jane'
print(f'Good morning, {name}!')

print({ 'a': 1, "b": 42, 'c': "string", 'd': [5, 6], 'e': { 8, 9, 10 }})

print(time.asctime())

print(1, 2, 3, 'a', 'b')
print([1, 2, 3], 4, False, { 5, 6, 7, 8})
print(1, 2, 3, 'a', 'b', sep=',')
print('a', 'b', 'c', 'd', 'e', sep='')
print(1, 2, 'a', 'b', sep=',', end=' <-\n')
print('a', 'b', end='', sep=','); print('c', 'd', sep=',')
# Note the semicolon (;) on line 4: that's an easy way to enter multiple
# statements on a single line. Mostly, you should only use semicolons like this in the REPL.
print()