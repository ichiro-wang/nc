class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # hrn,hrf
        # n -> f
        # hrf,er
        # h -> e
        # er,enn
        # r -> n
        # enn,rfnn
        # e -> r
        alienDict = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j >= len(w2):
                    return ""
                if w1[j] != w2[j]:
                    alienDict[w1[j]].add(w2[j])
                    break
        
        res = []
        cycle, visit = set(), set()

        def dfs(c1):
            if c1 in cycle:
                return False
            if c1 in visit:
                return True
            cycle.add(c1)
            visit.add(c1)

            for c2 in alienDict[c1]:
                if not dfs(c2):
                    return False
            
            res.append(c1)
            cycle.remove(c1)
            return True
        
        for c in alienDict:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
        
                