from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")

        def atMost(k: int) -> int:
            cnt = defaultdict(int)
            left = 0
            distinct = 0
            ans = 0

            for right, ch in enumerate(word):
                if ch not in vowels:
                    # reset on consonant
                    cnt.clear()
                    left = right + 1
                    distinct = 0
                    continue

                if cnt[ch] == 0:
                    distinct += 1
                cnt[ch] += 1

                while distinct > k:
                    c = word[left]
                    cnt[c] -= 1
                    if cnt[c] == 0:
                        distinct -= 1
                    left += 1

                # number of valid substrings ending at right
                ans += right - left + 1

            return ans

        return atMost(5) - atMost(4)
