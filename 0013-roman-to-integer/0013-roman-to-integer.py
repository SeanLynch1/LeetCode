class Solution:
    def romanToInt(self, s: str) -> int:
        
        code = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D" : 500, "M" : 1000}

        letters = list(s)
        num = 0

        for i in range(len(letters)):
            val = code[letters[i]]

            if i < len(letters) - 1:
                if (code[letters[i + 1]] / val) % 5 == 0:
                    val = -val
            
            num += val
        
        return num

