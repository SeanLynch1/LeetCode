class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        

        total = 0

        vowels = set("aeiou")


        for left in range(len(word)):
            
            right = left
            found = set()

            while right < len(word) and word[right] in vowels:
                found.add(word[right])

                if len(found) == 5:
                    total += 1
                
                right += 1


        return total