#--------------------
#REMOVE THINGS
#--------------------
# You can't grow a python list forever. Sooner or later you must remove elements and release disk and memory space
# We will cover list.remove(), list.pop(index), and list.clear()


#list.remove(element) - Removes the first occurance of an element (not all occruences)
my_list = [1, 2, 3, 4, 5, 6, 7]
print('My List:')
print(my_list, '\n')
# Remove ...
my_list.remove(7)
print('New List:')
print(my_list, '\n')
#NOTE:
# Removing an element from a list has a linear runtime complexity
# The growth of the runtime is restricted by a liner function O(n) for n elements - See O Notation (You have to check all elements in the list if the searched element doesn't exist ...)
# If the list has 1000 elements, you need 1000 comparisons. For 2000 elements, you'll need 2000 comparisons ...


#lst.pop() - This method removes AND returns the last element from an existing list
#lst.pop(index) - Removes and returns the element at the position index
# Make the list longer to play with ...
my_list.extend([7, 8, 9, 10])
print('Longer List:')
print(my_list, '\n')
# Pop the last element
my_list.pop()
# Pop the all other even elements
my_list.pop(0)
# Now print to screen
print('Cut Up List:')
print(my_list, '\n')


#lst.clear() - Removes all elements from an existing list (list becomes empty again)
# Using lst.insert() and lst.append methods (to restore the list)
my_list.insert(0, 1)
my_list.append(10)
print('Restored List:')
print(my_list, '\n')
# Now, let's use lst.clear
my_list.clear()
print('List Emptied:')
print(my_list, '\n')


#lst.remove(element) - Removes the first occurance of the PROVIDED element from an existing list
# Repopulate list (using a for loop for fun)
new_list = []
count = 1
while len(new_list) < 10:
    new_list.append(count)
    count += 1
print('Repopulated List:')
print(new_list, '\n')
# Now, let's remove a few elements
new_list.remove(1)
new_list.remove(3)
new_list.remove(2)
print(new_list, '\n')


#CODE PUZZLE
presidents = [ 'Clintont',
                'Bush',
                'Obama',
                'Trump']
presidents_2 = presidents[:4]
presidents_2.remove('Trump')
print('Some Better Than Others:')
print(presidents) # print what?
#ANSWER
# The computer prints ['Clinton', 'Bush', 'Obama', 'Trump']
# Becuase we manipulated presidents_2 - The inital presidents variable remained unchagned



print('\n\n')