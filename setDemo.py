"""
    Characteristics of a Set

    Unordered: The items in the set are unordered, unlike lists, 
    i.e., it will not maintain the order in which the items are inserted. 
    The items will be in a different order each time when we access the Set object.
    There will not be any index value assigned to each item in the set.

    Unchangeable: Set items must be immutable. We cannot change the set items, 
    i.e., We cannot modify the items’ value. But we can add or remove items from the Set. 
    A set itself may be modified, but the elements contained in the set must be of an immutable type.

    Unique: There cannot be two items with the same value in the set.

    remove()	To remove a single item from a set. This method will take one parameter,
     which is the item to be removed from the set. 
     Throws a keyerror if an item not present in the original set

    discard()	To remove a single item that may or may not be present in the set. 
    This method also takes one parameter, which is the item to be removed. 
    If that item is present, it will remove it. 
    It will not throw any error if it is not present.

"""

# create a set using {}
sample_set = {'Mark', 'Jessa', 25, 75.25}
print(sample_set)

# create a set using set constructor
book_set = set(("Harry Potter", "Angels and Demons", "Atlas Shrugged"))
print(book_set)

#You will get an error if you try to create a set with mutable elements like lists or dictionaries as its elements.
#sample_set = {'Mark', 'Jessa', [35, 78, 92]}
#print(sample_set)
# Output TypeError: unhashable type: 'list' [35, 78, 92]

#whenever you wanted to create an empty set always use the set() constructor.
emptySet = {}
print(type(emptySet)) # class 'dict'

# add() method
book_set = {'Harry Potter', 'Angels and Demons'}
book_set.add('The God of Small Things')
print(book_set)

# update() method to add more than one item
book_set.update(['Atlas Shrugged', 'Ulysses'])
print(book_set)


color_set = {'red', 'orange', 'yellow', 'white', 'black'}

# remove single item
color_set.remove('yellow')
print(color_set)

# remove single item from a set without raising an error
color_set.discard('white')
print(color_set)

# remove any random item from a set
deleted_item = color_set.pop()
print(deleted_item)

# remove all items
color_set.clear()
print(color_set)

# delete a set
del color_set

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# union of two set using OR operator
vibgyor_colors = color_set | remaining_colors
print(vibgyor_colors)
# Output {'indigo', 'blue', 'violet', 'yellow', 'red', 'orange', 'green'}

# union using union() method
vibgyor_colors = color_set.union(remaining_colors)
print(vibgyor_colors)
# Output {'indigo', 'blue', 'violet', 'yellow', 'red', 'orange', 'green'}


color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# intersection of two sets
common_colors = color_set.intersection(remaining_colors)
print(common_colors)  # output {'indigo'}
# original set after intersection
print(color_set)
# Output {'indigo', 'violet', 'green', 'yellow', 'blue'}

# intersection of two sets using intersection_update()
color_set.intersection_update(remaining_colors)
# original set after intersection
print(color_set)
# output {'indigo'}

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}


# difference using '-' operator
print(color_set - remaining_colors)
# output {'violet', 'blue', 'green', 'yellow'}

# difference of two sets
new_set = color_set.difference(remaining_colors)
print(new_set)
# output {'violet', 'yellow', 'green', 'blue'}
# original set after difference
print(color_set)
# {'green', 'indigo', 'yellow', 'blue', 'violet'}

# difference of two sets
color_set.difference_update(remaining_colors)
# original set after difference_update
print(color_set)
# Output {'green', 'yellow', 'blue', 'violet'}


color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

# symmetric difference between using ^ operator
unique_items = color_set ^ remaining_colors
print(unique_items)
# Output {'blue', 'orange', 'violet', 'green', 'yellow', 'red'}

# symmetric difference
unique_items = color_set.symmetric_difference(remaining_colors)
print(unique_items)
# output {'yellow', 'green', 'violet', 'red', 'blue', 'orange'}
# original set after symmetric difference
print(color_set)
# {'yellow', 'green', 'indigo', 'blue', 'violet'}

# using symmetric_difference_update()
color_set.symmetric_difference_update(remaining_colors)
# original set after symmetric_difference_update()
print(color_set)
# {'yellow', 'green', 'red', 'blue', 'orange', 'violet'}

set1 = {20, 4, 6, 10, 8, 15}
sorted_list = sorted(set1)
sorted_set = set(sorted_list)
print(sorted_set)
# output {4, 6, 8, 10, 15, 20}


rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
# create a frozenset
f_set = frozenset(rainbow)

print(f_set)
# output frozenset({'green', 'yellow', 'indigo', 'red', 'blue', 'violet', 'orange'})

rainbow = ('violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')
other_colors = ('white', 'black', 'pink')

nested_set = set((frozenset(rainbow), frozenset(other_colors)))

for sample_set in nested_set:
    print(sample_set)
    

""" 
    When to use frozenset ?
    When you want to create an immutable set that doesn’t allow adding or removing items from a set.
    When you want to create a read-only set

    All the mathematical operations performed in a set is possible with the frozenset.
    We can use union(), intersection(), difference(), and symmetric_difference() on a frozenset as well.

    But we can’t use the 
        intersection_update(),
        difference_update() and symmetric_difference_update() on frozenset as it is immutable.
        When to use a Set Data structure?

It is recommended to use a set data structure when there are any one of the following requirements.

Eliminating duplicate entries: 
    In case a set is initialized with multiple entries of the same value,
    then the duplicate entries will be dropped in the actual set. A set will store an item only once.

Membership Testing: 
    In case we need to check whether an item is present in our dataset or not,
    then a Set could be used as a container. Since a Set is implemented using Hashtable, 
    it is swift to perform a lookup operation, i.e., 
    for each item, one unique hash value will be calculated, and it will be stored like a key-value pair.
    So to search an item, we just have to compute that hash value and search the table for that key. 

Performing arithmetic operations similar to Mathematical Sets: 
    All the arithmetic operations like union, Intersection, finding the difference 
    that we perform on the elements of two sets could be performed on this data structure.

"""
