#--------------------
#APPEND AND EXTEND
#--------------------

#lst.append(x) - Appends element x to the END of the list
my_list = [1, 2, 3, 4, 5, 6]
my_list.append(7)
print('Print appended list:')
print(my_list, '\n\n')


#PUZZLE (practice using append())
# What's the output of the code below?
nums = [1, 2, 3]
nums.append(nums[:])
print('-- List length is', len(nums), '--')
#THE ANSWER:
# Appending nums[:] to itself - Adds the list object as a new list item
# Print the updated list - notice there the list object ['1, 2, 3'] counts as one list item ...
print('What it Looks Like:')
print(nums, '\n\n')


# You can't append multiple elements in one method call. Instead call the append method multiple times
new_list = [1, 2]
print('New List:')
print(new_list)
# Let's append single ultimes and list objects
new_list.append(3)
new_list.append(4)
new_list.append([5, 6])
print('New List - Appended')
print(new_list, '\n\n')


# More append examples
another_list = [1, 2, 3]
print('Another List:')
print(another_list)
# Practice appending to the list
another_list.append(4)
another_list.append([5, 6])
another_list.append([7, 8])
# Print it again
print('After Multiple Append Methods:')
print(another_list, '\n\n')


#list.extend(iter) - This method adds all elements in a list as multiple new list items (not one list object)
last_list = [1, 2, 3]
last_list.extend([4, 5, 6])
print('Use the Extend Method Instead:')
print(last_list)






print('\n\n\n')