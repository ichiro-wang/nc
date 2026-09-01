"""

            lm    r
1   2   5   6 | 7
5 | 7   9   10  11


"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            p1 = nums1[m1] if m1 >= 0 else float("-inf")
            p2 = nums2[m2] if m2 >= 0 else float("-inf")
            n1 = nums1[m1 + 1] if m1 + 1 < len(nums1) else float("inf")
            n2 = nums2[m2 + 1] if m2 + 1 < len(nums2) else float("inf")

            if p1 <= n2 and p2 <= n1:
                if total % 2:
                    return min(n1, n2)
                return (max(p1, p2) + min(n1, n2)) / 2
            if p2 > n1:
                l = m1 + 1
            else:
                r = m1 - 1
        