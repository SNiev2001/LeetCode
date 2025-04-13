# Last updated: 4/13/2025, 2:25:42 PM
# Easy implementation
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if (nums[a] + nums[b]) == target:
                    return [a, b]
        return False

        