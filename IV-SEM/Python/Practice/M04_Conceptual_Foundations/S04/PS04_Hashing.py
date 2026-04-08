'''
1. Keys should be immutable (like strings, numbers, tuples).
2. Keys should be unique (no duplicate keys allowed).
'''
d = {1:'a', 2:'b', 3:'c', 1:'z'}
print(d) # {1: 'z', 2: 'b', 3: 'c'} - The value for key 1 is overwritten by the last assignment.

