# Last updated: 4/14/2025, 5:02:42 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Position for next non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k  # New length of the modified array
        