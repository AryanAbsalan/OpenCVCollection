"""
    Tuple has the following characteristics

    Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
    Unchangeable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.
        But we can convert the tuple to a list, add items to the list , and then convert it back to a tuple.
        We can convert a tuple into a list and then remove any one item using the remove() method of the list. 
        Then convert it back into a tuple using the tuple() constructor.
    Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
    Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value.

    The tuples are used for the following requirements instead of lists.

    There are no append() or extend() to add items and similarly no remove() or pop() methods to remove items. 
    This ensures that the data is write-protected. 
    As the tuples are Unchangeable, they can be used to represent read-only or fixed data that does not change.
    As they are immutable, they can be used as a key for the dictionaries, while lists cannot be used for this purpose.
    As they are immutable, the search operation is much faster than the lists. 
    This is because the id of the items remains constant.
    Tuples contain heterogeneous (all types) data that offers huge flexibility in data that contains 
    combinations of data types like alphanumeric characters.

"""
# packing variables into tuple
tuple1 = 1, 2, "Hello"
print(tuple1)  

# unpacking tuple into variable
i, j, k = tuple1
print(i, j, k) 

# Limit the search locations using start and end
# search only from location 4 to 6
# get index of item 60 start = 4 and end = 6 
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80)
position = tuple1.index(60, 4, 6)
print(position)  

# Count all occurrences of item 60
tuple1 = (10, 20, 60, 30, 60, 40, 60)
count = tuple1.count(60)
print(count)

"""
    The chain() function is part of the itertools module in python.
    It makes an iterator, which will return all the first iterable items (a tuple in our case), 
    which will be followed by the second iterable. 
    We can pass any number of tuples to the chain() function.
"""

import itertools

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

# using itertools
tuple3 = tuple(item for item in itertools.chain(tuple1, tuple2))
print(tuple3)