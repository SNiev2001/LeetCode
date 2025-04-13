# Last updated: 4/13/2025, 5:30:48 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        total = len(merged)
        mid = total // 2

        if total % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return float(merged[mid])

        

        