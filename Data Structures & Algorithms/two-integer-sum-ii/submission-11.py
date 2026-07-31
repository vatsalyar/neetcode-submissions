class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0, len(numbers) -1
        while l < r:
            currsum = numbers[l] + numbers[r]
            if target > currsum:
                l +=1
            elif target < currsum:
                r-=1
            else:
                return [l+1, r+1]
        return[]