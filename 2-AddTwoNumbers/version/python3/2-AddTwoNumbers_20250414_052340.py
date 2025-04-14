# Last updated: 4/14/2025, 5:23:40 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10 == 0:
            return True
        
        arr = []
        while x / 10 != 0:
            arr.append(x%10)
            x=x//10
        n=len(arr)
        for i in range(n//2):
            print(arr)
            print(arr[i],arr[n-1-i])
            if arr[i] != arr[n-1-i]:
                return False
        return True
        