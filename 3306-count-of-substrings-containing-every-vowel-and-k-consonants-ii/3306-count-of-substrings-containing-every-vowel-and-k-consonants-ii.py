class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowel_set = set("aieou")
        n = 5 + k

        def countSubstrings(nk: int) -> int:
            
            total = 0
            consonants = 0
            vowels = defaultdict(int)

            left = 0
            right = 0

            while right < len(word):
                
                letter = word[right]
                if letter in vowel_set:
                    vowels[letter] += 1
                else:
                    consonants += 1

                while len(vowels) + consonants > nk or consonants > k:
                    nxt_letter = word[left]

                    if nxt_letter in vowel_set:
                        vowels[nxt_letter] -= 1

                        if vowels[nxt_letter] == 0:
                            del vowels[nxt_letter]
                    else:
                        consonants -= 1

                    left += 1

                total += right - left + 1
                right += 1

            return total

        return countSubstrings(n) - countSubstrings(n - 1)