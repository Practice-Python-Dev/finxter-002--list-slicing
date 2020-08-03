#------------------------------
# SORT LISTS
#------------------------------

#lst.sort() - Sorts a list elements in ascending order
#lst.sort(reverse=True) - Sorts a list in descending order
my_list = ['bananas', 'apples', 'kiwis', 'oranges', 'watermelon', 'rasberries', 'strawberries', 'grapefruit']
print('Unsorted List:')
print(my_list, '\n')

# Sort ascending
my_list.sort()
print('Sorted List:')
print(my_list, '\n')

#Sort descending
my_list.sort(reverse=True)
print('Reversed List:')
print(my_list, '\n')


#ADVANCED - MODIFY DEFAULT SORTING BEHAVIOR
# lst.sort(key= lambda x: x[i]) - This allows you to modify the default sorting behavior
# Think of the i as where in a tuple you'd like to sort from. FOR EXAMPLE:
    # my_list = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
    # This is sorted ascending based on the first item in each tuple
# But we can sort the list by the second item in each tuple 
    # my_list.sort(key=lambda x: x:[1])
    # The list will be sorted like this:
    # my_list = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2)]

# This is complicated, so let's practice
tuple_list = [(1,2), (3,2), (3,3), (4,0), (1,0), (4,0)]
print('Unsorted Tuples:')
print(tuple_list, '\n')

#NOTE: lst.sort(keys=lambda x: x[0]) is the SAME AS lst.sort()
tuple_list.sort(key=lambda x: x[0])
print('Sorted Tuples:')
print(tuple_list, '\n')

# Let's sort the list by the second item in all tuples [1]
tuple_list.sort(key=lambda x: x[1])
print('Sort By Second item in tuple:')
print(tuple_list, '\n')

# Last, let's sort a list (without tuples) by leading number
# Standard sort below:
misc_nums = [11, 25, 2, 7, 50, 14, 33, 67, 76, 100, 99, 19]
misc_nums.sort()
print('Standard Sort:')
print(misc_nums, '\n')
# NOW, let's sort by leading number (e.g., 11 should come first)
# Hint: we need to analyze the int as a string ...
misc_nums.sort(key=lambda x: str(x)[0])
print('Leading Num Sort:')
print(misc_nums, '\n')


