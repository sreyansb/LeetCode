#attempt1:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for char in ransomCounter:
            if char not in magazineCounter or magazineCounter[char]<ransomCounter[char]:
                return False
        return True
        
