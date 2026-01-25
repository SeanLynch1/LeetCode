class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        mapping = set("abcdefghijklmnopqrstuvwxyz0123456789")

        left = 0
        right = len(s) - 1
 
        while left < right:
            while left < right and s[left].lower() not in mapping:
                left += 1

            while right > left and s[right].lower() not in mapping:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True