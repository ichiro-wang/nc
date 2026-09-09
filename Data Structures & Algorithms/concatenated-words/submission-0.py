class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]
            
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix not in words:
                    continue
                suffix = word[i:]
                if suffix in words or dfs(suffix):
                    dp[word] = True
                    return True
            
            dp[word] = False
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res