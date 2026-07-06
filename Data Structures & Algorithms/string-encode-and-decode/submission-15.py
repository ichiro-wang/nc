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
            j = i
            while s[j] != ":":
                j += 1

            num = int(s[i:j])
            i = j + 2
            j = i + num

            word = s[i:j]
            res.append(word)
            i = j

        return res
                
