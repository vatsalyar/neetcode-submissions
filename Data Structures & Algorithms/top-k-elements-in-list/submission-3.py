class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets=[[] for _ in range(len(nums)+1)]
        for num in nums:
            freq[num] += 1
        for n, i in freq.items():
            buckets[i].append(n)
        l = 0
        res = []
        print(buckets)
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)
                    l+=1
            if l >= k:
                return res