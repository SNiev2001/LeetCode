# Last updated: 4/13/2025, 2:16:36 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for a in magazine:
            if a not in dic:
                dic[a] = 0
            dic[a] += 1
        
        for a in ransomNote:
            if a not in dic:
                return False
            if dic[a] == 0:
                return False
            else:
                dic[a] -= 1
        
        return True

        