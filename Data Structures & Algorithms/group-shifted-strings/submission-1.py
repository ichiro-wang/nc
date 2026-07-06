class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = {}

        for s in strings:
            key = []
            first = s[0]
            for c in s:
                key.append((ord(first) - ord(c)) % 26)
            key = tuple(key)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values())
                