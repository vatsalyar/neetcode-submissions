class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = defaultdict(int)
        freqT = defaultdict(int)

        for c in s:
            freqS[c] += 1
        for c in t:
            freqT[c] += 1
        return freqS == freqT
