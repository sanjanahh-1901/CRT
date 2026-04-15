'''
#Fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return "Provide a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5)) # 3
print(fibonacci(10)) # 34
print(fibonacci(15)) # 377

#GCD of two numbers using traditional approach
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(4, 10)) # 2
print(gcd(12, 18)) # 6
'''
#GCD of two numbers using recursion
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(4, 10)) # 2
print(gcd(12, 18)) # 6



