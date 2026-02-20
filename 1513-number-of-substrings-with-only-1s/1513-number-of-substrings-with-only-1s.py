class Solution:
    def numSub(self, s: str) -> int:
        
        total = 0
        right = 0
        for i in range(len(s)):
            if s[i] == "1":
                while right < len(s) and s[right] == "1":

                    total += right - i + 1
                    right += 1

            else:
                right = i + 1
        return total % ((10**9) + 7)