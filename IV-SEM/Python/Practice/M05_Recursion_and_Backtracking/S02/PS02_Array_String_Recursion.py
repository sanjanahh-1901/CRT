'''
#Sum of array elements using traditional approach
from operator import index

def array_sum(nums):
    s = 0
    for i in range(len(nums)-1, -1, -1):  #4, -1, -1 are the values for i in each iteration
        s += nums[i]
    return s
print(array_sum([1, 2, 3, 4, 5])) # 15
print(array_sum([10, 20, 30, 40, 50])) # 150

#Sum of array elements using recursion
def array_sum1(nums):
    if index == -1:
        return 0
    return nums[index] + array_sum1(nums, index-1)
print(array_sum1([1, 2, 3, 4, 5])) # 15
print(array_sum1([10, 20, 30, 40, 50])) # 150

#Recursive approach
def array_sum2(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + array_sum2(nums[1:])

print(array_sum2([1, 2, 3, 4, 5])) # 15 

#Reverse an array
def reverse_array(nums):
    res = []
    for i in range(len(nums)-1, -1, -1):
        res.append(nums[i])
    return res
print(reverse_array([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]

#Reverse an array
def reverse_array(nums, i, j):
    if i >= j:
        return nums
    nums[i], nums[j] = nums[j], nums[i]
    return reverse_array(nums, i+1, j-1)
print(reverse_array([1, 2, 3, 4, 5], 0, 4)) # [5, 4, 3, 2, 1]
'''
#Reverse a string
def reverse_string(st):
    if len(st) == 0:
        return st
    else:
        return st[-1] + reverse_string(st[:-1])

print(reverse_string("abc")) #cba 

def is_palindrome(st):
    return st == reverse_string(st)

print(is_palindrome("abc")) # False
print(is_palindrome("abcba")) # True

