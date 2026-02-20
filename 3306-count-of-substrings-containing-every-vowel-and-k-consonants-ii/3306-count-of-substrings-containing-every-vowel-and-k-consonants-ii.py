class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atMost(k):
            if k < 0:
                return 0
            
            vowels = set('aeiou')
            last_seen = {}
            left = 0
            consonants = 0
            res = 0

            for right,ch in enumerate(word):

                if ch in vowels:
                    last_seen[ch] = right
                else:
                    consonants += 1

                while consonants > k:
                    if word[left] not in vowels:
                        consonants -= 1

                    left += 1

                if len(last_seen) == 5:
                    min_last = min(last_seen.values())
                    if min_last >= left:
                        res += min_last - left + 1

            return res

        return atMost(k) - atMost(k - 1)