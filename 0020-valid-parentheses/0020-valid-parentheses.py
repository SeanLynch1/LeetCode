class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            
            if char in pairs and stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True