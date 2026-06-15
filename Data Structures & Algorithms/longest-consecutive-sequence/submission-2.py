class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        cur = 1
        long = 1
        nums = sorted(list(set(nums)))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1: 
                cur += 1
                if cur > long: long = cur
            else: 
                if cur > long: long = cur 
                cur = 1 
        return long