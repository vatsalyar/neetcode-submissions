class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] = res.get(num, 0) + 1
        elements = []
        res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            elements.append(list(res.keys())[i])
        return elements
