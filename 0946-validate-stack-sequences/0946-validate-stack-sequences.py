class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []

        n = len(popped)
        left = 0
        right = 0

        while left < n:
                
            while pushed[left] != popped[right]:
                print(f"left = {pushed[left]}, right = {popped[right]}")
                stack.append(pushed[left])
                left += 1

            print(f"stack = {stack}")

            stack.append(pushed[left])
            print(f"stack = {stack}")

            while stack and stack[-1] == popped[right]:
                stack.pop()
                right += 1
                print(f"stack = {stack}")

            left += 1
            if left < n and right < n:
                print(f"left = {pushed[left]}, right = {popped[right]}")
            else:
                print(f"left idx = {left}, right idx = {right}")

            print("")

        print(stack)

        return True if len(stack) == 0 else False