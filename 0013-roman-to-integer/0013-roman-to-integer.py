class Solution:
    def romanToInt(self, s: str) -> int:
        
        code = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D" : 500, "M" : 1000}

        num = 0

        for i in range(len(s)):
            val = code[s[i]]

            if i < len(s) - 1:
                if (code[s[i + 1]] / val) % 5 == 0:
                    val = -val
            
            num += val
        
        return num

