class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")

        # Count substrings that contain ALL 5 vowels and AT MOST K consonants
        def at_most(K):
            freq = {v: 0 for v in vowels}
            distinct_vowels = 0
            consonants = 0
            total = 0
            left = 0
            min_left = 0  # minimal left index that still keeps all vowels

            for right, ch in enumerate(word):

                # Expand window
                if ch in vowels:
                    if freq[ch] == 0:
                        distinct_vowels += 1
                    freq[ch] += 1
                else:
                    consonants += 1

                # Shrink until consonants <= K
                while consonants > K:
                    left_ch = word[left]
                    if left_ch in vowels:
                        freq[left_ch] -= 1
                        if freq[left_ch] == 0:
                            distinct_vowels -= 1
                    else:
                        consonants -= 1
                    left += 1

                # Now left..right window has <= K consonants
                # But we also need all 5 vowels to be present
                # So we must push min_left forward until vowels drop
                while distinct_vowels == 5:
                    left_ch = word[min_left]
                    if left_ch in vowels:
                        if freq[left_ch] - 1 == 0:
                            break  # stop: removing it would break vowel condition
                        freq[left_ch] -= 1
                    min_left += 1

                # If all vowels present:
                if distinct_vowels == 5:
                    # all substrings starting in [left .. min_left] and ending at right are valid
                    total += (min_left - left + 1)

            return total

        # F(k) - F(k-1)
        return at_most(k) - at_most(k - 1)