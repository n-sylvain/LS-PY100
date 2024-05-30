Take a look at this code snippet:

```python
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
```

What does this program print? Why?

The program prints bar since the assignment on line 4 creates a new variable that is local to the function. That is, the foo variable on line 4 shadows the foo variable on line 1, so line 4 doesn't change the value of foo from line 1.