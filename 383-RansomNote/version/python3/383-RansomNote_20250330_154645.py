# Last updated: 3/30/2025, 3:46:45 PM
# Este codigo emplea funciones para obtener la mejor respuesta en tiempo.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        letters = {}
        for a in magazine:
            if a not in letters:
                letters[a] = 1
                continue 
            letters[a] += 1

        for b in ransomNote:
            if b not in letters or letters[b] <= 0:
                return False
            else:
                letters[b] -= 1
        return True
        '''
        for c in set(ransomNote):
            if magazine.count(c)<ransomNote.count(c):
                return False
        return True


        