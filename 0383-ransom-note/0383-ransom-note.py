
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):
            return False
        

        mag_letters = {}
        for letter in magazine:
            if letter not in mag_letters:
                mag_letters[letter] = 1
            else:
                mag_letters[letter] += 1

        for char in ransomNote:
            if char in mag_letters:
                if mag_letters[char] > 0:
                    mag_letters[char] -= 1
                else:
                    return False
            else:
                return False
        
        return True