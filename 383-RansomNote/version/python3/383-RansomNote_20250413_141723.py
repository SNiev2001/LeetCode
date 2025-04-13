# Last updated: 4/13/2025, 2:17:23 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True