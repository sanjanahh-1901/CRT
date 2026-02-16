'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_Patterns.S03.PS04_Number_Validation
1. Palindrome Number
input: 121
output: palindrome

input: 123
output: not palindrome

#palindrome number
n = int(input())
temp = n
rev = 0
while temp > 0:
    dig = temp % 10
    rev = rev * 10 + dig
    temp //= 10
if n == rev:
    print("palindrome")
else:
    print("not palindrome")

2. Armstrong Number
input: 153
output: armstrong
explanation: 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

input: 123
output: not armstrong
explanation: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 != 123

#armstrong number
n = int(input())
temp = n
order = len(str(n))
armstrong_sum = 0   
while temp > 0:
    dig = temp % 10
    armstrong_sum += dig ** order
    temp //= 10
if n == armstrong_sum:
    print("armstrong")
else:
    print("not armstrong")

3. Strong Number
input: 145
output: strong
explanation: 1! + 4! + 5! = 1 + 24 + 120 = 145

input: 123
output: not strong
explanation: 1! + 2! + 3! = 1 + 2 + 6 = 9 != 123
'''
#strong number
n = int(input())
temp = n
strong_sum = 0
while temp > 0:
    dig = temp % 10
    factorial = 1
    for i in range(1, dig + 1):
        factorial *= i
    strong_sum += factorial
    temp //= 10
if n == strong_sum:
    print("strong")
else:
    print("not strong")

#strong number using function
def factorial(num): 
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact
