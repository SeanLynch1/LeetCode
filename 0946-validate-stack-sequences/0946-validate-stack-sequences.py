class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        n = len(popped)
        left = 0
        right = 0

        while left < n:
                
            while left < n and pushed[left] != popped[right]:
                stack.append(pushed[left])
                left += 1

            if left >= n:
                break

            stack.append(pushed[left])

            while stack and stack[-1] == popped[right]:
                stack.pop()
                right += 1

            left += 1

        return True if len(stack) == 0 else False