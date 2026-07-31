class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        for curr in range(n):
            r = n-1
            diff = target - numbers[curr] 
            l = curr + 1
            while l <= r:
                mid = (l + r)//2
                m = numbers[mid]
                if diff < m:
                    r = mid - 1
                elif diff > m:
                    l = mid + 1
                else:
                    return [curr+1, mid +1]
        return res