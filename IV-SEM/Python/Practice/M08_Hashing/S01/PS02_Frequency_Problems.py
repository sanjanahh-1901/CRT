'''
##Frequency Problems##
#Count frequency of each element
#[1,2,4,3,1,2,5] ==> {1:2, 2:2, 3:1, 4:1, 5:1}    
li = list(map(int, input().split()))
#Without using get method 
d = {}
for el in li:
    if el not in d:
        d[el] = 1
    else:
        d[el] += 1  
print(d)

#Using get method
d1 = {}
for el in li:
    d1[el] = d1.get(el, 0) + 1
print(d1)

from collections import Counter
print(Counter(li))

#Find all distinct elements
#[1,2,4,3,1,2,5] ==> {1, 2, 3, 4, 5}

li = list(map(int, input().split()))
s = set()
for el in li:
    if el not in s:
        s.add(el)
print(list(s))

#Find the element with maximum frequency
#[1,2,4,3,1,2,5,1] ==> 1
#VS Code Soln
li = list(map(int, input().split()))
d = {}
for el in li:
    d[el] = d.get(el, 0) + 1
max_freq = 0
max_freq_el = None
for el, freq in d.items():
    if freq > max_freq:
        max_freq = freq
        max_freq_el = el
print(max_freq_el)
'''
#Class Soln
from collections import Counter
li = list(map(int, input().split()))
freq = Counter(li)
print(max(freq, key=freq.get))

max_freq = max(freq.values())
for k in freq:
    if freq[k] == max_freq:
        print(k)

#Majority Element
#[1,2,3,2,2] ==> 2
#LeetCode 169. Majority Element
li = list(map(int, input().split()))
freq = Counter(li)
print(max(freq, key=freq.get))

