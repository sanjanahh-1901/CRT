from typing import List

def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

li = list(map(int, input().split()))
target = int(input())
print(binary_search(li, target)) # 1

#LeetCode 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
li = list(map(int, input().split()))
target = int(input())
s = Solution()
print(s.searchInsert(li, target)) # 2

#LeetCode 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            hours = sum((pile - 1) // mid + 1 for pile in piles)
            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low
piles = list(map(int, input().split()))
h = int(input())
s = Solution()
print(s.minEatingSpeed(piles, h)) # 4

