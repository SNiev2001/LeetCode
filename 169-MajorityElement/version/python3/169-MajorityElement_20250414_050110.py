# Last updated: 4/14/2025, 5:01:10 AM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2
        nums1[:m+n] = sorted(nums1[:m] + nums2)
        """
        i = m - 1  # pointer for nums1
        j = n - 1  # pointer for nums2
        k = m + n - 1  # pointer for final position in nums1

        # Merge from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has leftovers
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
                
                
        