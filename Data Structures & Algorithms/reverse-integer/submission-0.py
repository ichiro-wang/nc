class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MAX = 2 ** 31 - 1
        MIN = -MAX - 1

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if int(MIN / 10) > res or int(MIN / 10) == res and digit < -8:
                return 0
            if int(MAX / 10) < res or int(MAX / 10) == res and digit > 7:
                return 0
            
            res *= 10
            res += digit
        
        return res