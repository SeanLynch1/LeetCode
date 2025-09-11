class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"*","-","+","/"}

        for token in tokens:

            if token not in ops:
                stack.append(int(token))
            elif len(stack) > 1:
                val1 = stack.pop()
                val2 = stack.pop()

                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                else:
                    stack.append(int(val2 / val1))

        return stack[0]