class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowel_set = set("aeiou")
        n = 5 + k

        def countSubstrings(nk: int) -> int:

            vowels = defaultdict(int)
            consonants = 0
            total = 0
            left = 0
            right = 0

            while right < len(word):
                letter = word[right]

                if letter not in vowel_set:
                    consonants += 1
                else:
                    vowels[letter] += 1

                while len(vowels) + consonants > nk or consonants > k:
                    letter_left = word[left]

                    if letter_left in vowel_set:
                        vowels[letter_left] -= 1

                        if vowels[letter_left] == 0:
                            del vowels[letter_left]

                    else:
                        consonants -= 1

                    left += 1

                total += right - left + 1
                right += 1

            return total
                
        return countSubstrings(n) - countSubstrings(n - 1)