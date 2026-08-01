class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums = sorted(nums)
        n= len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            target = -(nums[i])
            l = i+1
            r = n-1
            while l<r:
                currsum = nums[l] + nums[r]
                if currsum < target:
                    l+=1
                elif currsum > target:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res