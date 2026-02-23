'''
li = [1, 2, 3, 4, 5]
output = [1, 4, 9, 16, 25]

li = list(map(int, input().split()))
for i in range(len(li)):
    li[i] = li[i] ** 2
print(li)

#output code
li = [1, 2, 3, 4, 5]
res = []
for i in li:
    res.append(i**2)
print(res)

#reduced code
li = [1, 2, 3, 4, 5]
ans = [i**2 for i in li]
print(ans)

#even numbers from the list
li = [1, 2, 3, 4, 5]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)

#reduced code
ans = [i for i in li if i % 2 == 0]
print(ans)

print(" * "*5)
li = ['a', 'b', 'c'] #'a b c'
for i in li:
    print(i, end=" ")

li = ['a', 'b', 'c']
res = []
for ch in li:
    res = res + [ch] +[" "]  #res.append(ch) can also be used
print(res)

print("@".join(li))  #a@b@c
'''
