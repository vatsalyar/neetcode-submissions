class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            a[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in a and i != a[diff]:
                return [i, a[diff]]