'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S02.PS02_Factors_and_Primes
#print factors of the given number
input: 12
sample output: 1 2 3 4 6 12

#solution
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

#optimal solution
n = int(input("Enter a number: "))
for i in range(1, n//2 + 1):
    if n % i == 0:
        print(i, end=" ")
print(n)

#count the number of factors of a given number
from random import sample

input: 12
output: 6

n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)

#read a number from the user and check if it is prime or not
#solution
n = int(input("Enter a number: "))
counter = 0
for i in range(2, n//2 + 1):
    if n % i == 0:
        counter += 1
if counter == 0:
    print("Prime")
else:                       
    print("Not Prime")

#optimal solution
n = int(input("Enter a number: "))
counter = 0
for i in range(2, n//2 + 1):
    if n % i == 0:
        counter += 1
print("Prime" if counter == 0 else "Not Prime")

#print all prime numbers in the given range
input: 1; 10
output: 2; 3; 5; 7
a, b = map(int, input("Enter the range: ").split())
for num in range(a, b  + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

#read a number from the user and print its factorial
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

#gcd of two numbers     
input: 12 24 
output: 12

#solution 
a, b = map(int, input("Enter two numbers: ").split())
while b:
    a, b = b, a % b 
print(a)
'''

#reverse a number
class Solution:
    def reverse(self, num: int) -> int:
        if x < 0:
            x = -1 * x
            rev = int(str(x)[::-1])
            return -1 * rev
        else:
            rev = int(str(x)[::-1])
            return rev
        
#leetcode problems - palindrome number, multiply strings, plus one