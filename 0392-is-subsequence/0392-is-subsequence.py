class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
            
        left = 0
        right = 0

        while right < len(t):
            
            while right < len(t) and s[left] != t[right]:
                right += 1

            left += 1
            right += 1

            print(f"left = {left}, right = {right}")
            if left >= len(s):
                return True

        return False
