class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":;" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            numStr = ""
            while s[i] != ":":
                numStr += s[i]
                i += 1
            i += 2
            num = int(numStr)
            end = i + num
            word = ""
            while i < end:
                word += s[i]
                i += 1
            res.append(word)
        
        return res

