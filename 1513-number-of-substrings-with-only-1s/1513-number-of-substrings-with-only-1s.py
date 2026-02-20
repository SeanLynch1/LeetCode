class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        run = 0  # current streak length of '1's

        for c in s:
            if c == '1':
                run += 1          # extend the current streak
                total += run      # add all substrings ending here
            else:
                run = 0           # streak broken

        return total % MOD