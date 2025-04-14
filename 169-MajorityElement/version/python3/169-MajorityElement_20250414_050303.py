# Last updated: 4/14/2025, 5:03:03 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] not in nums2:
                nums2.add(nums[i])
                nums[k] = nums[i]
                k += 1   
            
        return k
                