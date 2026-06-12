class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]
        for num in nums:
            freq[num] += 1
        for n, i in freq.items():
            buckets[i].append(n)
        i=len(buckets) - 1 
        j=0
        lst=[]
        while i >= 0:
            if buckets[i]:
                for num in buckets[i]:
                    if j >= k: return lst
                    lst.append(num)
                    j+=1
            i -= 1
        return lst