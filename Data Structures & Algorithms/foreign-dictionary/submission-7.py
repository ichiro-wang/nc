class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j >= len(w2):
                    return ""
                elif w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res = []
        cycle = set()
        visit = set()

        def dfs(c1):
            if c1 in cycle:
                return False
            if c1 in visit:
                return True
            
            cycle.add(c1)
            for c2 in adj[c1]:
                if not dfs(c2):
                    return False
            cycle.remove(c1)
            visit.add(c1)
            res.append(c1)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
