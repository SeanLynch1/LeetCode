class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set("aeiou")
        total = 0

        for i in range(len(word)):

            right = i
            found = set()
            while right < len(word) and word[right] in vowels:
                found.add(word[right])
                if len(found) == 5:
                    total += 1

                right += 1

        return total