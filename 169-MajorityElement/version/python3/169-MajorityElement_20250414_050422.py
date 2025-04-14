# Last updated: 4/14/2025, 5:04:22 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        head = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[head-2]:
                nums[head] = nums[i]
                head += 1

        return head

                

            
            
        