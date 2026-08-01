class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n
        res = 0
        prefix[0] = height[0]
        suffix[-1] = height[-1]
        for i, num in enumerate(height):
            if i == 0: continue
            prefix[i] = max(num, prefix[i-1])
        for i in range(n - 1, -1 ,-1):
            if i == n - 1: continue
            suffix[i] = max(suffix[i+1] , height[i])
        print(n, prefix, suffix, sep='\n')
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]
        return res