# Reading: Format Strings in Python

# Format strings are a way to inject variables into a string in Python.
# They are used to format strings and produce more human-readable outputs. 
# There are several ways to format strings in Python:

# String interpolation (f-strings)

# Introduced in Python 3.6, f-strings are a new way to format strings in Python. They are prefixed with 
# 'f' and use curly braces {} to enclose the variables that will be formatted. For example:

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Additional capabilities

# F-strings are also able to evaluate expressions inside the curly braces,
# which can be very handy. For example:

x = 10
y = 20
print(f"The sum of x and y is {x+y}.")


# str.format()

# This is another way to format strings in Python.
# It uses curly braces {} as placeholders for variables which are passed as arguments
# in the format() method. For example:

name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))



# % Operator

# This is one of the oldest ways to format strings in Python. It uses the % operator 
# to replace variables in the string. For example:

name = "Johnathan"
age = 30
print("My name is %s and I am %d years old." % (name, age))



# Raw String (r’’)

# In Python, raw strings are a powerful tool for handling textual data, especially when dealing with escape characters.
# By prefixing a string literal with the letter ‘r’, Python treats the string as raw, meaning it interprets backslashes as literal characters rather than escape sequences.

# Consider the following examples of regular string and raw string:

# Regular string:

regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)


# Output:
# Regular String:  C:
# ew_folderile.txt

# In the regular string regular_string variable, the backslashes (\n) are interpreted as escape sequences.
# Therefore, \n represents a newline character, which would lead to an incorrect file path representation.

# Raw string:

raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)


# Output

# Raw String: C:\new_folder\file.txt