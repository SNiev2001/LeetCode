# Last updated: 3/30/2025, 1:01:04 PM
# This approach employs a different array because of issues that may occur when modifying the original array.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        answer.append(nums[0])
        for i in range(1,len(nums)):
            answer.append(nums[i]+answer[i-1])
        
        return answer
        
        