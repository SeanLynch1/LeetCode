class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first = {0: -1}
        mask = 0
        ans = 0

        bits = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }

        for i, c in enumerate(s):
            if c in bits:
                mask ^= 1 << bits[c]

            if mask not in first:
                first[mask] = i
            else:
                ans = max(ans, i - first[mask])

        return ans