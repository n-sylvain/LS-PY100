What does this code output, and why?

Copy Code
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])
Solution
The output is Empty since an empty list like [] is falsy. As a result, my_list on line 2 is falsy, so the else block runs instead of the if block.