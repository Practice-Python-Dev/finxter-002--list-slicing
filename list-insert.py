#--------------------
#LIST INSERTS
#--------------------

#lst.insert(i, element) - add an element at a specific i (index)
my_list = [1, 2, 3, 4, 5, 6, 7]
print("My List")
print(my_list, '\n')
# Update the list
my_list.insert(7, 8)
my_list.insert(8, 9)
print("Updated List:")
print(my_list, '\n')


#NEGATIVE INDEX
# With a negative index you count backwards, starting from the right
# The insert() method inserts the element right in front of the index position
# Note: if you overshoot (e.g., -99) it will simply insert at the beginning of the list
new_list = [1, 2, 3, 4, 6, 7, 10, 11]
print("Numbers Missing:")
print(new_list, '\n')
# Update with insert
new_list.insert(-2, 9)
new_list.insert(-4, 8)
new_list.insert(-6, 5)
print('Updated List:')
print(new_list, '\n')





