class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(len(nums)):
                if nums[j] == diff and i != j: return list((i,j))           