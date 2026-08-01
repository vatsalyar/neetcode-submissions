class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0 
        r = len(heights) -1
        while l<r:
            m = min(heights[l], heights[r])
            area = (r-l)*m
            if area > res:
                res = area 
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res 