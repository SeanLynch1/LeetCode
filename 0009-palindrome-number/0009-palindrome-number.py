class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        print(256)
        pres = x
        reverse = 0

        while pres > 9:

            end = pres % 10
            reverse += end
            reverse *= 10

            pres //= 10

        reverse += pres

        return x == reverse