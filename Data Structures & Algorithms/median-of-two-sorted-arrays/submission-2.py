class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined = nums1 + nums2
        joined.sort()
        n = len(joined)
        m = n // 2

        if n % 2 == 0:
            return (joined[m - 1] + joined[m]) /2
        else:
            return joined[m]
        