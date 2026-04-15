'''
#Sum of n natural numbers in traditional approach
def Natural_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s
print(Natural_sum(5)) # 15
print(Natural_sum(10)) # 55

#Sum of n natural numbers in reverse order
def Natural_sum(n):
    s = 0
    for i in range(n, 0, -1):
        s += i
    return s
print(Natural_sum(5)) # 15
print(Natural_sum(10)) # 55

#Sum of n natural numbers using recursion
def Natural_sum(n):
    if n == 1:                                     
        return 1
    else:
        return n + Natural_sum(n-1)
print(Natural_sum(5)) # 15
print(Natural_sum(10)) # 55

#Factorial of a number using traditional approach
def factorial(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
print(factorial(3)) # 6
print(factorial(5)) # 120
print(factorial(10)) # 3628800

#Factorial of a number using traditional approach in reverse order
def factorial_reverse(n):
    s = 1
    for i in range(n, 0, -1):
        s *= i
    return s
print(factorial_reverse(3)) # 6
print(factorial_reverse(5)) # 120
print(factorial_reverse(10)) # 3628800
'''
#Factorial of a number using recursion
def factorial(n):
    if n < 0:
        return "No factorial is not defined for negative numbers"
    if n == 0 or n == 1:                                     
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3)) # 6
print(factorial(5)) # 120
print(factorial(10)) # 3628800

