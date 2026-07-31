class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        for l in range(n):
            r = n-1
            diff = target - numbers[l] 
            while l < r:
                if numbers[r] == diff:
                    return [l+1, r+1]
                else:
                    r-=1

        