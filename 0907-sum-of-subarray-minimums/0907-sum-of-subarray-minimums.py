class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        output = 0

        for i, num in enumerate(arr):
            
            while stack and num < stack[-1][1]:
                j, m = stack.pop()

                left = j - stack[-1][0] if stack else j + 1
                right = i - j

                output = (output + m * left * right) % (10 ** 9 + 7)       
                
            stack.append([i, num])

        for i in range(len(stack)):
            
            j, num = stack[i]

            left = j - stack[i-1][0] if i > 0 else j + 1

            right = len(arr) - j

            output = (output + num * left * right) % (10 ** 9 + 7)

        return output 