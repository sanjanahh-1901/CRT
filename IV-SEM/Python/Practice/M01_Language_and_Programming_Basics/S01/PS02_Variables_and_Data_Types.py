"""
Data types in Python:
1. Fundamental Data Types:
- Integer (int)
- Float (float)
- Complex (complex)
- String (str)
- Boolean (bool)
2. Collection Data Types:
- List (list)       
- Tuple (tuple)
- Set (set)
- Dictionary (dict)
"""

s1 = "python"
s2 = "python 3.14.2"
s3 = '''line1
line2
line3
'''
print(s1[3])      # h
print(s1[::2])   # pto
print(s1[::-1])   # nohtyp

# Examples of different data types in Python
x = 10          # Integer
y = 3.14        # Float     
z = 2 + 3j     # Complex
name = "Alice"  # String
is_student = True  # Boolean
fruits = ["apple", "banana", "cherry"]  # List
coordinates = (10.0, 20.0)  # Tuple
unique_numbers = {1, 2, 3, 4, 5} # Set
person = {"name": "Bob", "age": 25}  # Dictionary

# Print variable types
print(type(x))              # <class 'int'>
print(type(y))              # <class 'float'>
print(type(z))              # <class 'complex'>
print(type(name))           # <class 'str'>
print(type(is_student))     # <class 'bool'>
print(type(fruits))         # <class 'list'>
print(type(coordinates))    # <class 'tuple'>
print(type(unique_numbers))  # <class 'set'>
print(type(person))         # <class 'dict'>

# Example of type conversion
num_str = "100"
num_int = int(num_str)      # Convert string to integer
print(num_int, type(num_int))  # 100 <class 'int'>
num_float = float(num_int)  # Convert integer to float
print(num_float, type(num_float))  # 100.0 <class 'float'>
num_str_back = str(num_float)  # Convert float back to string
print(num_str_back, type(num_str_back))  # "100.0" <class 'str'>

# Demonstrating dynamic typing
var = 10
print(var, type(var))  # 10 <class 'int'>
var = "Now I'm a string"
print(var, type(var))  # Now I'm a string <class 'str'>
var = [1, 2, 3]
print(var, type(var))  # [1, 2, 3] <class 'list'>

# Variable naming conventions
my_variable = 5
_myVariable = 10
myVariable2 = 15
print(my_variable, _myVariable, myVariable2)

