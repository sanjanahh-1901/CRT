#Digital root sum
#386 --> 17 --> 8
def digital_sum(n):
    if n <= 0:
        return n
    s = sum([int(ch) for ch in str(n)])
    return digital_sum(s)
print(digital_sum(386)) # 8

#Sorted array
def sorted_array(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True
print(sorted_array([10, 20, 30, 40, 50])) # True
print(sorted_array([10, 4, 30, 25, 50])) # False
   