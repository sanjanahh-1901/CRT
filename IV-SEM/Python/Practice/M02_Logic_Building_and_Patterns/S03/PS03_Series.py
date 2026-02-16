'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S03.PS03_Series
Arithmetic Series:
input: 1 2
output: 1 3 5 7 9 11 13 15 17 19

#arithmetic progression
a, d = map(int, input().split())
for n in range(1, 10):
    print(a+(n-1)*d, end=" ")

Geometric Series:
input: 1 2
output: 1 2 4 8 16 32 64 128 256 512 

#geometric progression
a, r = map(int, input().split())
for i in range(10):
    print(a*(r**i), end = " ")

Fibonacci Series:
input: 5
output: 0 1 1 2 3

#fibonacci using traditional method
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#fibonacci using list
n = int(input())
li = [0, 1]
for i in range(2, n):
    li.append(li[i-2] + li[i-1])
    print(li)

#factorial of a number
input: 5
output: 120 

#factorial using traditional method
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
'''
#factorial 
n = int(input())
if n < 0:
    print("No factorial for negative numbers.")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)

#factorial using function
def factorial(num): 
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact