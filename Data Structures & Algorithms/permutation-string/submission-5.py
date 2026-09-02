class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1, count_s2 = [0]* 26, [0]* 26
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if count_s1[i] == count_s2[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            char_r = ord(s2[r]) - ord('a')
            count_s2[char_r]+=1

            if count_s1[char_r] == count_s2[char_r]:
                matches += 1
            elif count_s1[char_r] == count_s2[char_r] - 1:
                matches -= 1
            
            char_l = ord(s2[l]) - ord('a')
            count_s2[char_l]-=1

            if count_s1[char_l] == count_s2[char_l]:
                matches += 1
            elif count_s1[char_l] == count_s2[char_l] + 1:
                matches -= 1
            l+=1
        return matches == 26
