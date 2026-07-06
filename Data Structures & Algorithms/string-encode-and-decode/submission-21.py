class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + ":" + s
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while i < len(s):
            while s[j] != ":":
                j += 1
            strLength = int(s[i:j])
            i = j + 1
            j = i + strLength
            res.append(s[i:j])
            i = j
        
        return res

