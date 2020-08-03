#--------------------
#INDEX BY VALUE
#--------------------

#lst.index(value)
    # Method *returns the index* of the "value argument" (position of number)
    # You can use optional start and stop arguments to limit the index range where to search

#CHECK THE ENTIRE LIST
my_list = [1, 4, 6, 3, 6, 8, 8, 101, 33, 5, 13, 27, 58]
# Find where 101 is in the list (it's index)
my_index = my_list.index(101)
print('Where\'s 101...')
print('At position', my_index, '\n')



#CHECK A PORTION OF THE LIST
# Set start and stop arguments  - lst.index(value, start, stop)
# e.g., ("look for this, begin looking here, stop looking here")
print('6 within the first ten list items?')
print('Yes, at position:', my_list.index(6, 0, 9), '\n')



#ERROR WHEN NOT IN THE LIST
# Consider the following code:
    # print(my_list.index(27, 0, 9))
    # Output: "ValueError: 27 is not in list"
# We get an error because '27' isn't in first 10 indices

# We can prevent an error (using 'Exception Handling')
print('27 within the first ten list items?')
try:
    my_list.index(27, 0, 9)
    print('YES\n')
except ValueError:
    print('NO\n')



#FOR FUN - ENUMURATE A LIST
print('Index value pairs:')
for index, value in enumerate(my_list):
    print('Index %d = %d' % (index, value))
print()



#PUZZLE
    # Create a list of customers
    # Extract all names of customers starting with 'A'
    # Print the extracted customer names 
customers = ['Alice', 'Bob', 'Frank', 'Ann']
starts_with_A = []
for i in customers:
    if i[0] == 'A':
        starts_with_A.append(i)
print('Our customer list has these A-holes...')
print(starts_with_A, '\n')



#NOTES:
    # The index() method has linear runtime complexity in the number of list elements
    # For n elements, the runtime complexity is 0(n) because, in the worst case, you need to iterate over each element in the list to find that the element does' appear in it


