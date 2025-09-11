class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"*","-","+","/"}

        for token in tokens:

            if token not in ops:
                stack.append(int(token))
            elif len(stack) > 1:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(int(val2 / val1))

        return stack[0]