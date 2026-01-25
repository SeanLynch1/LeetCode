class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        mapping = set("abcdefghijklmnopqrstuvwxyz0123456789")

        left = 0
        right = len(s) - 1
 
        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            if left_char not in mapping:
                left += 1
                continue

            if right_char not in mapping:
                right -= 1
                continue

            if left_char != right_char:
                return False

            left += 1
            right -= 1

        return True