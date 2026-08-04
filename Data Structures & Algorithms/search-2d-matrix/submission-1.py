class Solution:
    def search (self, nums: List[int], target: int) -> bool:
        i = 0 
        j = len(nums) - 1
        while i <=j:
            mid = i + (j-i)//2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i=mid+1
            else: 
                return True
        return False  
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0 
        r = m-1
        while l <= r:
            if target < matrix[l][-1]:
                return self.search(matrix[l], target)
            elif target > matrix[l][-1]:
                l+=1
            else:
                return True
        return False 
