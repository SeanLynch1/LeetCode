class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        longest = 0
        curr_len = 0
        curr_vowels = 0

        for i, ch in enumerate(word):
            if i > 0 and ch < word[i - 1]:
                curr_len = 0
                curr_vowels = 0

            if curr_len == 0:  # starting new substring
                if ch == 'a':
                    curr_vowels = 1
                    curr_len = 1
            else:
                curr_len += 1
                if ch != word[i - 1]:
                    curr_vowels += 1

            if curr_vowels == 5:
                longest = max(longest, curr_len)

        return longest