from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):
            return False
        
        mag_letters = Counter(magazine)

        for char in ransomNote:
            if mag_letters[char] > 0:
                mag_letters[char] -= 1
            else:
                return False
        
        return True