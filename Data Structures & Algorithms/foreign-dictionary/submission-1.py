class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j >= len(w2):
                    return ""
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    adj[c1].add(c2)
                    break
        
        visit = {}
        res = []
        def dfs(c1):
            if c1 in visit:
                return visit[c1]

            visit[c1] = True
            for c2 in adj[c1]:
                if dfs(c2):
                    return True
            visit[c1] = False
            res.append(c1)
        
        for c in adj.keys():
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)