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

1. Pyramid star pattern
input: n = 4
output: *
       * *
      * * *
     * * * *

#code
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "* " * i)

2. Reverse pyramid star pattern
input: n = 4
output: * * * *
         * * *
          * *
           *
#code
n = int(input())
for i in range(n, 0, -1):
    print(" "*(n-i) + "* " * i)

3. Diamond star pattern
input: n = 4    
output:    *
          * *
         * * *
        * * * *
         * * *
          * *
           *

#code
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "* " * i)

4. Number pyramid pattern
input: n = 4
output:    1
          1 2
         1 2 3
        1 2 3 4

#code
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + " ".join(str(j) for j in range(1, i+1)))

5. Hollow pyramid star pattern
input: n = 4
output:    *
          * *
         *   *
        * * * *
'''
#code
n = int(input())
for i in range(1, n+1):
    if i == 1:
        print(" "*(n-i) + "*")
    elif i == n:
        print("* " * n)
    else:
        print(" "*(n-i) + "*" + " "*(2*i-3) + "*" )