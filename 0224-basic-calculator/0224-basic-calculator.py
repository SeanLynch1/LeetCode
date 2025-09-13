class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # stores number inside brackets that haven't been finished yet, used to update result
        result = 0 # the final result, is updated when a bracket is closed or at the return
        sign = 1 # the sign before the bracket, that the number inside will be multiplied by
        number = 0 # the temporary numbre in brackets that will be added to result once bracket is closed

        for char in s:

            if char.isdigit():
                # for numbers next to each other '123', 1, then 10 + 2, then 120 + 3
                number = number * 10 + int(char)
            elif char == "+":
                # update result
                result += number * sign
                number = 0
                sign = 1
            elif char == "-":
                result += number * sign
                number = 0
                sign = -1
            elif char == ")":
                result += number * sign
                result *= stack.pop()
                result += stack.pop()
                number = 0
                sign = 1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            print("char = ", char)
            print(f"result = {result}")
            print(stack, "\n")

        return result + (number * sign)
