class Solution:
    def intToRoman(self, num: int) -> str:
        
        code = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        numeral = []

        for key, value in code:
            
            count = num // key
            num = num % key

            numeral.append(value * count)

        return ''.join(numeral)

