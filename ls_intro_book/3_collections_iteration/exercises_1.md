If you have a list named people, how can you determine the number of entries in that list?

Solution
You can use len(people) to determine the number of entries.

==============

Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

Copy Code
stuff = ('hello', 'world', 'bye', 'now')
Note: this problem is a bit tricky.

Solution
Since tuples are immutable, you can't replace 'bye' with 'goodbye'. At best, you can create a new tuple and reassign it:

Solution 1Copy Code
stuff = ('hello', 'world', 'goodbye', 'now')
Solution 2Copy Code
stuff = stuff[0:2] + ('goodbye', stuff[3])
Solution 3Copy Code
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
Solution 1 creates an entirely new tuple with the changed value. That's not quite in the spirit of what we're asking. It would also be tedious if the tuple contained more than a few elements.

Solution 2 is a little closer to being in the proper spirit. This one concatenates a slice of the original tuple combined with a new tuple that includes 'goodbye' and 'now' (from stuff[3]). However, that code is difficult to read. Furthermore, the slicing and indexing is a sure-fire way to get an off-by-one error. For example, if you wrote stuff[0:1] instead of stuff[0:2], the result would be missing 'world'.

Solution 3 is as close as we can get to the spirit of the problem. Here, we convert the original tuple to a list and reassign the element to the new value. Finally, we transform the list into a new tuple. This approach still creates an entirely new tuple. However, it avoids the problem of re-entering a long list of members, is cleaner than slicing and indexing, and is much easier to read.

===============

Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.

Solution
Differences
Lists are mutable; tuples are immutable.
List literals use []; tuple literals use ().
Similarities
Lists and tuples are both sequences. Sequences are ordered collections that can use numeric indexes to access the members.
Lists and tuples are heterogeneous; elements do not need to all be the same type.

=================

Why can we treat strings as sequences?

Solution
Strings are ordered; you can access the individual characters with indexing.

=================

How do the set types differ from the sequence types?

Solution
Sets are unordered; they don't support indexing.

==================

Assuming you have the following assignment:

Copy Code
pi = 3.141592
Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

Solution
Solution 1Copy Code
pi = 3.141592
str_pi = str(pi)
Solution 2Copy Code
pi = 3.141592
str_pi = f'{pi}'
Solution 1 is the preferred solution since it is slightly more readable. Solution 2 works, too. However, f-strings are better suited for creating strings mixed with other text.


==================

Without running the following code, identify the numbers that are included in each of the following ranges:

Copy Code
range(7)
range(1, 6)
range(3, 15, 4)
range(3, 8, -1)
range(8, 3, -1)
Solution
Copy Code
range(7)            # [0, 1, 2, 3, 4, 5, 6]
range(1, 6)         # [1, 2, 3, 4, 5]
range(3, 15, 4)     # [3, 7, 11]
range(3, 8, -1)     # []
range(8, 3, -1)     # [8, 7, 6, 5, 4]
The most important thing to observe here is that ranges never include the "stop" value. Furthermore, a negative step value counts downwards from the start to the stop value. Thus, the start value should typically be larger than the stop value when the step value is negative.

=================

How would you print all the numbers in the following range?

Copy Code
range(3, 17, 4)
Solution
Solution 1Copy Code
print(list(range(3, 17, 4)))
Solution 2Copy Code
print(tuple(range(3, 17, 4)))
Since ranges are lazy sequences, you must either iterate over the range or convert the range to a non-lazy sequence: a list or tuple. Here, we transform the range into a list and a tuple.

==================

Copy Code
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
Given the above code, answer the following questions and explain your answers:

Are the lists assigned to my_list and another_list equal?
Are the lists assigned to my_list and another_list the same object?
Are the nested lists at index 3 of my_list and another_list equal?
Are the nested lists at index 3 of my_list and another_list the same object?
Don't write any code for this exercise.

Solution
The two lists are equal: they are both lists with the same elements.
The two lists are not the same object: The list constructor creates a new object.
The two nested lists are equal: they are both lists that have the same elements.
The two nested lists are the same object: the list constructor creates a shallow copy of the iterable passed as an argument. Shallow copies don't create new nested lists. Instead, only a reference to the nested list gets copied.


====================

Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.

Copy Code
names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
Solution
This code probably won't print the names alphabetically. Sets, by definition, are unordered collections. Thus, the order in which members are shown when printing or iterating is arbitrary. Bob's code may print the names alphabetically on rare occasions, but it would do so only once every 5040 times.

=====================

Consider the data in the following table:

Name	Country
Alice	USA
Francois	Canada
Inti	Peru
Monika	Germany
Sanyu	Uganda
Yoshitaka	Japan
You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

Solution
Copy Code
countries = {
    'Alice':     'USA',
    'Francois':  'Canada',
    'Inti':      'Peru',
    'Monika':    'Germany',
    'Sanyu':     'Uganda',
    'Yoshitaka': 'Japan',
}

print(countries['Monika'])