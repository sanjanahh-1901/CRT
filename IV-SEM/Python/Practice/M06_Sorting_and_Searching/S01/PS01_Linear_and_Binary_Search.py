#Linear Search# 
#Method 1
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
print(linear_search([12, 15, 45, 67, 89, 20], 15)) # 1
print(linear_search([12, 15, 45, 67, 89, 20], 100)) # -1

#Method 2
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
li = list(map(int, input().split()))
target1 = int(input())
print(linear_search(li, target1)) #1
target2 = int(input())
print(linear_search(li, target2)) #-1
 
#Binary Search#
#Method 1
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Method 2
