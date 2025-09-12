class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0   # current accumulated result
        number = 0   # current number being built
        sign = 1     # +1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)  # build multi-digit numbers

            elif char == '+':
                result += sign * number
                number = 0
                sign = 1

            elif char == '-':
                result += sign * number
                number = 0
                sign = -1

            elif char == '(':
                # push the result and sign before the parenthesis
                stack.append(result)
                stack.append(sign)
                # reset for new sub-expression
                result = 0
                sign = 1

            elif char == ')':
                result += sign * number
                number = 0
                result *= stack.pop()  # stack.pop() = sign before '('
                result += stack.pop()  # stack.pop() = result calculated before '('

            # ignore spaces

        return result + sign * number
