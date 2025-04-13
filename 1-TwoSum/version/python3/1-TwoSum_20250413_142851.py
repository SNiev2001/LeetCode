# Last updated: 4/13/2025, 2:28:51 PM
# Uses a Hash Map to run it as fast as posible
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
    
        for i in range(n):
            complement = target - nums[i]
            if complement in map:  
                "don't need check for same index since \current one is not added yet"
                return [i, map[complement]]
            map[nums[i]] = i
        return []