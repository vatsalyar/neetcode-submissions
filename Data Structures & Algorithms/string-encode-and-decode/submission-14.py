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
        n = (len(s))
        while i < n:
            j= s.find('#', i)
            length = int(s[i:j])
            word = str(s[j+1:j+1+length]) 
            res.append(word)           
            i = j + 1 + len(word)
            print(word)
        return (res)