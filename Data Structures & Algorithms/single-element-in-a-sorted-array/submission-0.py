class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            mMid = nums[m]
            mLeft = nums[m - 1] if m - 1 >= 0 else -1
            mRight = nums[m + 1] if m + 1 < len(nums) else -1

            if mMid != mLeft and mMid != mRight:
                return mMid
            
            if mMid == mLeft:
                if (r - m) % 2 == 0:
                    r = m - 2
                else:
                    l = m + 1
            else:
                if (m - l) % 2 == 0:
                    l = m + 2
                else:
                    r = m - 1
        
        return -1