class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r= n - 1
        ans = float('inf')
        while l<=r:
            mid = l + (r-l)//2
            ans = min(ans, nums[mid])

            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l = mid + 1
            else:
                r = mid - 1
        return ans  
        
        