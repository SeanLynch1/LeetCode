
class Solution:
    def isHappy(self, n: int) -> bool:
        
        happy_number = n

        found_numbers = set()

        while happy_number != 1:
            digits = list(str(happy_number))

            happy_number = 0

            for digit in digits:
                happy_number += (int(digit) ** 2)
            
            if happy_number not in found_numbers:
                found_numbers.add(happy_number)
            else:
                return False

        return True