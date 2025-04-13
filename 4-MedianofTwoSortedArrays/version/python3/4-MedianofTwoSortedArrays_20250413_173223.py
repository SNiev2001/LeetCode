# Last updated: 4/13/2025, 5:32:23 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        n = len(nums1)
        m = len(nums2)
        
        i = j = k = 0

        while i < n and j <m:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        while i < n:
            res.append(nums1[i])
            i += 1
        while j < m:
            res.append(nums2[j])
            j += 1

        total = len(res)
        
        if total % 2 == 1:
            return float(res[total // 2])
        else:
            mid = total // 2
            return (res[mid - 1] + res[mid]) / 2.0