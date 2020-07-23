#--------------------
#LIST SLICING
#--------------------

# Mastering slicing is importing - "Any non-trivial Python code base relies on slicing"
# Slicing dives deeper than indexing - You can retrive substrings within an index range


# Create a string to slice - Note slice does not mean remove
my_string = 'universe'
# Print the first three letters - Think like this [0 <= x < 3]
print(my_string[0:3], '\n')


# There's also shorthand - Print from the beginning to the index of your choice
print(my_string[:4], '\n')
# Or from a decided start point to the end
print(my_string[3:], '\n')


# We can add one more parameter - Add steps at the end (like this [start:end:steps])
print(my_string[::2])