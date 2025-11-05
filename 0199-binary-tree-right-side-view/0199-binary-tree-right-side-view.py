# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        output = []
        stack = [(root, 1)]

        while stack:
            curr, depth = stack.pop()

            if depth > len(output):
                output.append(curr.val)


            if curr.left:
                stack.append((curr.left, depth + 1))
            if curr.right:
                stack.append((curr.right, depth + 1))
            




        return output
        