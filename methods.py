#--------------------
# PYTHON LIST METHODS
#--------------------

# lst.append(x) - Appends element x to the lst
fruits = ['apples', 'oranges', 'kiwis', 'grapefruit', 'watermelon', 'bananas', 'canteloupe']
fruits.append('grapes')
print(fruits, '\n')


# lst.clear() - Removes all elements from the list,which becomes empty
fruits.clear()
print('List still exists. But look inside:', fruits, '\n')


#lst.copy() - Returns a copy of the list
fruits = ['apples', 'oranges', 'kiwis', 'grapefruit', 'watermelon', 'bananas', 'canteloupe', 'grapes']
fruits_clone = fruits.copy()
print('This is list copy:')
print(fruits_clone, '\n')


#lst.count(x) - Counts the number of occurences of element x in the list
fruits.append('bananas')
print('Appended bananas to the list:')
print('There are now', fruits.count('bananas'), 'bananas in list.', '\n')


#lst.extend(iterable) - Adds all elements of 'iterable' to the list (e.g., list, tuple, string)
berries = ['strawberries', 'blueberries', 'rasberries']
fruits.extend(berries,)
print('Use "extend" to append the list "berries" at the end:')
print(fruits, '\n')


#lst.index(x) - Returns fot position (index) of THE FIRST occurence of value x in the list
print('Find the first occurance of "bananas"')
print('At position', (fruits.index('bananas')), '\n')


#lst.insert(i, x) - Inserts element x at position i (index) in the list
print('Fruits is:')
print(fruits, '\n')
# Insert a string at the beginning of 'fruits'
fruits.insert(0, 'bananas')
print('Insert more bananas:')
print(fruits, '\n')


#lst.pop - Removes AND RETURNS the last element of the list (only)
print('Fruits is:')
print(fruits, '\n')
# Let's pop the last variable off the list
print(fruits.pop(), 'was popped!', '\n')
print('Fruits is now:')
print(fruits, '\n')


#lst.remove(x) - Removes and returns THE FIRST occurence of element x in the list
print('Remove the first banana:')
# Run the method, then print fruits again
fruits.remove('bananas')
print(fruits, '\n')


#lst.reverse() - Reverses the order of elements in the list
fruits.reverse()
print('Reverse the list ')
print(fruits, '\n')


#lst.sort() - Sort the elements in the list in ascending order (alphabetical)
fruits.sort()
print(fruits, '\n')





print('\n\n')