class Solution:
    def numberOfWeakCharacters(self, properties):
        # Step 1: Sort by attack ASC, defense DESC
        properties.sort(key=lambda x: (x[0], -x[1]))

        stack = []
        weak = 0

        # Step 2: Build a monotonic decreasing stack (on defense)
        for atk, df in properties:
            # If the current character has strictly higher attack AND defense
            # than the top of the stack, then the top is weak.
            while stack and stack[-1][0] < atk and stack[-1][1] < df:
                stack.pop()
                weak += 1

            # Push current character onto the stack
            stack.append((atk, df))

        return weak