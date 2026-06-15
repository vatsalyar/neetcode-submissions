class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        cur = 1
        long = 1
        nums = sorted(list(set(nums)))
        nums_set = set(nums)
        for i in range(1, len(nums)):
            if nums[i] - 1 not in nums_set:
                cur = 1
                continue
            if nums[i] - nums[i-1] == 1: 
                cur += 1
                if cur > long: long = cur
        return long