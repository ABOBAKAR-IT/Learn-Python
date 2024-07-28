# To create a list, type the list within square brackets [ ],
# with your content inside the parenthesis and separated by commas. Let us try it!

L = ["Michael Jackson", 10.1, 1982]
print(L)

# List Content

# Lists can contain strings, floats, and integers. We can nest other lists,
# and we can also nest tuples and other data structures. The same indexing 
# conventions apply for nesting:

# Sample List

L = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
print(L)

# List Slicing
print(L[3:5])

# We can use the method extend to add new elements to the list:

L.extend(['pop', 10])
print(L)

# Another similar method is append. 
# If we apply append instead of extend, we add one element to the list:
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L)


# As lists are mutable, we can change them. For example, we can change the first element as follows:
# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)

# Split the string, default is by space

'hard rock'.split()

# Split the string by comma

'A,B,C,D'.split(',')