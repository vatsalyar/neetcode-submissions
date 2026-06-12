class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return (res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        n = len(s)
        while i < n and j < n:
            if s[i] != '#':
                i+=1
                continue
            length = int(s[j:i])
            word = str(s[i+1:i+1+length]) 
            res.append(word)           
            j = i + 1 +len(word)
            i=j
        return (res)