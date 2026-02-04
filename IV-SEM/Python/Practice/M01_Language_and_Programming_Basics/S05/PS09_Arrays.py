'''
Arrays:
Collection of homogeneous data elements that can be stored in a single variable.
Python doesn't have built-in support for arrays like some other languages (e.g., C, Java).

NumPy:
NumPy-Numerical Python-powerful library for numerical computing in Python.
It can easily access arrays.
Mainly used in ML, DS, AI applications.

The index values start with 0 and end with (n-1), where n is the number of elements in the array.
'''

import numpy as np
arr = np.array([10, 20, 30])
print(arr)
print(np.max(arr))  # Maximum value in the array
print(np.min(arr))  # Minimum value in the array
print(np.mean(arr)) # Mean value of the array
print(np.sum(arr)) # Sum of all elements in the array
print(np.zeros(8)) # Array of 8 zeros
print(np.ones(5))  # Array of 5 ones
print("Even numbers list is:", np.arange(2, 10, 2)) # Even numbers from 2 to 10
print("Odd numbers list is:", np.arange(1, 10, 2)) # Odd numbers from 1 to 10

n = int(input("Enter the size of the array: "))
ele = list(map(int, input("Enter the elements: ").split()))
print("The elements in the array are:", np.array(ele[:n]))