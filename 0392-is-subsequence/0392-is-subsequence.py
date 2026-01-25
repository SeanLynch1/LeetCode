class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        left = 0
        right = 0
        while right < len(t) and left < len(s):
            

            while right < len(t) and s[left] != t[right]:
                right += 1

            left += 1
            right += 1

        return left >= len(s) and right <= len(t)
