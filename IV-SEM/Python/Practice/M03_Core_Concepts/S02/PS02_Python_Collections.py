'''
Python Collections


#1)


#2) Accessing a list:
a = [10, 20, 30, 40, 50]
print(a[0])  # O(1)
print(a[-1])  # O(1)

#3)








































'''
#4) Adding elements to a list:
a = [10, 20, 30, 40, 50]
a.append(100)  # O(1)




#5) Removing elements from a list:
a = [10, 20, 30, 40, 50]
a.remove(40)  # O(n)
print(a)
a.pop()  # O(1)
print(a)

#6) Slicing:
a = [10, 20, 30, 40, 50]
print(a[0:])  # O(k) where k is the size of the slice
print(a[2:])  # O(k) where k is the size of the slice
#reversing a list using slicing
print(a[::-1]) 
















#5) Set Operations:
a = set([10, 20, 30, 450])
b = set([20, 30, 40, 50])



#7) LeetCode 169

#8) LeetCode 88

#9) LeetCode 268

#10) LeetCode 575

t = (10, 20, 30, 40, 50)
print(t)
t1=tuple((10, 20, 30, 40, 50))
print(t1)
print(t[0])  # O(1
print(t[-1])  # O(1)
print(t+t1)  # O(n)
print(tuple(t,t1))  # O(n)
print(t*3)  # O(n)
print(t[0:])  # O(k) where k is the size of the slice
print(t1[1:3])  # O(k) where k is the size of the slice
del t 
print(t)  # This will raise an error since t is deleted

#LeetCode 349
#LeetCode 657

'''
Dictionary:
i) Definition: A collection of key-value pairs where each key is unique.
ii) Creation ({}, dict())
iii) Accessing dict items
iv) Adding & updating items (assignment)
v) Removing items (del, pop(), clear())
vi) LeetCode problems on Dictionary(1, 242)
'''
d={'name':'sanjana','a':'anvikha','age':23}

print(d1)
print(d1['name'])  # O(1)
print(d1.get('name'))  # O(1)
print(d1.keys())  # O(n)
print(d1.values())  # O(n)
print(d1.getitem('a'))
d1['name']='renupriya'  # O(1)

d={'name':'sanjana','a':'anvikha','age':23}
print(d)
del d
print(d)  # This will raise an error since d is deleted

val=d1.pop('a')  # O(1)
print(val)
print(d)

d1.clear()  # O(1)
print(d1)  # This will print an empty dictionary

#LeetCode 242
