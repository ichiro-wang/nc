class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            i += 1
            end = int(n) + i
            newWord = ""
            while i < end:
                newWord += s[i]
                i += 1
            res.append(newWord)


        return res

            

