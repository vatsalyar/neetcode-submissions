class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        l = 0
        max_freq = 0
        for r in range(len(s)):
            charMap[s[r]] += 1
            max_freq = max(max_freq, charMap[s[r]])
            noR = (r-l+1) - max_freq
            if noR > k:
                charMap[s[l]] -= 1
                l += 1
        return len(s) - l 