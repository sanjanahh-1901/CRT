'''
Debugging in Python:
Bug: An error in a program that prevents it from running as expected.
Finding and fixing bugs is called debugging.

Types of errors:
1. Syntax Errors - Missing colon, parentheses, indentation
2. Runtime Errors - Number division by zero, file not found
3. Logical Errors - Missing logics, calculations and conditions

Debugging Techniques:
1. print - Run code line by line with print statements
2. try-except - Handle runtime errors gracefully
3. Using pdb - Python Debugger module for step-by-step execution
4. Using IDE Debuggers - Built-in debugging tools in IDEs like PyCharm, VSCode

pdb comments:
- n (next): Execute the next line of code   
- c (continue): Continue execution until the next breakpoint
- q (quit): Exit the debugger
- b (breakpoint): Set a breakpoint at a specific line number
- l (list): Display the current location in the code
- s (step): Step into a function call
- r (return): Continue execution until the current function returns
- p (print): Print the value of an expression
- h (help): Display a list of available commands or detailed help for a specific command

'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = a + b
print("Value of a:", a)
print("Value of b:", b)
print("Sum of a and b is:", c)

try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Not divisible by zero")
except ValueError:
    print("Invalid input")

import pdb
def add(a, b):
    pdb.set_trace()  # Set a breakpoint here
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a, b))