class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        vowels = ["a","e","i","o","u"]

        left = 0
        total = 0


        while left < len(word):

            target = 0
            right = left
            while right < len(word) and (word[right] == vowels[target]):
                
                if target < len(vowels) - 1 and right < len(word) - 1 and word[right + 1] != word[right]:
                    target += 1
                
                if word[right] == vowels[-1]:
                    total = max(total, right - left + 1)
    

                right += 1

            if right > left:
                left = right
            else:
                left += 1   

        return total