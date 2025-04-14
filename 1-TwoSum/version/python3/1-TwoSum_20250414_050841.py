# Last updated: 4/14/2025, 5:08:41 AM
class Solution:
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if (nums[a] + nums[b]) == target:
                    return [a, b]
        return False
    '''
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

        