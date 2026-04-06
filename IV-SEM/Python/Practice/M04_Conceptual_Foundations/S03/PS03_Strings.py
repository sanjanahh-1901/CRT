'''
#String: Collection of characters enclosed in single or double quotes.
s = "python"
print(s[2]) #t
print(s[-1]) #n
print(s[1:]) #ython

print(s.capitalize()) #Python
print(s) #Strings are immutable, so the original string remains unchanged.

#s[0] = 'P' #This will raise an error because strings are immutable.
s.replace('p', 'P') #This will return a new string with 'p' replaced by 'P', but it does not change the original string.
print(s) #The original string is still unchanged.

#Reverse a string without using built-in functions.
#Method-1: Using slicing
s = input()
res = ""
stop = -1 * (len(s) + 1)
for i in range(-1, stop, -1):
    res += s[i]
print(res)

#Method-2: Using a loop
s = input()
res = ""
for ch in s:
    res = ch + res
print(res)

#Method-3: Using functions to reverse a string
def reverse_string(s):
    res = ""
    for ch in s:
        res = ch + res
    return res
print(reverse_string("python"))

def is_palindrome(s):
    return s == reverse_string(s)

print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False 

def frequency_count(s):
    pass 
print(frequency_count("abcabc")) # {'a': 2, 'b': 2, 'c': 2}
'''
def frequency_count(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d
print(frequency_count("abcabc")) # {'a': 2, 'b': 2, 'c': 2}

def is_anagram(s1, s2):
    return frequency_count(s1) == frequency_count(s2)

print(is_anagram("space", "paces")) # True
print(is_anagram("abc", "abcabc")) # False

#Leetcode questions:
# 3,13,28*,38,43*,65,151,165*,242,389*,771
