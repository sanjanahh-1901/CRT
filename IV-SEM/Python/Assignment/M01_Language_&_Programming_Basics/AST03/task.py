name = input()
n1,n2,n3 = list(map(int,input().split()))
average = (n1+n2+n3)/3
if average >= 50:
    status = "Pass"
else:
    status = "Fail"
print("Average grade:", average, "Status:", status)