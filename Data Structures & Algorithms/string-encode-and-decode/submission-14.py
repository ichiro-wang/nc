class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":;" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            numStr = ""
            while s[i] != ":":
                numStr += s[i]
                i += 1
            num = int(numStr)
            i += 2
            end = i + num
            word = ""
            while i < end:
                word += s[i]
                i += 1
            res.append(word)
        
        return res


