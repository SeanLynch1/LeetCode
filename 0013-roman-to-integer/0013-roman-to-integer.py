class Solution:
    def romanToInt(self, s: str) -> int:
        
        code = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D" : 500, "M" : 1000}

        num = 0
        n = len(s)
        i = 0

        while i < n:
            val = code[s[i]]

            if i < n - 1:
                if (code[s[i + 1]] / val) % 5 == 0:
                    val = code[s[i + 1]] - val
                    i += 1
            
            print("i = , ",i ,val)
            num += val
            i += 1
        
        return num

