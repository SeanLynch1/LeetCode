
class Solution:
    def isHappy(self, n: int) -> bool:
        
        happy_number = n
        found_numbers = set()

        while happy_number != 1:
            
            total = 0
            num = happy_number

            while num > 0:
                num, digit = num // 10, num % 10 # gets the first digit, can contain more than one digit, that's why we loop
                # gets the second digit

                print(num, digit)
                total += digit ** 2

            happy_number = total
            print(happy_number)
            if happy_number not in found_numbers:
                found_numbers.add(happy_number)
            else:
                return False

        return True