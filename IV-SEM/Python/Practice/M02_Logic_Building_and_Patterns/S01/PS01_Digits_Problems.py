'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S01.PS01_Digits_Problems
sample input: 1234
sample output: 4

sample input: 12236
sample output: 5

'''
'''
#Count the number of digits in a number
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)
'''
'''
#Sum of digits in a number
n = input("Enter a number: ")
sum_of_digits = 0
for digit in n:
    sum_of_digits += int(digit)
print(sum_of_digits)
'''
'''
#Sum of digits in a number
n = int(input())
s = 0
while n > 0: 
    s += (n%10) 
    n = n // 10
print(s)
'''
'''
#Reverse a number
def reverse(num):
    rev = 0
    while num > 0:
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev

n = int(input())
num = 0
while n > 0:
    digit = n % 10
    num = digit + num * 10
    n = n // 10
print(num)
'''
'''
#Palindrome Number Checking
n = int(input())
palindrome = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = (reverse * 10) + digit
    n = n // 10
if palindrome == reverse:
    print("Palindrome")     
else:
    print("Not a palindrome")   
'''
'''
#Palindrome Number Checking
n = int(input())
reverse = 0
temp = reverse(n)
if n == temp:
    print(True)
else:
    print(False)
print(True if n == temp else False)
'''