'''
Time Complexity:
Time reqd to run an algorithm based on the input.

Big O Notation:
O(1) - Constant Time
O(log n) - Logarithmic Time
O(n) - Linear Time
O(n log n) - Linearithmic Time
O(n^2) - Quadratic Time
O(2^n) - Exponential Time
O(n!) - Factorial Time
'''
def constant_time(arr):
    return arr[0]
print(constant_time([10, 20, 30]))  # O(1)

def linear_time(arr):
    for i in arr:
        print(i)
print(linear_time([10, 20, 30, 40, 50]))  # O(n)

def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i, j)
print(quadratic_time([1, 2, 3]))  # O(n^2)

def linearithmic_time(arr):
    return sorted(arr)
print(linearithmic_time([10, 20, 30, 40, 50]))  # O(n log n)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input())
print(fibo(n))  # O(2^n)

