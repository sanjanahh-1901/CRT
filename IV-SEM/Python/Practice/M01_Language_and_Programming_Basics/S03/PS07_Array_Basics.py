'''
import array
arr = array.array('i', [12, 45, 78, 36])
print(arr, type(arr))
arr.append(40)
print(arr)
arr.append(12.45)
print(arr)
'''

import numpy
arr = numpy.array([12, 45, 78, 36])
print(arr, type(arr))
arr = numpy.array([12.5, 45.8, 78.9, 36.2])
print(arr, type(arr))

