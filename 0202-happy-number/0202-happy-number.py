class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num: int) -> int:
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit * digit
            return total

        slow = n
        fast = sum_of_squares(n)
        print("slow = ", slow)
        print("fast = ", fast)
        print("\n")

        
        while fast != 1 and slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

            print("slow = ", slow)
            print("fast = ", fast)

            print("\n")

        return fast == 1
