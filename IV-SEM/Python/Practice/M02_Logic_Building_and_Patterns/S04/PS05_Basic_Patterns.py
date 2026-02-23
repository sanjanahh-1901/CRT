'''
#square star pattern
n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end=" ")
    print()

#right angle triangle star pattern
n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):   #for j in range(n): can also be used 
        print("*", end=" ")
    print()
'''

#inverted right angle triangle star pattern
n = int(input())
for i in range(1, i+1):
    for j in range(1, n+1):
        print("*", end=" ")
    print()

#diamond star pattern
n = int(input())    
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print("*", end=" ")
    print()