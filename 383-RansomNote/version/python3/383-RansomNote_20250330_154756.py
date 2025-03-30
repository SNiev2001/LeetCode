# Last updated: 3/30/2025, 3:47:56 PM
# It has the best performance and saves the most memory
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}

        for c in magazine:
            magazine_map[c] = 1 + magazine_map.get(c, 0)
        
        for c in ransomNote:
            if c not in magazine_map or magazine_map[c] <= 0:
                return False
            magazine_map[c] -= 1
        
        return True
        
        