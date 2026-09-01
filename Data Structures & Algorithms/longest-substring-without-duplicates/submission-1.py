class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxlen = 0, 0
        n = len(s)
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen