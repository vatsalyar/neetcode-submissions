class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0 
        r = n - 1 
        while l <= r:
            m = (l+r)//2
            mid = nums[m]
            if mid > target:
                r = m - 1
            elif mid < target:
                l = m + 1
            else:
                return m
        return -1
        