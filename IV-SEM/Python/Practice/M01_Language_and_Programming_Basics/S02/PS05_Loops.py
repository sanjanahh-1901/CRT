#loop types: for loop, while loop
# while loop - executes a block of code as long as a specified condition is true
#for loop - iterates over a sequence (like a list, tuple, dictionary, set, or string)
#range - range(start,stop,step)
#iterable obj - string, list, tuple, dictionary, set
#while loop
'''
count = 0
while count < 5:
    print("Hello world!")
    count += 1  # increment count by 1


Read two integers start and stop variables.
Display all the even numbers between start and stop (inclusive).
Input : 1   10
Output : 2 4 6 8 10

start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))

for num in range (start, stop + 1):
    if num % 2 == 0:
        print(num, end=' ')

while start <= stop:
    if start % 2 == 0:
        print(start, end=' ')
    start += 1

consider 3 multiple as fizz , 5 multiple as buzz , both as fizzbuzz, else print the number from 1 to 10.
read a number n from user

start = int(input())
stop = int(input())
while start <= stop:
    if start % 3 == 0 and start % 5 == 0:
        print("FizzBuzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else:
        print(start)
    start += 1

#for loop
#syn: for i in range(start, stop, step):

for i in range(0,5,1):
    print("Hello world!")

#display n natural numbers in the same line using for loop
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end=' ')

#display n natural numbers in reverse order using for loop
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i, end=' ')
'''

li = [1,5,4,3,6,9,10]
for i in range(0,len(li),1):
    if i % 2 == 0:
        print(li[i], end=" ")
