class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        tree = self.root
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree["end"] = True

    def search(self, word: str, tree=None) -> bool:
        tree = tree if tree is not None else self.root
        for i, c in enumerate(word):
            if c == ".":
                for char, subtree in tree.items():
                    if char == "end":
                        continue
                    if self.search(word[i + 1:], subtree):
                        return True
                return False
            if c not in tree:
                return False
            tree = tree[c]
        return "end" in tree