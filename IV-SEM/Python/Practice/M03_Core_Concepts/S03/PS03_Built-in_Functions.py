'''
#Find largest number from a list of numbers without using built-in functions.
#input = [12, 78, 32, 54, 69,100]
#output = 100

# Without using built-in functions
nums = [12, 78, 32, 54, 69,100]
lar = nums[0]  
for num in nums:
    if num > lar:
        lar = num  
print(lar)
#Using built-in functions
nums = [12, 78, 32, 54, 69,100]
print(max(nums))

#2) Check palindrome
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Using join and reversed()
s = input()
if s == ''.join(reversed(s)):
    print("Palindrome")
else:    
    print("Not Palindrome")

#Count even numbers using filter()
li = [1,2,3,4,5]
res = list(filter(lambda x: x%2==0, li))
print(res)

#Remove duplicates from a list using set()
li = [1,2,3,4,5,1,2]
print(set(li))

#Sum of digits using sum()
n = int(input())
res = sum(int(digit) for digit in str(n))
print(res)
'''
#Sort words alphabetically using sorted()
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)    
print(sorted_words)

#Find second largest number using sorted()
li = [10,20,30,50,100,50,60,70,100]
sorted_li = sorted(set(li))
print(sorted_li[-2])