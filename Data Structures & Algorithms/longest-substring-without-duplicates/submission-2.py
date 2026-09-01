class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxlen = 0, 0
        n = len(s)
        charMap = {}
        for r in range(len(s)):
            if s[r] in charMap:
                l = max(charMap[s[r]] + 1, l)
            charMap[s[r]] = r
            maxlen = max(maxlen, r-l+1)
        return maxlen