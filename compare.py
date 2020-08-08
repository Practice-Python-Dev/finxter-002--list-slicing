#------------------------------
# COMPARING LISTS
#------------------------------

# Initialize lists to manipulate - Note, we aren't mutating them

list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
list2 = [10, 20, 30, 40, 50, 60]
list3 = [20, 40, 60]
list4 = [20, 40, 60]

#------------------------------
# CONVERT LISTS TO SETS
#------------------------------

# You can't subtract a list from a list
# But you can subtract a set from a set

# CREATE FUNCITON - Takes two arguments (listA, listB):
def whats_different(a, b):    
    # Convert the lists into sets, Subtract one from another - 'set(list)'
    # Convert the set containing what's different back into a list - 'list(set)'
    compute = (list(set(a) - set(b)))
    # Yes, that all happened on one line ... Now sort the list (it comes back in random order)
    compute.sort()
    # Last, return the sorted list containing "what's different"
    return(compute)

# PRINT STYLING
print("\n" + "-" *30)
print("List 1:", list1)
print("List 2:", list2)
print("\n" + "-" *30)

# CALL FUNCTION, PRINT
print("Difference:", whats_different(list1, list2))

#----- DO WITH LESS CODE -----

# Don't initialize a variable, Don't sort
def less_code(a, b):
    return list(set(a) - set(b))

# CALL FUNCTION, PRINT
print("Difference:", less_code(list1, list2))

# PRINT STYLING
print("\n" + "-" *30)

#------------------------------
# USE AN 'IF' STATEMENT
#------------------------------

# CREATE FUNCITON - Initialize and append to an empty list
# (Note, using a function is optional...)
def list_items(a, b):
    # Initialize empty list
    duplicates = []
    # Use 'for _ in _' logic
    for item in a:
        if item in b:
            duplicates.append(item)
    return (duplicates)

# CALL FUNCTION, PRINT
print("Same:", list_items(list1, list2))

# PRINT STYLING
print("\n" + "-" *30)

#------------------------------
#  LIST COMPREHENSION
#------------------------------

# "An elegent way to define and create lists based on existing lists."
# Syntax is kinda crazy, but it works (just as well as a for loop)
    # new_list = [expression for member in iterable]

#----- EXAMPLE -----

list_comprehension = [ item1 for item1 in list1 for item2 in list2 if item1 == item2 ]
print("List Comprehension:")
print(list_comprehension)

#----- ANOTHER EXAMPLE -----

# Use "list comprehension" on string ...
word_comprehension = [ letter for letter in "hello" ]
print(word_comprehension)

#----- LAMBDA EXAMPLE -----

# Lambda and other functions can create / modify lists
letters = list(map(lambda x: x, "goodbye"))
print("\nLambda Function:")
print(letters)

# PRINT STYLING
print("\n" + "-" *30)

#------------------------------
# COMPREHENSION CONDITIONALS
#------------------------------

# Create list that uses mathematical operators, integers, and range()

#----- USING IF -----

# Use range and calculate
number_list1 = [ x for x in range(21) if x % 2 ==0 ]
print("Evens in 20:", number_list1)

#----- NESTED IF -----

# Is y divisible by 2, Is y divisible by 5
# If y satisfies both conditions it's appended the list

number_list2 = [ y for y in range(100) if y % 2 == 0 if y % 5 == 0 ]
print("\nDivisible by 2 and 5:", number_list2)

#----- IF ... ELSE -----

my_object = [ "Even" if i % 2 == 0 else "0dd" for i in range(10 )]
print("\nEven or Odd:", my_object)

# PRINT STYLING
print("\n" + "-" *30)

#------------------------------
# TRANSPOSE OF MATRIX
#------------------------------

# A matrix is a two-dimensional data structure where numbers are arranged into rows and columns
    # For example: a 3x4 (pronounced "three by four") has 3 rows and 4 columns (like a spreadsheet)
    # Note, learn more about the 'matrix' ... (lol)

#----- USING NESTED LOOPS -----

# Transposing a 'matrix" using nested for loops
    # Transpose of a matrix is obtained by moving the rows data to the column and columns data to the rows
    # If we have an array of shape (X, Y) then the transpose of the array will have the shape (Y, X)

# This matrix is 2x4 ("two rows and by four columns")
matrix1 = [[1, 2, 3, 4], [4, 5, 6, 8]]
transposed1 = []

for i in range(len(matrix1[0])):
    transposed_row = []
    # 
    for row in matrix1:
        transposed_row.append(row[i])
    transposed1.append(transposed_row)

print (transposed1)
#Output: [[1, 4], [2, 5], [3, 6]]

#----- USING LIST COMPREHENSION -----

# Output should be the same as if we used a nested loop!
# Note, the range is 4 (number of items in each row ...)

matrix2 = [[1, 2, 3, 4], [4, 5, 6, 8]]
transposed2 = [[row[i] for row in matrix2] for i in range(4)]

print ()
print(transposed2)
#Output: [[1, 4], [2, 5], [3, 6]]

# Note: Nested loops in list comprehension don’t work like normal nested loops
# In the above program, for i in range(2) is executed before row[i] for row in matrix
# First, a value is assigned to i then item directed by row[i] is appended in the transpose variable

#------------------------------
# RESOURCES
#------------------------------

# https://www.programiz.com/python-programming/list-comprehension
# https://www.geeksforgeeks.org/python-difference-in-record-lists/?ref=rp
# https://www.stechies.com/compare-lists-python-using-set-cmp-function/#:~:text=The%20cmp()%20function%20is%20a%20built%2Din%20method%20in,1%2C%200%20or%20%2D1.
# https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
