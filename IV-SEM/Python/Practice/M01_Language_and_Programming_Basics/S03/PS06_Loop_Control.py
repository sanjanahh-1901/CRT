'''Loop Control Statements in Python:
1. break
2. continue'''
'''
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
else:
    print("Loop completed.")
    if i == 8:
        print("The loop reached 8.")
'''
'''
Password retry system (max 3 attempts)
If password is correct, show "Login Successful"
else ask for password 3 times 
and after attempts exceed show "Account Locked"
'''

p1 = "abc123"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("Login Successful")
        break
    else:
        print("Account Locked")