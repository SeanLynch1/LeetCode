class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"
        mapping = set(str())

        for c in letters:
            mapping.add(c)

        
        left = 0
        right = len(s) - 1
 
        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()
            print(f"left = {left_char}")
            print(f"right = {right_char}")
            print("")

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

        print(left)
        print(right)
        if s[left].lower() != s[right].lower():
            return False

        return True