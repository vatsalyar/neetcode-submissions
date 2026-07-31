class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for n in range(len(numbers)):
            diff = target - numbers[n] 
            if diff in hm:
                return [hm[diff] + 1, n+1]
            hm[numbers[n]] = n
        return []