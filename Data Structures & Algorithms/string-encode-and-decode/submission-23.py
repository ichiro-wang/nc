class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + ";" + s
        return string

    def decode(self, s: str) -> List[str]:
        res = []

        r = 0
        while r < len(s):
            l = r
            while s[r] != ";":
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            res.append(s[l:r])
        
        return res
