'''
1. Pascal's Triangle
Input: n = 5
Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Code:
n = int(input())
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()      

2. Butterfly Pattern
Input: n = 4
Output:
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *

Code:
n = int(input())
for i in range(1, n+1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
for i in range(n, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)
'''