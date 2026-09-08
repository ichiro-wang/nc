class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        odd = 0
        even = 0
        for char, cnt in count.items():
            if cnt % 2 == 0:
                even += cnt
            else:
                even += cnt - 1
                odd = 1
            
        return even + odd