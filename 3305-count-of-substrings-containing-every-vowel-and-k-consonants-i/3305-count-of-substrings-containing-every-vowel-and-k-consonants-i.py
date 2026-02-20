class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowel_set = set("aeiou")
        total = 0
        n = 5 + k

        for i in range(len(word)):

            vowels = set()
            consonants = 0
            right = i
            while right < len(word):
                
                nxt_letter = word[right]

                if nxt_letter in vowel_set:
                    vowels.add(nxt_letter)
                else:
                    consonants += 1

                if consonants > k:
                    break

                if len(vowels) + consonants == n:
                    total += 1

                right += 1


        return total