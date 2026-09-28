"""
hit -> *it, h*t, hi*

*it ->
h*t -> hot
hi* ->

hot -> *ot, h*t, ho*

*ot -> hot, dot, lot
h*t -> hot
ho* -> 

dot -> *ot, d*t, do*

do* -> dog

dog -> *og, d*g, do*

*og -> cog


"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = defaultdict(list)
        for word in wordList:
            if word == beginWord:
                continue
            for i in range(len(word)):
                seq = word[:i] + "*" + word[i + 1:]
                words[seq].append(word)
        
        q = deque([[beginWord, 1]])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                seq = word[:i] + "*" + word[i + 1:]
                while words[seq]:
                    q.append([words[seq].pop(), dist + 1])
        
        return 0