#Leetcode 560. Subarray Sum Equals K
from ast import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        pref_sum = 0
        count = 0
        for ele in nums:
            pref_sum += ele
            if (pref_sum - k) in freq:
                count += freq[pref_sum - k]
            freq[pref_sum] = freq.get(pref_sum, 0)
        return count
    
    