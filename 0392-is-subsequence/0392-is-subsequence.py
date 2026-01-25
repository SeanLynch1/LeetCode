class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        left = 0
        right = 0

        while right < len(t):
            if left >= len(s):
                return True

            print(f"left = {s[left]}, right = {t[right]}")
            print("")

            while right < len(t) and s[left] != t[right]:
                right += 1

            left += 1
            right += 1

        if left >= len(s) and right <= len(t):
            return True

        print(f"left = {left}, right = {right}")
        return False
