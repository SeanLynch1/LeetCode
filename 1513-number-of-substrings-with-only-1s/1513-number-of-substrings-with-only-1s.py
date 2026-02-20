class Solution:
    def numSub(self, s: str) -> int:
        
        total = 0
        left = 0
        right = 0

        while right < len(s):
            while right < len(s) and s[right] == "1":
                print(s[left:right+1])
                total += right - left + 1
                right += 1
            else:
                right += 1

            left = right

        return total % ((10**9) + 7)