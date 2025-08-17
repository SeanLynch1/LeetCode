class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1

        while right > left:
            left_letter = s[left]
            right_letter = s[right]

            if not left_letter.isalnum():
                left += 1
            elif not right_letter.isalnum():
                right -= 1
            elif left_letter.lower() == right_letter.lower():
                left += 1
                right -= 1
            else:
                return False
            
            

        return True